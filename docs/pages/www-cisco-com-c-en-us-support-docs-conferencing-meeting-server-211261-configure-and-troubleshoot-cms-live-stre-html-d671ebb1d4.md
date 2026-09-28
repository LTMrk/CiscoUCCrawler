---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-211261-configure-and-troubleshoot-cms-live-stre-html-d671ebb1d4
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/211261-Configure-and-Troubleshoot-CMS-live-stre.html
retrieved_at: 2026-08-21T13:12:32.774651+00:00
---

Configure and Troubleshoot CMS Live Streaming with VBrick DME

# Configure and Troubleshoot CMS Live Streaming with VBrick DME

### Download Options

Updated: February 22, 2021

Document ID: 211261

Contents

## Contents

## Introduction

This document describes the steps to configure and troubleshoot Cisco Meeting Server (CMS) integration with VBrick Distributed Media Engine (DME). CMS integration with VBrick has been added in Version 2.1 and later.

For CMS Versions 2.1 to 2.9, the CMS streaming service relied on the Extensible Messaging and Presence Protocol (XMPP) component to authenticate and join CMS conferences. In Versions 3.0 and later, due to the removal of the XMPP component, the CMS streamer service is not a Session Initiation Protocol (SIP)-based client and is joined into CMS conference by being called using SIP method.

## Prerequisites

### Requirements

- CMS Callbridge(s) Version 2.9 or earlier with Recording/Streaming license(s). (one recording license will allow one streaming call)

- CMS XMPP Version 2.9 or earlier

- Vbrick DME (used for publishing the live stream from CMS Streaming service)

- Vbrick REV (optional: only required if Live Streaming needs to be shared outside internal network or multicast)

- CMS Callbridge(s) Version 3.0 or later with Recording/Streaming license(s). (one recording license will allow one streaming call)

- Vbrick DME (used for publishing the live stream from CMS Streaming service)

- Vbrick REV (optional: only required if Live Streaming need to be shared outside internal network or multicast)

### Components Used

- CMS 2.9.5 (for streaming service and Callbridge, on separate VMs)

- Vbrick DME 3.15.0 RHEL7

Tip : Cisco recommends that the CMS VM hosting the streaming serivce, running Version 2.9 or earlier, should be sized with 1 vCPU and 1GB of memory per 6 concurrent streams, with a minimum of 4vCPUs and a maximum of 32vCPUs.

- CMS 3.1.1 (for streaming service and Callbridge, on separate VMs)

- Vbrick DME 3.15.0 RHEL7

Tip : Cisco recommends if you are running a CMS hosting SIP-based streaming service, running 3.0 or later, the minimum requirements are still 4vCPUs/4GB RAM. However, the number or streams are dependent on the call quality as well. Refer to the chart after this tip for more information.

The information in this document was created from the devices in a specific lab environment. All of the devices used in here started with cleared (default) configurations. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

CMS Version 2.1 and later introduced support for live streaming with the CMS streamer using standard Real-Time Messaging Protocol (RTMP). In CMS 3.1, support for RTMPS was added and thus communcation between the CMS streamer component and external server can be encrypted. This allows for the CMS streamer to integrate with any streaming platform that supports RTMP(S) (Youtube, Facebook, Wowza, and so on). Currently the CMS Streamer has been tested with Vbrick DME as an external streaming server and is the recommended platform for integration.

Live Streaming (Webcast) integration with VBrick DME allow users to watch any live streamed CMS conference anywhere inside the network from different devices. Additionally, when VBrick Rev is used along VBrick DME, this extends this capability for viewing from outside the internal network for every VBrick Rev authorized user.

## Configure

### Network Diagram

There are several scenarios supported to deploy Live Streaming with CMS such as a single Callbridge with multiple streaming servers, a Callbridge cluster with a single streaming server, and a Callbridge cluster with multiple streaming servers. This document uses the most basic deployment with a single Callbridge connecting to a single streaming server. All the configuration steps with this scenario apply to the other scenarios too.

CMS 2.9 or Earlier (XMPP-Based)

Server A: CMS server with Callbridge and XMPP configured

Server B: CMS server that will act as the XMPP Streamer client

CMS 3.0 or Later (SIP-based)

Server A: CMS server with Callbridge

Server B: CMS server that acts as SIP-based Streamer

Note : The CMS server(s) hosting the Callbridge service is the location in which the Streaming/Recording License generated for and installed, not the CMS server acting as the Streamer server.

### Configurations

#### Version 2.9 or Earlier XMPP-Based Deployment

In order to begin this configuration, it is assumed that you already have a CMS server with a working Callbridge and XMPP server. This is because the streamer server acts as an XMPP client, so the XMPP server needs to be enabled and completely configured on the CMS hosting the Callbridge. See the Troubleshoot section of this document to find common error messages received when streaming is not working due to XMPP configured incorrectly.

Caution : If the XMPP server is not correctly configured, stream will not work. XMPP needs to be enabled and completely configured, which includes SRV or DNS resource records (RRs).

1. Certificates: As with all other CMS servers, the streamer server needs to have a valid internal CA signed certificate.

1a. Create the files using the pki csr command.

```
streamer.example.com> pki csr streamer CN:streamer.example.com O:ExampleOrg subjectAltName:example.com
```

Note : Streamer does not require any specific parameters for its service certificate.

1b. Retrieve the files using the SSH File Transfer Protocol (SFTP) client.

1c. Sign and issue the certificate with your internal local authority, in this example an AD server.

1d. Upload the signed certificate and the Callbridge trust bundle certificate to the streamer server using SFTP.

Note : The trust for the streamer acts as a while list and thus only validates the actual certificate offered and does not validate based CA. Thus, the certificate added as the trust should either be a certificate file that contains either the Callbridge or Callbridges (using trust bundle method) that will connect to this streamer and does not need to contain the certificate authorities that signed the Callbridge certificates.

2. SSH configuration.

2a. Configure the interface(s) for the streamer to listen, in this case it was configured interface 'a' only to listen on port 8443.

```
streamer.example.com> streamer listen a:8443
```

2b. Define certificates for the streamer server.

```
streamer.example.com> streamer certs streamer.key streamer.crt
```

2c. Trust the Callbridge certificate bundle.

```
streamer.example.com> streamer trust callbridge.crt
```

2d. Verify that the information entered in the previous steps is correct with the streamer command.

```
streamer.example.com> streamer Enabled                 : false Interface whitelist     : a:8443 Key file                : streamer.key Certificate file        : streamer.crt Trust bundle            : callbridge.crt
```

2e. If everything shows correct, you can proceed and enable the streamer with the command streamer enable .

```
streamer.example.com> streamer enable
```

3. DNS A record.

3a. The DNS A record for the streamer needs to resolve to the IP address of the Ethernet interface configured in step 2a.

4. API configuration.

This configuration is performed in the CMS hosting the Callbridge service. In Version 2.9 and later, a built API configuration tool is on the WebAdmin page. You can still use a third-party application (such as POSTman or RESTer) to interface with the CMS API, but this document will reflect use of the Build-In API configurator.

4a. Add the streamer to /streamers, with the HTTPS 'URL' of the streamer server.

Note : You can use the IP address or hostname (if DNS exists) for the streamer interface and must append with the port listening on.

4b. Verify streamer was added by navigating to '/streamers' in the API menu.

4c. Add the VBrick 'streamURL' to the space(s) that will be used for streaming.

In order for a space to invoke streaming, the space MUST HAVE a 'streamURL' associated to the space. The 'streamURL' is unique to a space and can only be set at the space level.

For this example, a space called 'Stream Test' is created.

The 'streamURL' should be configured in this format:

```
rtmp:// <VBrickBroadcastUsername>:<VBrickBroadcastPassword> @< VBrick IP or FQDN> /live/ NameoftheStream
```

Note : The default username and password for VBrick DME Broadcast is: broadcast / broadcast . Go to the Troubleshoot section of this document if you have issues setting up this streamURL.

4d. Verify streamURL was added correctly by navigating to the space in the API menu.

4e. Configure 'streamingMode' in the callProfile and associate to the cospace(s). These are options for this mode:

- Manual: Can manually start or stop streaming and must be started manually during call.

- Automatic: Automatically start streaming at beginning of call when space is joined, can be manually stopped or started throughout.

- Disabled: This disables the ability to stream for where the callProfile is associated.

This example was configured for 'Automatic' in the callProfile:

4f. Verify 'streamingMode' was added correctly by navigating to the callProfile in API menu (/api/v1/callProfiles/<callProfileGUID>).

4g. Verify this callProfile id is set within the API (system profiles or cospace ). If it is not set, streaming will not perform mode action and will not start automatically. In this document, the callProfile was set at the cospace level:

4h. The parameter 'streamingControlAllowed' in the /callLegProfiles/<callLegProfileid> will allow the ability to set users/devices permissions, that join a conference and assigned this callLegProfile, to have control over streaming or not during the call. By default is set to true.

The CallLegProfile can be set at the Cospace, System Profile, AccessMethod, or CospaceUser level.

4i. If the 'manual' option was selected for 'streamingMode' in step 4e and/or you wish to have devices to have the ability to start and stop streaming using associated tones, then dtmfProfiles need to be configured. Go to /dtmfProfiles and use the 'startStreaming' and 'stopStreaming' parameters to define the DTMF tones to start and stop the streaming. In this example, a DTMF tone with these values is created.

4j.  If using the DTMF Profile, this MUST be set at the System Profile level.

#### Version 3.0 or Later SIP-Based Deployment

In order to begin this configuration it is assumed that you already have a CMS server with working Callbridge.

1. Certificates: As with all other CMS servers, the streamer SIP server needs a valid signed certificate (Internal or Public)

1a. Create the certificate request for streamer using the pki csr command.

```
streamer.example.com> pki csr streamer CN:streamer.example.com O:ExampleOrg subjectAltName:example.com
```

1b. Retrieve the files using the SFTP client.

1c. Sign and issue the certificate with your certificiate authority. In this example, an internal Windows AD was used.

1d. Upload the signed certificate and certificate authority bundle to the streamer server using SFTP.

2. SSH Configuration.

2a. Configure the interface for streamer service to listen for SIP connections. This command references the interface and port(s) used for SIP TCP and TLS.

```
streamer sip listen <tcp-port|none> <tls-port|none>
```

You can specify any port for this servcie as long as it does not overlap with other services on the server. The default is 5060(tcp) and 5061(tls).

An example is shown here:

```
streamer.example.com> streamer sip listen a 6000 6001
```

2b. Configure the certificates to be used for the SIP streamer. Specify the key file, certificate, and CA trust bundle.

```
streamer.example.com> streamer sip certs streamer.key streamer.crt CAbundle.cer
```

2c. OPTIONAL: configure the resolution and call limit for the streamer.

```
streamer.example.com> streamer sip resolution <audio|720p|1080p> streamer.example.com> streamer limit <0-500|none>
```

2d. Verify that the information configured is correctly with the streamer command.

```
streamer.example.com> streamer Enabled                 : false SIP interfaces          : tcp a:6000, tls a:6001 SIP key file            : streamer.key SIP certificate file    : streamer.crt SIP CA Bundle file      : CAbundle.cer SIP Resolution          : 1080p SIP traffic trace       : Disabled Call Limit              : 6
```

2e. After validating, enable the SIP streamer service with the streamer enable option:

```
streamer.example.com> streamer enable
```

3. DNS Configuration.

3a. A DNS record can be created to resolve the FQDN/Hostname of the Streamer IP address configured on the Ethernet interface set in step 2a.

3b. If the Vbrick address is set as a hostname in the 'streamURL' (configured later), ensure that the DNS is configured to resolve.

4. API Configuration.

This configuration is performed in the CMS hosting the Callbridge service. Beginning in Version 2.9 and later,  there is a built API configuration tool on the WebAdmin page. You can still use a third-party application (such as POSTman or RESTer) to interface with the CMS API, but this document will reflect use of the built-in API configurator.

4a. Add the Vbrick 'streamURL' to the space(s) that will be used for streamer.

In order for a space to invoke streaming, the space MUST HAVE a 'streamURL' associated to the space. The 'streamURL' is unique to a space and can only be set at the space level.

In this example, a space named 'SIP Stream Test' is created.

In Version 3.1 and later, it is possible to have RTMPS and thus can be prefixed with rtmps:// for the URL. In this example, RTMP is used:

The 'streamURL' should be configured in this format:

```
rtmp:// <VBrickBroadcastUsername>:<VBrickBroadcastPassword> @< VBrick IP or FQDN> /live/ NameoftheStream
```

Note : The default username and password for VBrick DME Broadcast is: broadcast / broadcast . Go to the Troubleshoot section of this document if you have issues setting up this streamURL.

4b. Verify 'streamURL' was added correctly by navigating to the space in the API menu.

4c. Configure 'streamingMode' and 'sipStreamerUrl' in the callProfile and associate to cospace(s). These options are available for 'streamingMode:

- Manual: Can manually start or stop streaming and must be started manually during call.

- Automatic: Automatically start streaming at beginning of call when space is joined, can be manually stopped or started throughout.

- Disabled: This disables the ability to stream for where the callProfile is associated.

This example was configured for 'Automatic' in the callProfile:

Note : The value in the 'sipStreamerURI' does not need to be anything specific to match against the streamer. This URI is used for routing purposes only and should ensure the routing environment is set to send this to the streaming server. This will be addressed later.

4d. Verify 'streamingMode' and 'sipStreamerUri' have been set correctly by navigating to the callProfile in the API menu (/api/v1/callProfiles/<callProfileGUID>).

4e. Verify this callProfile id is set within the API (system profiles or cospace ). If it is not set, streaming will not perform mode action and will not start automatically. In this document, the callProfile was set at the cospace level:

4f. The parameter 'streamingControlAllowed' in the /callLegProfiles/<callLegProfileid> will allow the ability to set users/devices permissions, that join a conference and assigned this callLegProfile, to have control over streaming or not during the call. By default is set to true.

The CallLegProfile can be set at the Cospace, System Profile, AccessMethod, or CospaceUser level.

4g. If the 'manual' option was selected for 'streamingMode' in step 4e and/or you wish to have devices to have the ability to start and stop streaming using associated tones, then dtmfProfiles need to be configured. Go to /dtmfProfiles and use the 'startStreaming' and 'stopStreaming' parameters to define the DTMF tones to start and stop the streaming. In this example, a DTMF tone with these values is created:

4h. If using the DTMF Profile, this MUST be set at the System Profile level:

#### Routing for CMS SIP Streamer

Unlike the Version 2.9 and earlier XMPP streaming client, because this streaming client is SIP-based, it requires there to be Outbound routing from the CMS in order for the call to connect. This routing allows for when Streaming is invoked on the Callbridge (either manually or automatically). It uses the sipStreamerUri and sends a SIP INVITE from the Cospace to the streamer. This means the domain portion or the Streaming URI should be unique to routing for the streamer component. It is also worth mentioning, SIP Contact headers are used to indicate the streaming URL details to the streaming component.

A. Call Flow: The CMS SIP streamer (also SIP recorder) supports two call routing paths (three scenarios in total) from the Callbridge to the streamer:

##### 1. Direct Flow

This is where the call routing to the streamer is routed directly from Callbridge server to the streamer, with NO call control in between:

For the direct flow scenario, navigate to Configuration > Outbound calls in the WebAdmin page of the Callbridge server and add a rule matching these requirements:

a. Domain - this will be the domain associated wit the sipStreamerURI (ex: streamer.com ).

b. SIP Proxy to use - this should be the IP address or FQDN AND the port the service is using (this is required IF the service is using a port other than 5060 or 5061) for the streamer server (for example, streamer.example.com:6000 ).

c. Trunk Type - standard SIP

d. Behavior - continue OR Stop

e. Priority - set pirority for the routing rule (generally if using both TLS and TCP for streamer, the TLS should have higher priority on routing rule)

f. Encryption - set the encryption based on if connecting to TLS or TCP.

Direct Example:

Note : As shown, there are two rules (one for TLS and one for TCP) and the TLS rule is prioritized. However, based on the behavior, it should fall back to the TCP.

##### 2. Call Control Routing (Expressway or CUCM)

This is where the call routing to the streamer is routed through a Call Control (such as Expressway or CUCM) from the Callbridge server:

2a. CMS Outbound routing:

For the call control scenario, navigate to Configuration > Outbound calls in the WebAdmin page of the Callbridge server and add a rule matching the below requirements:

a. Domain - this will be the domain associated wit the sipStreamerURI (for example, streamer.com )

b. SIP Proxy to use - this should be the IP address or FQDN of the call control that the call is being routed through (ex: cucm.example.com )

c. Trunk Type - standard SIP

d. Behavior - continue OR Stop

e. Priority - set pirority for the routing rule (generally if using both TLS and TCP for streamer, the TLS should have higher priority on routing rule)

f. Encryption - set the encryption based on if connecting to TLS or TCP

2b. CUCM Routing: This configuration piece assumes you have a SIP trunk configured between CUCM and CMS CB server as well as CMS streamer.

Note : It should be noted that for the Trunk between the CUCM and CMS Streamer , it should be enabled for Early Offer on the SIP Profile.

Navigate to Call Routing > SIP Route Pattern and create a new Domain Routing for the matching domain and route to the create SIP Trunk for the CMS streamer.

2c. Expressway Routing: This configuraiton pieces assumes you have a Neighbor zone between CMS (or CUCM) and the Streaming CMS server.

Navigate to Configuration > Dial Plan > Search Rules on the Expressway server and create a new rule for the streamer.

For the call control routing, you can use either Expressway or CUCM for routing the call or both. Ensure that the routing rules are configured to route correctly the destination of the CMS streamer.

## Verify

Use this section in order to confirm that your configuration works properly.

1. CMS event log: In the CMS hosting the Callbridge web interface, check that the streaming shows available and streaming, in this example as the streaming is set to automatic, thus when the call is initiated, a guest account is created for the streaming client and it shows that the streaming device is available and currently streaming:

Version 2.9 or Earlier XMPP-based Streamer

```
2021-02-15 13:29:00.714 Info starting automatic streaming (space 'Stream Test')
2021-02-15 13:29:01.953 Info call 2: allocated for guest2686566456@brhuff.local "Streaming client (61b0e8e8-254a-4847-a4d3-ae6382342b9f)" conference participation
2021-02-15 13:29:01.996 Info participant "guest2686566456@brhuff.local" joined space 8ae56cc2-705e-4ad9-b181-072a625cbdd3 (Stream Test)
2021-02-15 13:29:01.996 Info participant "guest2686566456@brhuff.local" (4fed1d6e-67e5-440c-835c-bcc548185904) joined conference 5aabb283-603f-417e-a6a2-56fd98264345 via XMPP
2021-02-15 13:29:05.953 Info streaming device 1: available (1 streamings)
```

Version 3.0 or Later SIP-Based Streamer

```
2021-02-15 13:55:48.784 Info starting automatic streaming (space '3.0 Stream Test Space')
2021-02-15 13:55:48.784 Info API call leg 94ca1e1b-5d4b-4f13-81c0-149b5c604097 in call 3d7086e3-e1f9-426b-b79c-ac78956e1609 (API call 1616db86-452b-428f-9e43-ed45dcdf51d6)
2021-02-15 13:55:48.791 Info call 24: outgoing SIP call to "stream@streamer.com" from space "3.0 Stream Test Space"
2021-02-15 13:55:48.791 Info call 24: configured - API call leg 2a31774f-f12f-4a3d-bc16-82eeb01a6732 with SIP call ID "554f17b5-d562-4c2e-a586-4a2396abcc65"
2021-02-15 13:55:48.793 Info call 24: setting up UDT RTP session for DTLS (combined media and control)
2021-02-15 13:55:48.800 Info conference "3.0 Stream Test Space": unencrypted call legs now present
2021-02-15 13:55:48.801 Info participant "stream@streamer.com" joined space 06a80dbd-66a4-4d08-8e82-e13331ac6dfb (3.0 Stream Test Space)
2021-02-15 13:55:48.801 Info participant "stream@streamer.com" (2a31774f-f12f-4a3d-bc16-82eeb01a6732) joined conference 3d7086e3-e1f9-426b-b79c-ac78956e1609 via SIP
```

2. If using a WebRTC (2.9 or earlier) or WebApp (3.0 or later) , you will see a streaming icon on the left side of the screen. If not using CMA client or WebBridge, proceed to step 3 so you can check it via API.

3. A check against the API for the specified call can indicate if it is currently streaming as well. Navigate to Configuration > API and locate the /calls section. Check the streaming field in the API. As seen here, if the call currently streams it should show a true value:

Tip : If streaming show 'true', but the additional participant is not showing, this is most likely a XMPP issue where the 'streaming' client is having issues to communicate with the XMPP server. See the Troubleshoot section of this document to check the most common XMPP configuration issues.

4. VBrick DME web interface: Navigate to Monitor and Logs > Multi-Protocol Connections and check that you can see the stream in this location as in incoming stream.

5. Play the live stream: Using the information found under Multi-Protocol Connections in the DME web interface it is possible to play the stream using a streaming player like VLC media player ( http://www.videolan.org/vlc/ ) to confirm audio and video are working correctly. Simply copy the rtmp stream and paste into the Open network stream option:

## Troubleshoot

### CMS Version 2.9 or Earlier XMPP Streamer

Syslog Follow Command

Always run the syslog follow command on the streamer server. You should be able to see very important information and error messages that will help you to know where to start your troubleshooting. Here is an example of a succesful stream with no error messages shown:

```
Feb 15 14:27:58.120 daemon.info streamer streamer-proxy[1]: 2021/02/15 19:27:58 TRACE (ALL):r = &{POST /streamings HTTP/1.1 1 1 map[Content-Type:[application/x-www-form-urlencoded] Content-Length:[160] User-Agent:[Acano server] Connection:[close]] 0xc4204655c0 <nil> 160 [] true 14.49.17.7:445 map[] map[] <nil> map[] 14.49.17.237:42812 /streamings 0xc4200a7ef0 <nil> <nil> 0xc420465600} upgrade not found
Feb 15 14:27:58.120 daemon.info streamer streamer-proxy[1]: 2021/02/15 19:27:58 TRACE (ALL):set path to /streamings from /streamings: websocket: false, protected: true
Feb 15 14:27:58.120 daemon.info streamer streamer-proxy[1]: 2021/02/15 19:27:58 INFO (ALL):peer presented certificate in whitelist with serial number 1338044712371352933337304391814440992479641688
Feb 15 14:27:58.120 daemon.info streamer streamer-proxy[1]: 2021/02/15 19:27:58 INFO (ALL):Adding auth header
Feb 15 14:27:58.161 user.info streamer streamer[1]: Start session 50939c65-301c-468e-a54a-b7b2bd06dd50
Feb 15 14:27:58.346 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Start Keepalives
Feb 15 14:27:58.346 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Start send
Feb 15 14:27:58.347 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Bot started
Feb 15 14:27:58.348 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: new status: disconnected
Feb 15 14:27:58.348 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: new status: connecting
Feb 15 14:27:58.348 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Connecting to '172.18.105.43', app 'live', stream 'CMS', port '1935', scheme 'rtmp'
Feb 15 14:27:58.355 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Set sending chunk size to 4096
Feb 15 14:27:58.356 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: new status: disconnected
Feb 15 14:27:58.357 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Starting authmod=adobe
Feb 15 14:27:58.357 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Connecting to '172.18.105.43', app 'live', stream 'CMS', port '1935', scheme 'rtmp'
Feb 15 14:27:58.363 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Set sending chunk size to 4096
Feb 15 14:27:58.365 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Connecting to '172.18.105.43', app 'live', stream 'CMS', port '1935', scheme 'rtmp'
Feb 15 14:27:58.370 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Set sending chunk size to 4096
Feb 15 14:27:58.372 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Server window size now set to 16777216
Feb 15 14:27:58.372 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Set peer bandwidth received (size=2500000, type=2)
Feb 15 14:27:58.372 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Acknowledged window size 2500000
Feb 15 14:27:58.372 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Stream begin 0
Feb 15 14:27:58.372 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: authmod=adobe successful
Feb 15 14:27:58.373 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Ignored command message 'onBWDone' (['onBWDone', 0.0, None, 8192.0])
Feb 15 14:27:58.373 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Ignored unexpected command message (['_result', 2.0, None, None])
Feb 15 14:27:58.373 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Ignored unexpected command message (['_result', 3.0, None, None])
Feb 15 14:27:58.374 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Ignored command message 'onFCPublish' (['onFCPublish', 0.0, None, {'code': 'NetStream.Publish.Start', 'description': 'CMS'}])
Feb 15 14:27:58.374 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Successfully created stream with stream id 1
Feb 15 14:27:58.375 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: new status: streaming
Feb 15 14:27:58.375 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Successfully published stream to RTMP server
Feb 15 14:27:59.238 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Client connected
Feb 15 14:27:59.241 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Call found
Feb 15 14:27:59.454 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Call connected
Feb 15 14:27:59.454 user.info streamer streamer.50939c65-301c-468e-a54a-b7b2bd06dd50[111]: Start monitor
Feb 15 14:27:59.455 user.info streamer streamer[1]: Bot 50939c65-301c-468e-a54a-b7b2bd06dd50 started
```

XMPP Related Issues

XMPP is required to be enabled, working correctly and completely configured in order for streaming to work. This includes having correct SRV records or RRs resolvable by the streaming server. If they are not configured, the 'streaming' client will not be able to connect to stream. You will see the error message in the syslogs of the streaming server.

```
May 23 16:20:19 user.err streamer streamer.af28cb0c-08d3-4692-b9e6  Client connect failed
May 23 16:20:19 user.info streamer streamer.af28cb0c-08d3-4692-b9e6  new status: disconnecting
May 23 16:20:19 user.err streamer streamer[1]:  Bot af28cb0c-08d3-4692-b9e6-36d7b5b7e149 failed: CLIENT_CONNECT_FAILED
```

Solution

1. Enter the dns and dns lookup SRV _xmpp-client._tcp.<domain> commands from the streaming server to verify DNS is configured and if it can locate the SRV for the XMPP client.

2.If it is not resolvable, ensure the correct DNS settings on the server and ensure _xmpp-client SRV exists or create it with the dns add rr command to add a Resouce record for the XMPP SRV and also an A record for the XMPP server.

Other error messages:

1. "streamerUnavailable"

Error message: "Streamer ' streamURL ' unavailable."

Possible causes: Wrong port was set, port duplicated, port blocked. Streamer server down.

Solution: Verify correct port, address and dns is configured on callbirdge, and that is not in use by other service as 'Recording' and that is not being blocked between servers. Restart CMS server hosting the Callbridge.

Screenshots and logs: The web interface will show the message:

CMS Callbridge Webadmin shows error in Fault condition page for connection failure:

CMS API shows connection failure for streamer status:

2. "streamingLimitReached"

Error message: "start streaming failed: streaming limit reached"

Cause: No enough licenses to stream.

Solution: Verify 'streaming' license(s) is/are installed in the CMS hosting the Callbridge and not in the CMS streamer.

### CMS 3.0 or Later SIP Streamer

'Syslog follow' on streaming server:The syslog for the streamer can be used to validate issues occurring real time. Here is an example of a working syslog follow on a streaming server running Version 3.0:

```
// Incoming SIP Invite to CMS Streamer:

Feb 15 20:12:11.628 daemon.info streamer streamer-sip[2209]: 201211.628 : INFO : SIP trace #10<: is incoming connection from 14.49.17.236:57830 to 14.49.17.246:6000
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.630 : INFO : SIP trace #10<: incoming SIP TCP data from 14.49.17.236:57830 to 14.49.17.246:6000, size 1000:
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.630 : INFO : SIP trace #10<: BEGINNING OF MESSAGE
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.630 : INFO : SIP trace #10<: INVITE sip:stream@streamer.com SIP/2.0
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: Via: SIP/2.0/TCP 14.49.17.236:5060;branch=z9hG4bKe1133b8673549b22eec179d4d90cf553
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: Call-ID: 5ee7860f-17c0-46be-a787-30feae921f92
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: CSeq: 999692844 INVITE
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: Max-Forwards: 70
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: Contact: <sip:test4@14.49.17.236;transport=tcp>;audio;video;x-cisco-tip;x-cisco-multiple-screen=3;isFocus;x-cisco-stream="rtmp://broadcast:broadcast@172.18.105.43/live/CMS3"
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: To: <sip:stream@streamer.com>
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: From: "3.0 Stream Test Space" <sip:test4@14.49.17.236>;tag=e13c70d7c8424b7d
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: Allow: INVITE,ACK,CANCEL,OPTIONS,INFO,BYE,UPDATE,REFER,SUBSCRIBE,NOTIFY,MESSAGE
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: Supported: timer,X-cisco-callinfo
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: Session-Expires: 1800
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: Min-SE: 90
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: User-Agent: Acano CallBridge
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: Content-Type: application/sdp
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: Content-Length: 3455
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: v=0
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: o=Acano 0 0 IN IP4 14.49.17.236
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: s=-
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: c=IN IP4 14.49.17.236
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: b=CT:2000
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: t=0 0
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: m=audio 34904 RTP/AVP 108 107 119 96 109 110 9 99 111 100 104 103 0 8 15 102 18 13 118 101
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: b=TIAS:256000
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: a=sendrecv
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: a=rtpmap:108 opus/48000/2
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: a=fmtp:108 useinbandfec=1
Feb 15 20:12:11.631 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: a=rtpmap:107
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: incoming SIP TCP data from 14.49.17.236:57830 to 14.49.17.246:6000, size 1000:
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: MP4A-LATM/90000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: a=fmtp:107 profile-level-id=24;bitrate=64000;object=23
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: a=rtpmap:119 MP4A-LATM/32000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: a=fmtp:119 profile-level-id=30;bitrate=64000;object=2
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: a=rtpmap:96 mpeg4-generic/48000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: a=fmtp:96 profile-level-id=16;streamtype=5;config=B98C00;mode=AAC-hbr
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: a=rtpmap:109 G7221/32000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: a=fmtp:109 bitrate=48000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: a=rtpmap:110 G7221/32000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: a=fmtp:110 bitrate=32000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: a=rtpmap:9 G722/8000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.631 : INFO : SIP trace #10<: a=rtpmap:99 G7221/16000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=fmtp:99 bitrate=32000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:111 G7221/32000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=fmtp:111 bitrate=24000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:100 G7221/16000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=fmtp:100 bitrate=24000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:104 speex/32000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:103 speex/16000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:0 PCMU/8000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:8 PCMA/8000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:15 G728/8000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:102 speex/8000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:18 G729/8000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=fmtp:18 annexb=yes
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:13 CN/8000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:118 CN/16000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:101 telephone-event/8000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=fmtp:101 0-15
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: m=video 34906 RTP/AVP 97 116 96 34 31 100 121
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: b=TIAS:1744000
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=content:main
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=sendrecv
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=sprop-source:1 count=2;policies=cs:1
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=sprop-simul:1 1 *
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtcp-fb:* nack pli
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: incoming SIP TCP data from 14.49.17.236:57830 to 14.49.17.246:6000, size 1000:
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtcp-fb:* ccm fir
Feb 15 20:12:11.632 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtcp-fb:* ccm cisco-scr
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=extmap:1 http://protocols.cisco.com/virtualid
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=extmap:2 http://protocols.cisco.com/framemarking
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:97 H264/90000
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=fmtp:97 profile-level-id=42800d;max-mbps=489600;max-fs=8160;max-cpb=4000;max-dpb=4752;max-br=1453;max-fps=6000
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:116 H264/90000
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=fmtp:116 profile-level-id=42800d;max-mbps=489600;max-fs=8160;max-cpb=4000;max-dpb=4752;max-br=1453;max-fps=6000;packetization-mode=1
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:96 H263-1998/90000
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=fmtp:96 qcif=1;cif=1;cif4=1;custom=1024,768,1;custom=1280,720,1
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:34 H263/90000
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=fmtp:34 qcif=1;cif=1;cif4=1
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:31 H261/90000
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=fmtp:31 qcif=1;cif=1
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:100 VP8/90000
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=fmtp:100 max-fs=8160;max-fr=30
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtcp-fb:100 nack
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=rtpmap:121 x-rtvc1/90000
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.632 : INFO : SIP trace #10<: a=x-caps:121 263:1920:1080:30.0:2000000:1;4389:1280:720:30.0:2000000:1;8455:640:480:30.0:2000000:1;10345:352:288:30.0:2000000:1;12912:176:144:30.0:2000000:1
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=label:11
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: m=video 34908 RTP/AVP 97 116 96 34 100 121
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: b=TIAS:2000000
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=content:slide
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: incoming SIP TCP data from 14.49.17.236:57830 to 14.49.17.246:6000, size 1000:
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: s
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=sendrecv
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=rtcp-fb:* nack pli
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=rtcp-fb:* ccm fir
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=rtpmap:97 H264/90000
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=fmtp:97 profile-level-id=42800d;max-mbps=270000;max-fs=32400;max-cpb=4000;max-dpb=4752;max-br=1666;max-fps=3000
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=rtpmap:116 H264/90000
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=fmtp:116 profile-level-id=42800d;max-mbps=270000;max-fs=32400;max-cpb=4000;max-dpb=4752;max-br=1666;max-fps=3000;packetization-mode=1
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=rtpmap:96 H263-1998/90000
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=fmtp:96 qcif=1;cif=1;cif4=1;custom=1024,768,1;custom=1280,720,1
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=rtpmap:34 H263/90000
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=fmtp:34 qcif=1;cif=1;cif4=1
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=rtpmap:100 VP8/90000
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=fmtp:100 max-fs=8160;max-fr=30
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=rtcp-fb:100 nack
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=rtpmap:121 x-rtvc1/90000
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=x-caps:121 263:1920:1080:30.0:2000000:1;4389:1280:720:30.0:2000000:1;8455:640:480:30.0:2000000:1;10345:352:288:30.0:2000000:1;12912:176:144:30.0:2000000:1
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=label:12
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: m=application 34912 UDP/BFCP *
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: c=IN IP4 14.49.17.236
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=floorctrl:c-only s-only
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=confid:1
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=userid:14
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=floorid:2 mstrm:12
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: m=application 34913 RTP/AVP 100
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=sendrecv
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=rtpmap:100 H224/4800
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: m=application 34
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: incoming SIP TCP data from 14.49.17.236:57830 to 14.49.17.246:6000, size 186:
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: 910 UDP/UDT/IX *
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=setup:actpass
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=ixmap:0 ping
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=ixmap:2 xccp
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: a=fingerprint:sha-256 40:C7:F0:D7:2B:90:A1:A4:C7:28:36:5E:18:F6:1A:FC:C9:44:C2:EF:A2:58:1D:02:1A:68:D7:D5:FC:D2:6B:3A
Feb 15 20:12:11.633 daemon.info streamer streamer-sip[2209]: 201211.633 : INFO : SIP trace #10<: END OF MESSAGE
Feb 15 20:12:11.634 daemon.info streamer streamer-sip[2209]: 201211.634 : INFO : SIP trace #10>: outgoing SIP TCP data to 14.49.17.236:57830 from 14.49.17.246:6000, size 458:
Feb 15 20:12:11.634 daemon.info streamer streamer-sip[2209]: 201211.634 : INFO : SIP trace #10>: BEGINNING OF MESSAGE
Feb 15 20:12:11.634 daemon.info streamer streamer-sip[2209]: 201211.634 : INFO : SIP trace #10>: SIP/2.0 100 Trying
Feb 15 20:12:11.634 daemon.info streamer streamer-sip[2209]: 201211.634 : INFO : SIP trace #10>: Via: SIP/2.0/TCP 14.49.17.236:5060;branch=z9hG4bKe1133b8673549b22eec179d4d90cf553
Feb 15 20:12:11.634 daemon.info streamer streamer-sip[2209]: 201211.634 : INFO : SIP trace #10>: Call-ID: 5ee7860f-17c0-46be-a787-30feae921f92
Feb 15 20:12:11.634 daemon.info streamer streamer-sip[2209]: 201211.634 : INFO : SIP trace #10>: CSeq: 999692844 INVITE
Feb 15 20:12:11.634 daemon.info streamer streamer-sip[2209]: 201211.634 : INFO : SIP trace #10>: Max-Forwards: 70
Feb 15 20:12:11.634 daemon.info streamer streamer-sip[2209]: 201211.634 : INFO : SIP trace #10>: To: <sip:stream@streamer.com>;tag=657916f47da301ac
Feb 15 20:12:11.634 daemon.info streamer streamer-sip[2209]: 201211.634 : INFO : SIP trace #10>: From: "3.0 Stream Test Space" <sip:test4@14.49.17.236>;tag=e13c70d7c8424b7d
Feb 15 20:12:11.634 daemon.info streamer streamer-sip[2209]: 201211.634 : INFO : SIP trace #10>: Allow: INVITE,ACK,CANCEL,OPTIONS,INFO,BYE,UPDATE,REFER,SUBSCRIBE,NOTIFY,MESSAGE
Feb 15 20:12:11.634 daemon.info streamer streamer-sip[2209]: 201211.634 : INFO : SIP trace #10>: Server: Acano CallBridge Streamer
Feb 15 20:12:11.634 daemon.info streamer streamer-sip[2209]: 201211.634 : INFO : SIP trace #10>: Content-Length: 0
Feb 15 20:12:11.634 daemon.info streamer streamer-sip[2209]: 201211.634 : INFO : SIP trace #10>: END OF MESSAGE

// CMS streamer extracting details and parsing SIP headers for RTMP server connection details:

Feb 15 20:12:11.634 daemon.info streamer streamer-sip[2209]: 201211.634 : INFO : newIncomingCall, with session description
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.634 : INFO : call 13: using streamer worker 0
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : [USAGE] : 1 / 6 calls
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : call 13: supplying contact uri
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : call 13: supplying contact uri, "sip:14.49.17.246:6000"
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : call 13: handling new call information
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : call 13: parsing
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : ERROR : call 13: "" scheme not supported
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : ERROR : call 13: failed to parse stream URL:
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : ERROR : call 13: failed to start connection to RTMP server
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : WARNING : call 13: failed to configure stream
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : call 13: retrying (1/3)...
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : call 13: refresh
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : call 13: SipCallState_OutgoingAnswerPending with local 0
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : call 13: answer pending and have local address 14.49.17.246
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : call 13: answering session description offer
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : call 13: refreshing media, session descriptions: local 1 remote 1

// CMS streamer sending 200 OK to finish SIP transcation: 

Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : SIP trace #10>: outgoing SIP TCP data to 14.49.17.236:57830 from 14.49.17.246:6000, size 1300:
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : SIP trace #10>: BEGINNING OF MESSAGE
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : SIP trace #10>: SIP/2.0 200 OK
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : SIP trace #10>: Via: SIP/2.0/TCP 14.49.17.236:5060;branch=z9hG4bKe1133b8673549b22eec179d4d90cf553
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : SIP trace #10>: Call-ID: 5ee7860f-17c0-46be-a787-30feae921f92
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : SIP trace #10>: CSeq: 999692844 INVITE
Feb 15 20:12:11.635 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : SIP trace #10>: Max-Forwards: 70
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.635 : INFO : SIP trace #10>: Server: Acano CallBridge Streamer
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: Contact: <sip:14.49.17.246:6000;transport=tcp>
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: To: <sip:stream@streamer.com>;tag=657916f47da301ac
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: From: "3.0 Stream Test Space" <sip:test4@14.49.17.236>;tag=e13c70d7c8424b7d
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: Allow: INVITE,ACK,CANCEL,OPTIONS,INFO,BYE,UPDATE,REFER,SUBSCRIBE,NOTIFY,MESSAGE
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: Supported: timer,X-cisco-callinfo
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: Require: timer
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: Session-Expires: 1800;refresher=uas
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: Min-SE: 90
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: Content-Type: application/sdp
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: Content-Length: 665
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: v=0
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: o=Kokoro 0 0 IN IP4 14.49.17.246
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: s=-
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: c=IN IP4 14.49.17.246
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: b=CT:3500
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: t=0 0
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: m=audio 51264 RTP/AVP 119
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: b=TIAS:64000
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: a=recvonly
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: a=rtpmap:119 MP4A-LATM/32000
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: a=fmtp:119 profile-level-id=30;bitrate=64000;object=2
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: m=video 51266 RTP/AVP 116
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: b=TIAS:3500000
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: a=content:main
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: a=recvonly
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: a=rtcp-fb:* nack pli
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: a=rtcp-fb:* ccm fir
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: a=rtpmap:116 H264/90000
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: a=fmtp:116 profile-level-id=428014;max-mbps=248280;max-fs=8276;max-cpb=4000;max-dpb=4752;max-br=2916;max-fps=33;packetization-mode=1
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: a=label:11
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: m=video 0 RTP/AVP 97
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: a=rtpmap:97 H264/90000
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: m=application 0 UDP/BFCP *
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: m=application 0 RTP/AVP 100
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: a=rtpmap:100 H224/4800
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: m=application 0 UDP/UDT/IX *
Feb 15 20:12:11.636 daemon.info streamer streamer-sip[2209]: 201211.636 : INFO : SIP trace #10>: END OF MESSAGE
Feb 15 20:12:11.638 daemon.info streamer streamer-sip[2209]: 201211.638 : INFO : SIP trace #10<: incoming SIP TCP data from 14.49.17.236:57830 to 14.49.17.246:6000, size 398:
Feb 15 20:12:11.638 daemon.info streamer streamer-sip[2209]: 201211.638 : INFO : SIP trace #10<: BEGINNING OF MESSAGE
Feb 15 20:12:11.638 daemon.info streamer streamer-sip[2209]: 201211.638 : INFO : SIP trace #10<: ACK sip:14.49.17.246:6000;transport=tcp SIP/2.0
Feb 15 20:12:11.638 daemon.info streamer streamer-sip[2209]: 201211.638 : INFO : SIP trace #10<: Via: SIP/2.0/TCP 14.49.17.236:5060;branch=z9hG4bKa639567f534a668ab614137698e95db8
Feb 15 20:12:11.638 daemon.info streamer streamer-sip[2209]: 201211.638 : INFO : SIP trace #10<: Call-ID: 5ee7860f-17c0-46be-a787-30feae921f92
Feb 15 20:12:11.638 daemon.info streamer streamer-sip[2209]: 201211.638 : INFO : SIP trace #10<: CSeq: 999692844 ACK
Feb 15 20:12:11.638 daemon.info streamer streamer-sip[2209]: 201211.638 : INFO : SIP trace #10<: To: <sip:stream@streamer.com>;tag=657916f47da301ac
Feb 15 20:12:11.638 daemon.info streamer streamer-sip[2209]: 201211.638 : INFO : SIP trace #10<: From: "3.0 Stream Test Space" <sip:test4@14.49.17.236>;tag=e13c70d7c8424b7d
Feb 15 20:12:11.638 daemon.info streamer streamer-sip[2209]: 201211.638 : INFO : SIP trace #10<: Max-Forwards: 70
Feb 15 20:12:11.638 daemon.info streamer streamer-sip[2209]: 201211.638 : INFO : SIP trace #10<: User-Agent: Acano CallBridge
Feb 15 20:12:11.638 daemon.info streamer streamer-sip[2209]: 201211.638 : INFO : SIP trace #10<: Content-Length: 0
Feb 15 20:12:11.638 daemon.info streamer streamer-sip[2209]: 201211.638 : INFO : call 13: rtcpSessionApplicationPacketReceived (28)
Feb 15 20:12:11.638 daemon.info streamer streamer-sip[2209]: 201211.638 : INFO : SIP trace #10<: END OF MESSAGE
Feb 15 20:12:11.638 daemon.info streamer streamer-sip[2209]: 201211.638 : INFO : call 13: handling sip accepted notification
Feb 15 20:12:11.638 daemon.info streamer streamer-sip[2209]: 201211.638 : INFO : call 13: refresh
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.678 : INFO : SIP trace #10<: incoming SIP TCP data from 14.49.17.236:57830 to 14.49.17.246:6000, size 814:
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10<: BEGINNING OF MESSAGE
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10<: UPDATE sip:14.49.17.246:6000;transport=tcp SIP/2.0
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10<: Via: SIP/2.0/TCP 14.49.17.236:5060;branch=z9hG4bK24cbe73118ff6b015d9e4f90c3606c37
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10<: Call-ID: 5ee7860f-17c0-46be-a787-30feae921f92
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10<: CSeq: 999692845 UPDATE
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10<: Contact: <sip:test4@14.49.17.236;transport=tcp>;audio;video;x-cisco-tip;x-cisco-multiple-screen=3;isFocus;x-cisco-stream="rtmp://broadcast:broadcast@172.18.105.43/live/CMS3"
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10<: To: <sip:stream@streamer.com>;tag=657916f47da301ac
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10<: From: "3.0 Stream Test Space" <sip:test4@14.49.17.236>;tag=e13c70d7c8424b7d
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10<: Max-Forwards: 70
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10<: Allow: INVITE,ACK,CANCEL,OPTIONS,INFO,BYE,UPDATE,REFER,SUBSCRIBE,NOTIFY,MESSAGE
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10<: Supported: timer,X-cisco-callinfo
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10<: Session-Expires: 1800;refresher=uas
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10<: Call-Info: <urn:X-cisco-remotecc:callinfo>;security=NotAuthenticated
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10<: Min-SE: 90
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10<: User-Agent: Acano CallBridge
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10<: Content-Length: 0
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10<: END OF MESSAGE
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10>: outgoing SIP TCP data to 14.49.17.236:57830 from 14.49.17.246:6000, size 602:
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10>: BEGINNING OF MESSAGE
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10>: SIP/2.0 200 OK
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10>: Via: SIP/2.0/TCP 14.49.17.236:5060;branch=z9hG4bK24cbe73118ff6b015d9e4f90c3606c37
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10>: Call-ID: 5ee7860f-17c0-46be-a787-30feae921f92
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10>: CSeq: 999692845 UPDATE
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10>: Max-Forwards: 70
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10>: Server: Acano CallBridge Streamer
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10>: Contact: <sip:14.49.17.246:6000;transport=tcp>
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10>: To: <sip:stream@streamer.com>;tag=657916f47da301ac
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10>: From: "3.0 Stream Test Space" <sip:test4@14.49.17.236>;tag=e13c70d7c8424b7d
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10>: Allow: INVITE,ACK,CANCEL,OPTIONS,INFO,BYE,UPDATE,REFER,SUBSCRIBE,NOTIFY,MESSAGE
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10>: Supported: timer,X-cisco-callinfo
Feb 15 20:12:11.679 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10>: Require: timer
Feb 15 20:12:11.680 daemon.info streamer streamer-sip[2209]: 201211.679 : INFO : SIP trace #10>: Session-Expires: 1800;refresher=uas
Feb 15 20:12:11.680 daemon.info streamer streamer-sip[2209]: 201211.680 : INFO : SIP trace #10>: Min-SE: 90
Feb 15 20:12:11.680 daemon.info streamer streamer-sip[2209]: 201211.680 : INFO : SIP trace #10>: Content-Length: 0
Feb 15 20:12:11.680 daemon.info streamer streamer-sip[2209]: 201211.680 : INFO : SIP trace #10>: END OF MESSAGE

// CMS Streamer continuing to parse SIP header details and locates the stream details from the header 'x-cisco-stream':

Feb 15 20:12:11.681 daemon.info streamer streamer-sip[2209]: 201211.681 : INFO : call 13: handling new call information
Feb 15 20:12:11.681 daemon.info streamer streamer-sip[2209]: 201211.681 : INFO : call 13: parsing
Feb 15 20:12:11.681 daemon.info streamer streamer-sip[2209]: 201211.681 : ERROR : call 13: "" scheme not supported
Feb 15 20:12:11.681 daemon.info streamer streamer-sip[2209]: 201211.681 : ERROR : call 13: failed to parse stream URL:
Feb 15 20:12:11.681 daemon.info streamer streamer-sip[2209]: 201211.681 : ERROR : call 13: failed to start connection to RTMP server
Feb 15 20:12:11.681 daemon.info streamer streamer-sip[2209]: 201211.681 : WARNING : call 13: failed to configure stream
Feb 15 20:12:11.681 daemon.info streamer streamer-sip[2209]: 201211.681 : INFO : call 13: retrying (2/3)...
Feb 15 20:12:11.681 daemon.info streamer streamer-sip[2209]: 201211.681 : INFO : call 13: refresh
Feb 15 20:12:11.681 daemon.info streamer streamer-sip[2209]: 201211.681 : INFO : call 13: rtcpSessionApplicationPacketReceived (1032)
Feb 15 20:12:12.638 daemon.info streamer streamer-sip[2209]: 201212.638 : INFO : call 13: rtcpSessionApplicationPacketReceived (28)
Feb 15 20:12:12.681 daemon.info streamer streamer-sip[2209]: 201212.681 : INFO : call 13: parsing rtmp://broadcast:broadcast@172.18.105.43/live/CMS3
Feb 15 20:12:12.681 daemon.info streamer streamer-sip[2209]: 201212.681 : INFO : call 13: RTMP stream="CMS3"
Feb 15 20:12:12.681 daemon.info streamer streamer-sip[2209]: 201212.681 : INFO : call 13: RTMP server="rtmp://172.18.105.43:1935/live/CMS3"
Feb 15 20:12:12.681 daemon.info streamer streamer-sip[2209]: 201212.681 : INFO : call 13: new connection required
Feb 15 20:12:12.681 daemon.info streamer streamer-sip[2209]: 201212.681 : INFO : call 13: refresh
Feb 15 20:12:12.681 daemon.info streamer streamer-sip[2209]: 201212.681 : INFO : call 13: refreshing media, session descriptions: local 1 remote 1
Feb 15 20:12:12.682 daemon.info streamer streamer-sip[2209]: 201212.682 : INFO : call 13: rtcpSessionApplicationPacketReceived (1032)
Feb 15 20:12:12.682 daemon.info streamer streamer-sip[2209]: 201212.682 : INFO : call 13: connection 37 - success

// CMS Streamer sends connection to RTMP server and performs RTMP handshake and publishes the stream:

Feb 15 20:12:12.682 daemon.info streamer streamer-sip[2209]: 201212.682 : INFO : call 13: new outgoing TCP connection to 172.18.105.43:1935
Feb 15 20:12:12.682 daemon.info streamer streamer-sip[2209]: 201212.682 : INFO : call 13: sending C0 - len 1
Feb 15 20:12:12.682 daemon.info streamer streamer-sip[2209]: 201212.682 : INFO : call 13: sending C1 - len 1536
Feb 15 20:12:12.685 daemon.info streamer streamer-sip[2209]: 201212.685 : INFO : call 13: ParseState_Handshake_S0_S1_Receive; have 1537
Feb 15 20:12:12.685 daemon.info streamer streamer-sip[2209]: 201212.685 : INFO : call 13: received S0 and S1
Feb 15 20:12:12.685 daemon.info streamer streamer-sip[2209]: 201212.685 : WARNING : call 13: S1 byte 5 (exp: 0x00, rec: 0xf4)
Feb 15 20:12:12.685 daemon.info streamer streamer-sip[2209]: 201212.685 : WARNING : call 13: S1 byte 6 (exp: 0x00, rec: 0xab)
Feb 15 20:12:12.685 daemon.info streamer streamer-sip[2209]: 201212.685 : WARNING : call 13: S1 byte 7 (exp: 0x00, rec: 0xa)
Feb 15 20:12:12.685 daemon.info streamer streamer-sip[2209]: 201212.685 : WARNING : call 13: S1 byte 8 (exp: 0x00, rec: 0xe4)
Feb 15 20:12:12.685 daemon.info streamer streamer-sip[2209]: 201212.685 : INFO : call 13: ParseState_Handshake_S2_Receive; have 1536
Feb 15 20:12:12.685 daemon.info streamer streamer-sip[2209]: 201212.685 : INFO : call 13: received S2
Feb 15 20:12:12.685 daemon.info streamer streamer-sip[2209]: 201212.685 : INFO : call 13: Connected to RTMP server
Feb 15 20:12:12.685 daemon.info streamer streamer-sip[2209]: 201212.685 : INFO : call 13: C2 pending - len 1536
Feb 15 20:12:12.685 daemon.info streamer streamer-sip[2209]: 201212.685 : : call 13: snd: create new chunk stream 2
Feb 15 20:12:12.685 daemon.info streamer streamer-sip[2209]: 201212.685 : : call 13: snd: create new chunk stream 3
Feb 15 20:12:12.685 daemon.info streamer streamer-sip[2209]: 201212.685 : INFO : call 13: RTMP sent chunk size of 4096 and connect message
Feb 15 20:12:12.726 daemon.info streamer streamer-sip[2209]: 201212.726 : INFO : call 13: RTMP Created new Rx stream 3
Feb 15 20:12:12.726 daemon.info streamer streamer-sip[2209]: 201212.726 : INFO : call 13: RTMP Stream 3 didn't receive all data, waiting for next chunk
Feb 15 20:12:12.726 daemon.info streamer streamer-sip[2209]: 201212.726 : INFO : call 13: RTMP Got command message
Feb 15 20:12:12.726 daemon.info streamer streamer-sip[2209]: 201212.726 : INFO : call 13: RTMP Got command message
Feb 15 20:12:12.726 daemon.info streamer streamer-sip[2209]: 201212.726 : ERROR : call 13: connection : far end closed connection 37
Feb 15 20:12:12.726 daemon.info streamer streamer-sip[2209]: 201212.726 : INFO : call 13: new connection required
Feb 15 20:12:12.726 daemon.info streamer streamer-sip[2209]: 201212.726 : INFO : call 13: authenticating (authmod=adobe)
Feb 15 20:12:12.727 daemon.info streamer streamer-sip[2209]: 201212.727 : INFO : call 13: connection 38 - success
Feb 15 20:12:12.727 daemon.info streamer streamer-sip[2209]: 201212.727 : INFO : call 13: new outgoing TCP connection to 172.18.105.43:1935
Feb 15 20:12:12.727 daemon.info streamer streamer-sip[2209]: 201212.727 : INFO : call 13: sending C0 - len 1
Feb 15 20:12:12.727 daemon.info streamer streamer-sip[2209]: 201212.727 : INFO : call 13: sending C1 - len 1536
Feb 15 20:12:12.729 daemon.info streamer streamer-sip[2209]: 201212.729 : INFO : call 13: ParseState_Handshake_S0_S1_Receive; have 1460
Feb 15 20:12:12.729 daemon.info streamer streamer-sip[2209]: 201212.729 : INFO : call 13: ParseState_Handshake_S0_S1_Receive; have 1537
Feb 15 20:12:12.729 daemon.info streamer streamer-sip[2209]: 201212.729 : INFO : call 13: received S0 and S1
Feb 15 20:12:12.729 daemon.info streamer streamer-sip[2209]: 201212.729 : WARNING : call 13: S1 byte 5 (exp: 0x00, rec: 0x17)
Feb 15 20:12:12.729 daemon.info streamer streamer-sip[2209]: 201212.729 : WARNING : call 13: S1 byte 6 (exp: 0x00, rec: 0x8b)
Feb 15 20:12:12.729 daemon.info streamer streamer-sip[2209]: 201212.729 : WARNING : call 13: S1 byte 7 (exp: 0x00, rec: 0x9a)
Feb 15 20:12:12.729 daemon.info streamer streamer-sip[2209]: 201212.729 : WARNING : call 13: S1 byte 8 (exp: 0x00, rec: 0x9a)
Feb 15 20:12:12.729 daemon.info streamer streamer-sip[2209]: 201212.729 : INFO : call 13: ParseState_Handshake_S2_Receive; have 1536
Feb 15 20:12:12.729 daemon.info streamer streamer-sip[2209]: 201212.729 : INFO : call 13: received S2
Feb 15 20:12:12.729 daemon.info streamer streamer-sip[2209]: 201212.729 : INFO : call 13: Connected to RTMP server
Feb 15 20:12:12.730 daemon.info streamer streamer-sip[2209]: 201212.729 : INFO : call 13: C2 pending - len 1536
Feb 15 20:12:12.730 daemon.info streamer streamer-sip[2209]: 201212.730 : : call 13: snd: create new chunk stream 2
Feb 15 20:12:12.730 daemon.info streamer streamer-sip[2209]: 201212.730 : : call 13: snd: create new chunk stream 3
Feb 15 20:12:12.730 daemon.info streamer streamer-sip[2209]: 201212.730 : INFO : call 13: RTMP sent chunk size of 4096 and connect message
Feb 15 20:12:12.771 daemon.info streamer streamer-sip[2209]: 201212.771 : INFO : call 13: RTMP Created new Rx stream 3
Feb 15 20:12:12.771 daemon.info streamer streamer-sip[2209]: 201212.771 : INFO : call 13: RTMP Stream 3 didn't receive all data, waiting for next chunk
Feb 15 20:12:12.771 daemon.info streamer streamer-sip[2209]: 201212.771 : INFO : call 13: RTMP Got command message
Feb 15 20:12:12.771 daemon.info streamer streamer-sip[2209]: 201212.771 : INFO : call 13: RTMP Got command message
Feb 15 20:12:12.771 daemon.info streamer streamer-sip[2209]: 201212.771 : ERROR : call 13: connection : far end closed connection 38
Feb 15 20:12:12.771 daemon.info streamer streamer-sip[2209]: 201212.771 : INFO : call 13: got query string : "reason=needauth&user=broadcast&salt=WvviAT4cmEkeosgbQXFJTodwlqtZjBC5&challenge=KqLT7N==&opaque=KqLT7N=="
Feb 15 20:12:12.771 daemon.info streamer streamer-sip[2209]: 201212.771 : INFO : call 13: new connection required
Feb 15 20:12:12.772 daemon.info streamer streamer-sip[2209]: 201212.772 : INFO : call 13: connection 39 - success
Feb 15 20:12:12.772 daemon.info streamer streamer-sip[2209]: 201212.772 : INFO : call 13: sending C0 - len 1
Feb 15 20:12:12.772 daemon.info streamer streamer-sip[2209]: 201212.772 : INFO : call 13: sending C1 - len 1536
Feb 15 20:12:12.772 daemon.info streamer streamer-sip[2209]: 201212.772 : INFO : call 13: new outgoing TCP connection to 172.18.105.43:1935
Feb 15 20:12:12.773 daemon.info streamer streamer-sip[2209]: 201212.773 : INFO : call 13: ParseState_Handshake_S0_S1_Receive; have 1537
Feb 15 20:12:12.773 daemon.info streamer streamer-sip[2209]: 201212.773 : INFO : call 13: received S0 and S1
Feb 15 20:12:12.773 daemon.info streamer streamer-sip[2209]: 201212.773 : WARNING : call 13: S1 byte 5 (exp: 0x00, rec: 0x67)
Feb 15 20:12:12.773 daemon.info streamer streamer-sip[2209]: 201212.773 : WARNING : call 13: S1 byte 6 (exp: 0x00, rec: 0x2a)
Feb 15 20:12:12.773 daemon.info streamer streamer-sip[2209]: 201212.773 : WARNING : call 13: S1 byte 7 (exp: 0x00, rec: 0x52)
Feb 15 20:12:12.773 daemon.info streamer streamer-sip[2209]: 201212.773 : WARNING : call 13: S1 byte 8 (exp: 0x00, rec: 0x44)
Feb 15 20:12:12.773 daemon.info streamer streamer-sip[2209]: 201212.773 : INFO : call 13: C2 pending - len 1536
Feb 15 20:12:12.774 daemon.info streamer streamer-sip[2209]: 201212.773 : INFO : call 13: ParseState_Handshake_S2_Receive; have 1536
Feb 15 20:12:12.774 daemon.info streamer streamer-sip[2209]: 201212.773 : INFO : call 13: received S2
Feb 15 20:12:12.774 daemon.info streamer streamer-sip[2209]: 201212.773 : INFO : call 13: Connected to RTMP server
Feb 15 20:12:12.774 daemon.info streamer streamer-sip[2209]: 201212.773 : : call 13: snd: create new chunk stream 2
Feb 15 20:12:12.774 daemon.info streamer streamer-sip[2209]: 201212.774 : : call 13: snd: create new chunk stream 3
Feb 15 20:12:12.774 daemon.info streamer streamer-sip[2209]: 201212.774 : INFO : call 13: RTMP sent chunk size of 4096 and connect message
Feb 15 20:12:12.815 daemon.info streamer streamer-sip[2209]: 201212.815 : INFO : call 13: RTMP Created new Rx stream 2
Feb 15 20:12:12.815 daemon.info streamer streamer-sip[2209]: 201212.815 : INFO : call 13: RTCP rec window size is now set to 16777216 (was 4294967295)
Feb 15 20:12:12.815 daemon.info streamer streamer-sip[2209]: 201212.815 : INFO : call 13: RTMP Tx Bandwidth received of 2500000 type dynamic (2)
Feb 15 20:12:12.815 daemon.info streamer streamer-sip[2209]: 201212.815 : INFO : call 13: RTMP setting send window size is to 2500000 (was 4294967295)
Feb 15 20:12:12.815 daemon.info streamer streamer-sip[2209]: 201212.815 : INFO : call 13: RTMP received Stream begin 0
Feb 15 20:12:12.815 daemon.info streamer streamer-sip[2209]: 201212.815 : INFO : call 13: RTMP Created new Rx stream 3
Feb 15 20:12:12.815 daemon.info streamer streamer-sip[2209]: 201212.815 : INFO : call 13: RTMP Stream 3 didn't receive all data, waiting for next chunk
Feb 15 20:12:12.815 daemon.info streamer streamer-sip[2209]: 201212.815 : INFO : call 13: RTMP Got command message
Feb 15 20:12:12.815 daemon.info streamer streamer-sip[2209]: 201212.815 : INFO : call 13: RTMP sent FCpublish and create stream for CMS3
Feb 15 20:12:12.815 daemon.info streamer streamer-sip[2209]: 201212.815 : INFO : call 13: RTMP Got command message
Feb 15 20:12:12.855 daemon.info streamer streamer-sip[2209]: 201212.855 : INFO : call 13: RTMP Got command message
Feb 15 20:12:12.856 daemon.info streamer streamer-sip[2209]: 201212.855 : INFO : call 13: RTMP Got command message
Feb 15 20:12:12.856 daemon.info streamer streamer-sip[2209]: 201212.855 : INFO : call 13: RTMP Got command message
Feb 15 20:12:12.856 daemon.info streamer streamer-sip[2209]: 201212.855 : INFO : call 13: RTMP Got command message
Feb 15 20:12:12.856 daemon.info streamer streamer-sip[2209]: 201212.855 : INFO : call 13: RTMP Successfully create rtmp stream 1, now sending publish
Feb 15 20:12:12.856 daemon.info streamer streamer-sip[2209]: 201212.856 : : call 13: snd: create new chunk stream 4
Feb 15 20:12:12.857 daemon.info streamer streamer-sip[2209]: 201212.857 : INFO : call 13: RTMP Stream 3 didn't receive all data, waiting for next chunk
Feb 15 20:12:12.857 daemon.info streamer streamer-sip[2209]: 201212.857 : INFO : call 13: RTMP Got command message
Feb 15 20:12:12.857 daemon.info streamer streamer-sip[2209]: 201212.857 : INFO : call 13: RTMP publish successful, can start sending media
```

Call Routing Related Issues

Because the CMS streamer is a SIP-based client and as discussed earlier, it requires routing to be in place. This could cause scenarios where calls might fail. Consider this example, where the CMS Callbridge sent an outbound call, but it failed with the following 'not found' error:

Causes:Routing from CMS Callbridge it sent to another call control that does not have the correct routing setup or is not being routed correctly to streamer server.

Solutions:

1.Review the Outbound calls settings on the CMS Callbridge servers to validate the location it is being sent to and if being set correctly.

2.Review the route rules or route patterns in call control (if any) is correct and targetting the right zone or trunk

3.Ensure the port for the SIp streamer is correct and correctly set through the routing environment.

### General Troubleshooting

Packet Captures

Packet captures from CMS hosting the Callbridge, Streamer and DME will help you in most of the issues related to communication. They will be very important to troubleshoot the error messages:

- Connecting to RTMP server failed (Timeout)"

- "Initiating RTMP protocol failed (connection closed by far end)"

To take packet captures in:

CMS: Use the 'pcap' command and interface you wisht to capture traffic (ex: pcap a).

DME: Use the web interface in the Diagnostics > Trace Capture , press the 'Start capture' button. Press the 'Stop capture' button to stop the tracing. Press the 'Download trace file' to download the packet capture.

streamURL Configuration Issues

One of the most common issue is that the Stream Input Authentication username and/or password is incorrect, thus failing to authenticate to publish the stream. Verify you are using the correct credentials,  Using the VBrick DME web interface, navigate to User Configuration > Stream Input Authentication and check you are using the correct username and password.

Authentication issues against VBrick Stream Input Authentication username and/or password (broadcast user).

1. When using an incomplete format with no user or password, i.e. rtmp://broadcast@10.88.246.108/live/CMSAutomaticStream you will see:

```
May 26 02:08:43 user.info streamer streamer.bd052ae2-6501-4ae4-ab78-5b94c9a21717[305]:  Connecting to '10.88.246.108', app 'live', stream 'CMSAutomaticStream', port '1935', scheme 'rtmp'
May 26 02:08:43 user.info streamer streamer.bd052ae2-6501-4ae4-ab78-5b94c9a21717[305]:  Set sending chunk size to 4096
May 26 02:08:43 user.info streamer streamer.bd052ae2-6501-4ae4-ab78-5b94c9a21717[305]:  Starting authmod=adobe
May 26 02:08:43 user.err streamer streamer.bd052ae2-6501-4ae4-ab78-5b94c9a21717[305]:  No username or password defined for RTMP authentication
```

2. When the user/password are incorrect, rtmp://broadcast:wrongpassword@10.88.246.108/live/CMSAutomaticStream, you will see:

```
May 26 02:05:16 user.info streamer streamer.5fff36f0-e56d-4d02-9e5e-431b0fba130c[284]:  Connecting to '10.88.246.108', app 'live', stream 'CMSAutomaticStream', port '1935', scheme 'rtmp'
May 26 02:05:16 user.info streamer streamer.5fff36f0-e56d-4d02-9e5e-431b0fba130c[284]:  Set sending chunk size to 4096
May 26 02:05:16 user.err streamer streamer.5fff36f0-e56d-4d02-9e5e-431b0fba130c[284]:  RTMP authentication failed (['_error', 1.0, None, {'description': '[ AccessManager.Reject ] : [ authmod=adobe ] : ?reason=authfailed&opaque=vgoAAA==', 'level': 'error', 'code': 'NetConnection.Connect.Rejected'}])
```

Additional streamURL Related Error Messages

- "RTMP stream url has a bad format" - "Connecting to RTMP server failed ([Errno -2] Name or service not known)"

Solutions

- For both error messages, verify that the streamURL follows exactly this format: rtmp://<VBrickBroadcastUsername>:<VBrickBroadcastPassword>@<VBrick IP or FQDN>/live/NameoftheStream/

- Verify that VBrick IP or hostname is resolvable from the streamer server.