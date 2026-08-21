---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-210441-h-323-sip-on-cms-acano-call-bridge-html-64cf49fabb
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/210441-H-323-SIP-on-CMS-Acano-Call-Bridge.html
retrieved_at: 2026-08-21T13:12:56.991402+00:00
---

H.323 SIP on CMS/Acano Call Bridge

# H.323 SIP on CMS/Acano Call Bridge

### Download Options

Updated: April 6, 2017

Document ID: 210441

Contents

## Contents

## Introduction

This document describes how to configure the H.323 Gateway in a Cisco Meeting Server (CMS) or an Acano server deployment. The H.323 Gateway was added in version R1.7 and allows to receive/send H.323 calls.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

### Network Diagram

The Acano solution is very modular, let's discuss two common deployments:

- Single combined server deployment:

- Scalable and resilient deployment:

### Configuration Steps

Step 1. On the Acano server Command line interface (CLI) 1. Secure Shell (SSH) to the MMP with the use of the admin credentials. 2. Configure the interface on which the H.323 Gateway should listen for H.323 calls:

For example, if you chose interface a to be the listening interface, then use this command: h323_gateway h323_interfaces a 3. Configure the interface on which the Gateway listens for incoming SIP calls from the Call Bridge:

Note : The Gateway can listen on the same interface for both SIP and H.323 calls from the Call Bridge.

h323_gateway sip_interfaces a 4. Configure the port for the SIP interface to listen for SIP connections from the Call Bridge, by default the Gateway listens on port 6061: h323_gateway sip_port 6061

Note : If the call bridge and the H.323 Gateway are colocated on the same server, you can change the Gateway's SIP port from 6061 to other values other than 5061.

It is recommend to deploy the H.323 Gateway with a Gatekeeper. This is because the Gatekeeper is responsible for the further call routing as the Gateway is limited in this functionality.

If your deployment doesn't include a Gatekeeper, omit this step. 5. Configure the nexthop of the H.323 Gateway. The nexthop should be the Gatekeeper's (for example, VCS-C) IP address: h323_gateway h323_nexthop <IP_address> 6. Configure the SIP Proxy. The SIP Proxy is the part of the deployment that handles the SIP call leg in the H.323-SIP call. If the Gateway and the SIP Proxy are on the same server, the IP address used must be 127.0.0.1, for example: h323_gateway sip_proxy 127.0.0.1 If not, this should be the IP address of the Call bridge used as the SIP Proxy. h323_gateway sip_proxy <IP_address> 7. Assign the certificate to be used by the H.323 gateway. This is required as the gateway always connects to and accepts connection from the Call bridge securely. For this reason the gateway needs to verify the Call Bridge certificate, so this needs to be in the H.323 Gateway's trust store. "[<cert-bundle>]" in the command allows to add the CB certificate onto the Gateway's trust store. If you have multiple call bridges, this cert-bundle needs to contain the certificates of all the call bridges in the deployment. Use this command to configure the certificates to use: h323_gateway certs <key-file> <crt-file> [<cert-bundle>] 8. The H.323 SIP domain is appended onto outbound interworked calls from the H.323 gateway. If this is not set, the far-end would see the calling SIP URL as the username/DN@IP-address of H.323 gateway.

Set the H.323 SIP domain with this command:

h323_gateway sip_domain <domain>

9. Enable the H.323 Gateway component with this command: h323_gateway enable

Step 2. On the Call Bridge WebUI: 1. Connect to the WebUI of the Call Bridge with the admin credentials. 2. Single combined server deployment: a  Go to Configuration > Outbound  calls b. Configure the destination domain for example h323.vc.alero.local c. Under SIP Proxy to use, set the loopback IP and SIP Port confirgured, for example 127.0.0.1:6061 d. Under Local from domain use the domain of call bridge.

3. Scalable and resilient deployment: a  Go to Configuration > Outbound  calls b. Configure the destination domain for example h323.example.com c. Under SIP Proxy to use, set the IP and SIP Port confirgured, for example 10.48.36.76:6061 d. Under Local from domain use the domain of call bridge

## Call Flow Example

This example details a typical call flow in a Scalable and resilient deployment. The same is true for a Single combined Server deployment, except for the SIP Proxy address being 127.0.0.1.

Call flow details:

- VCS sends H225 Setup to H.323 Gateway:

```
h323_gateway: : rx H225 setup 10.48.36.247:15121->10.48.54.75:1720
```

- H.323 Gateway replies with a call proceeding:

```
h323_gateway:   : tx H225 callProceeding 10.48.54.75:1720->10.48.36.247:15121
```

- Callbridge1 (H323 Gateway) connect securely to callbridge2 (SIP Proxy):

```
acanosrv03 host:server:  INFO : SIP trace: connection 98: is incoming secure connection from 10.48.54.75:45169 to 10.48.54.76:5061
```

- Then sends a delayed offer SIP INVITE over TLS to the SIP Proxy:

```
acanosrv03 host:server:  INFO : SIP trace: connection 98: incoming SIP TLS data from 10.48.54.75:45169, size 547: 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: INVITE sip:joshua@cluster.alero.aca SIP/2.0 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Via: SIP/2.0/TLS 10.48.54.75:45169;branch=z9hG4bK1f974d0a0fe300a22eb9e8488702690b 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Call-ID: 364ac547-7bb3-4073-bb41-00f4bcd018d6 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: CSeq: 1711591119 INVITE 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Max-Forwards: 70 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Contact: <sip:10.48.54.75:6061;transport=tls> 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: To: <sip:joshua@cluster.alero.aca> 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: From: "Chambre 1" <sip:joshua.ex90@10.48.54.75>;tag=7a70e72401001572 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Allow: INVITE,ACK,CANCEL,OPTIONS,INFO,BYE,UPDATE,REFER,SUBSCRIBE,NOTIFY,MESSAGE 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Supported: timer 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Session-Expires: 1800 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: User-Agent: Acano H.323 Gateway 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Content-Length: 0
```

- SIP Proxy sends back 100 Trying:

```
2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: SIP/2.0 100 Trying 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Via: SIP/2.0/TLS 10.48.54.75:45169;branch=z9hG4bK1f974d0a0fe300a22eb9e8488702690b 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Call-ID: 364ac547-7bb3-4073-bb41-00f4bcd018d6 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: CSeq: 1711591119 INVITE 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Max-Forwards: 70 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: To: <sip:joshua@cluster.alero.aca>;tag=dc34d0c04f392db6 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: From: <sip:joshua.ex90@10.48.54.75>;tag=7a70e72401001572 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Allow: INVITE,ACK,CANCEL,OPTIONS,INFO,BYE,UPDATE,REFER,SUBSCRIBE,NOTIFY,MESSAGE 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Server: Acano CallBridge 2016-06-07 03:18:14               User.Info  acanosrv03               Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Content-Length: 0
```

- Then 180 Ringing:

```
acanosrv03 host:server:  INFO : SIP trace: connection 98: outgoing SIP TLS data to 10.48.54.75:45169, size 437: 2016-06-07 03:18:14              User.Info acanosrv03              Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: SIP/2.0 180 Ringing 2016-06-07 03:18:14              User.Info acanosrv03              Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Via: SIP/2.0/TLS 10.48.54.75:45169;branch=z9hG4bK1f974d0a0fe300a22eb9e8488702690b 2016-06-07 03:18:14              User.Info acanosrv03              Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Call-ID: 364ac547-7bb3-4073-bb41-00f4bcd018d6 2016-06-07 03:18:14              User.Info acanosrv03              Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: CSeq: 1711591119 INVITE 2016-06-07 03:18:14              User.Info acanosrv03              Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Max-Forwards: 70 2016-06-07 03:18:14              User.Info acanosrv03              Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: To: <sip:joshua@cluster.alero.aca>;tag=dc34d0c04f392db6 2016-06-07 03:18:14              User.Info acanosrv03              Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: From: <sip:joshua.ex90@10.48.54.75>;tag=7a70e72401001572 2016-06-07 03:18:14              User.Info acanosrv03              Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Allow: INVITE,ACK,CANCEL,OPTIONS,INFO,BYE,UPDATE,REFER,SUBSCRIBE,NOTIFY,MESSAGE 2016-06-07 03:18:14              User.Info acanosrv03              Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Server: Acano CallBridge 2016-06-07 03:18:14              User.Info acanosrv03              Jun  7 10:18:20 acanosrv03 host:server:  INFO : SIP trace: Content-Length: 0
```

- Followed by 200 OK with SDP:

```
2016-06-07 03:18:17               User.Info  acanosrv03               Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: connection 98: outgoing SIP TLS data to 10.48.54.75:45169, size 3235: 2016-06-07 03:18:17               User.Info  acanosrv03               Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: SIP/2.0 200 OK 2016-06-07 03:18:17               User.Info  acanosrv03               Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: Via: SIP/2.0/TLS 10.48.54.75:45169;branch=z9hG4bK1f974d0a0fe300a22eb9e8488702690b 2016-06-07 03:18:17               User.Info  acanosrv03               Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: Call-ID: 364ac547-7bb3-4073-bb41-00f4bcd018d6 2016-06-07 03:18:17               User.Info  acanosrv03               Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: CSeq: 1711591119 INVITE 2016-06-07 03:18:17               User.Info  acanosrv03               Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: Max-Forwards: 70 2016-06-07 03:18:17               User.Info  acanosrv03               Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: Server: Acano CallBridge 2016-06-07 03:18:17               User.Info  acanosrv03               Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: Contact: <sip:10.48.54.76;transport=tls> 2016-06-07 03:18:17               User.Info  acanosrv03               Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: To: "Joshua Alero" <sip:joshua@cluster.alero.aca>;tag=dc34d0c04f392db6 2016-06-07 03:18:17               User.Info  acanosrv03               Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: From: <sip:joshua.ex90@10.48.54.75>;tag=7a70e72401001572 2016-06-07 03:18:17               User.Info  acanosrv03               Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: Allow: INVITE,ACK,CANCEL,OPTIONS,INFO,BYE,UPDATE,REFER,SUBSCRIBE,NOTIFY,MESSAGE 2016-06-07 03:18:17               User.Info  acanosrv03               Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: Supported: timer 2016-06-07 03:18:17               User.Info  acanosrv03               Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: Require: timer 2016-06-07 03:18:17               User.Info  acanosrv03               Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: Session-Expires: 1800;refresher=uas 2016-06-07 03:18:17               User.Info  acanosrv03               Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: Min-SE: 90 2016-06-07 03:18:17               User.Info  acanosrv03               Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: Content-Type: application/sdp 2016-06-07 03:18:17               User.Info  acanosrv03               Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: Content-Length: 2629
```

- H323 Gateway sends Connect to the Gatekeeper:

```
2016-06-07 03:18:17               User.Info  acanosrv02               Jun  7 10:18:24 acanosrv02 h323_gateway:   : tx H225 connect 10.48.54.75:1720->10.48.36.247:15121
```

- H323 Gateway and Gatekeeper, exchanges TCS, MSD messages:

```
2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : tx H245 terminalCapabilitySet 10.48.54.75:44466->10.48.36.247:15123 AnABBgAIgXUAD4AwgAD6AAEAAAEAAAEABAIbAlAIAAiBcQAAAAD+oAgACIFxAAAAAf6QCXz+BmABAAGAEYAAACQwIXAABwAIgXUBAQBAAoACACIAAgBSAAEDAAMAGAAQADMAF4AAASFAJ4AAAiQwEWAABgAHuDUBAEB9AAEAEgACgAADJDARYAAGAAe4NQEAQF3AAQASAAKAAAQgwCeAAAUgQCeAAAYiQCeAAAcMACFgAAcACIFxAAABQE4eBQKR + 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : tx H245 terminalCapabilitySet 10.48.54.75:44466->10.48.36.247:15123 QAKiACsAMgPTAEIAHwDSF3CAAAgMACFgAAcACIFxAAABQE4eBQKRQAKiACsAMgPTAEIAHwDSF3CAAAkJ3AAAQE4dAHBQAQAfiAAAAEAA/wC/AP8Av0AAAT8AswE/ALNAADgBAAIAAIAACgncAABATh0AUEABAIAACwjwAEr/AIABAIAADAwIM0ABgCFgAAcACIFxAAABQE4eBQKRQAKiACsAMgIcAEIAIwDSC7gBIAAGAAiBbwECAQARAYAADQwI + 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : tx H245 terminalCapabilitySet 10.48.54.75:44466->10.48.36.247:15123 M0ABgCFgAAcACIFxAAABQE4eBQKRQAKiACsAMgIcAEIAIwDSC7gBIAAGAAiBbwECAQARAYAADgwIO0ABO4AACE4dAHBQAQAfiAAAAEAA/wC/AP8Av0AAAT8AswE/ALNAADgBAAIAAAEgAAYACIFvAQIBABEBgAAPDAgbQAE7gAAITh0AUEABAAEgAAYACIFvAQIBABEBgAAQgwFAgAARhgkAAAYACIFvAQEAgAEEBgAAAAEAAgADAAQABQAGBAAH + 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : tx H245 terminalCapabilitySet 10.48.54.75:44466->10.48.36.247:15123 AAgACQAKAAsDAAwADQAOAA8AABAAABE= 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : tx H245 masterSlaveDetermination 10.48.54.75:44466->10.48.36.247:15123 AQAygGbMEA== 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : rx H245 terminalCapabilitySet 10.48.36.247:15123->10.48.54.75:44466 AnABBgAIgXUADYA0gAA8AAEAAAEfgAEfhAIbAwgJfAgSFBAIAAiBcQAAAAAQCAAIgXEAAAABB2ADEABAAQABABiAAAAkMCFwAAcACIF1AQEAQAKAAgAiAAIAUgABAwADABgAEAAzABeAAAEkMCFwAAcACIF1AQEAQAIwAgAiAAIAUgABAwADABgAEAAzABeAAAIkMCFwAAcACIF1AQEAQAHgAgAiAAIAUgABAwADABgAEAAzABeAAAMkMCFwAAcA + 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : rx H245 terminalCapabilitySet 10.48.36.247:15123->10.48.54.75:44466 CIF1AQEAQAUAAgAiAAIAUgABAwADABkAEAAzABeAAAQiQBOAAAUhQCeAAAYkMBFgAAYAB7g1AQBAfQABABIAAoAAByQwEWAABgAHuDUBAEBdwAEAEgACgAAIIoATgAAJIsATgAAKJAgBE4AACyBAJ4AADCDAJ4AADwwALWAABwAIgXEAAAFA6IAIApFAAqIAOQAyANgAQgAPAGIAyAByANgA0hdwAKIAEIAAEAncAABATh8AcFABAGOIAAABwABX + 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : rx H245 terminalCapabilitySet 10.48.36.247:15123->10.48.54.75:44466 ADsAVwA7QCBAAK8AdwCvAHdAIEAAnwB3AJ8Ad0AgAADHAJUAxwCVQCAAAP8AvwD/AL9AIAABPwCzAT8As0IgAAB/AEcAfwBHQCAAAP8AjwD/AI9BIABwAQACAACAABEJ3AAAQE4fAHBAAQCAABIIsABK/8AAFAwIP0ABgC1gAAcACIFxAAABQOiACAKRQAKiADkAMgDYAEIADwBiAMgAcgDYANIXcACiABABIAAGAAiBbwECAQARAYAAFQwIf0AB + 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : rx H245 terminalCapabilitySet 10.48.36.247:15123->10.48.54.75:44466 O4AACE4fAHBQAQBjiAAAAcAAVwA7AFcAO0AgQACvAHcArwB3QCBAAJ8AdwCfAHdAIAAAxwCVAMcAlUAgAAD/AL8A/wC/QCAAAT8AswE/ALNCIAAAfwBHAH8AR0AgAAD/AI8A/wCPQSAAcAEAAgAAASAABgAIgW8BAgEAEQGAABYMCBtAATuAAAhOHwBwQAEAASAABgAIgW8BAgEAEQGAABcMCBVAARYASv+AASAABgAIgW8BAgEAEQGAABhIxoAC + 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : rx H245 terminalCapabilitySet 10.48.36.247:15123->10.48.54.75:44466 gIAAGoUBQIAAG4AEgGABAIAAHYYJAAAGAAiBbwEBAIABAwwAAAABAAIAAwAEAAUABgAHAAgACQAKAAsADAMADwAQABEAEgMAFgAXABQAFQAAGA== 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : h323OnReceivedCapabilitySet bw 1999872 enc 0 (3) 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : h323OnReceivedCapabilitySet not ready for olc (3) 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : tx H245 terminalCapabilitySetAck 10.48.54.75:44466->10.48.36.247:15123 IYAB 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : rx H245 terminalCapabilitySetAck 10.48.36.247:15123->10.48.54.75:44466 IYAB 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : rx H245 masterSlaveDetermination 10.48.36.247:15123->10.48.54.75:44466 AQC+gAnFXQ== 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : tx H245 masterSlaveDeterminationAck 10.48.54.75:44466->10.48.36.247:15123 IIA= 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : rx H245 masterSlaveDeterminationAck 10.48.36.247:15123->10.48.54.75:44466 IKA=
```

- To complete the SIP dialog the SIP Proxy, it sends an ACK that contains SDP to the Gateway:

```
2016-06-07 03:18:17              User.Info acanosrv03              Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: connection 98: incoming SIP TLS data from 10.48.54.75:45169, size 1000: 2016-06-07 03:18:17              User.Info acanosrv03              Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: ACK sip:10.48.54.76;transport=tls SIP/2.0 2016-06-07 03:18:17              User.Info acanosrv03              Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: Via: SIP/2.0/TLS 10.48.54.75:45169;branch=z9hG4bKc85679d1b5d9c93d2c36d94209417163 2016-06-07 03:18:17              User.Info acanosrv03              Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: Call-ID: 364ac547-7bb3-4073-bb41-00f4bcd018d6 2016-06-07 03:18:17              User.Info acanosrv03              Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: CSeq: 1711591119 ACK 2016-06-07 03:18:17              User.Info acanosrv03              Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: To: <sip:joshua@cluster.alero.aca>;tag=dc34d0c04f392db6 2016-06-07 03:18:17              User.Info acanosrv03              Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: From: "Chambre 1" <sip:joshua.ex90@10.48.54.75>;tag=7a70e72401001572 2016-06-07 03:18:17              User.Info acanosrv03              Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: Max-Forwards: 70 2016-06-07 03:18:17              User.Info acanosrv03              Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: User-Agent: Acano H.323 Gateway 2016-06-07 03:18:17              User.Info acanosrv03              Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: Content-Type: application/sdp 2016-06-07 03:18:17              User.Info acanosrv03              Jun  7 10:18:22 acanosrv03 host:server:  INFO : SIP trace: Content-Length: 1388
```

- Then OLC/OLCAcks are sent between the Gateway and Gatekeeper, with the H.245 TCP channel established after the connect message:

```
2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : tx H245 OLC-101 10.48.54.75:44466->10.48.36.247:15123 AwAAZAygJ4ALDQABAAowNkvs3QA= 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : rx H245 OLC-1 10.48.36.247:15123->10.48.54.75:44466 AwAAAA4YM3AABwAIgXUBAQBAAoACACIAAgBSAAEGAAMAGAAQADMAFwBgAIYHQQFzGgARAACWAwAAAIAQhEABAAoK9YNC+WAoAxAAQA== 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : tx H245 OLCack-1 10.48.54.75:44466->10.48.36.247:15123 IsAAAAKAE1wAAAowNkvs3AAKMDZL7N0BAQA= 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : rx H245 OLCack-101 10.48.36.247:15123->10.48.54.75:44466 IsAAZAaAFFwAAAoK9YNC+AAKCvWDQvkDAAEA 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : tx H245 OLC-102 10.48.54.75:44466->10.48.36.247:15123 AwAAZQoAKWAABwAIgXEAAAFAw1AHApFAAqIAOQAyANgAQgAPAGIAyAByANgA0hdwgBgNYAIACjA2S+zfAgALUAgACIFxAAAAAMA= 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : tx H245 OLC-103 10.48.54.75:44466->10.48.36.247:15123 AwAAZgoEO0ABgClgAAcACIFxAAABQMNQBwKRQAKiADkAMgDYAEIADwBiAMgAcgDYANIXcAEgAAYACIFvAQIBABEBgBgNYAAACjA2S+zhCgALUAgACIFxAAAAAMQ=
```

- At this point the SIP Proxy (Party 0) sends media to the Gateway:

```
2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : media stream 7F50040213F0 party 0 stream 0 local udp 10.48.54.75 60642 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : media stream 7F50040213F0 party 0 stream 1 local udp 10.48.54.75 60643 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : media stream 7F5004021740 party 0 stream 0 local udp 10.48.54.75 60644 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : media stream 7F5004021740 party 0 stream 1 local udp 10.48.54.75 60645 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : media stream 7F5004021A90 party 0 stream 0 local udp 10.48.54.75 60646 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : media stream 7F5004021A90 party 0 stream 1 local udp 10.48.54.75 60647
```

- And media from the Endpoint (Party 1) to the Gateway:

```
2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : media stream 7F5004021A90 party 1 stream 0 local udp 10.48.54.75 60640 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : media stream 7F50040213F0 party 1 stream 0 local udp 10.48.54.75 60636 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : media stream 7F5004021740 party 1 stream 0 local udp 10.48.54.75 60638
```

- And OLC/OLCAck between the Gateway and the SIP Proxy:

```
2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : h323OpenChannel mt 1 (3) 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : h323OpenChannel mt 0 (3) 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : sipOpenChannelAck mt 1 10.48.54.76 34936 (3) 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : sipOpenChannelAck mt 0 10.48.54.76 34934 (3)
```

- Finally, you see that the media streams between the gateway and the H.323 Endpoint:

```
2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : media stream 7F50040213F0 party 1 dest 10.10.245.131 17144 pt 9 ept 9 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : media stream 7F5004021740 party 1 dest 10.10.245.131 17146 pt 96 ept 97
```

Payload Type (PT).

- And from the Gateway to SIP proxy:

```
2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : media stream 7F5004021740 party 0 dest 10.48.54.76 34936 pt 97 ept 255 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : media stream 7F50040213F0 party 0 dest 10.48.54.76 34934 pt 107 ept 255 2016-06-07 03:18:17              User.Info acanosrv02              Jun  7 10:18:24 acanosrv02 h323_gateway:   : media stream 7F50040213F0 party 0 dest 10.48.54.76 34934 pt 107 ept 255
```

## Verify

Use this section to confirm that your configuration works properly.

Verify the configuration on the CLI with this command:

h323_gateway Example outputs of this command are: a. Single combined server deployment:

b. Scalable and resilient deployment:

## Troubleshoot

This section provides information you can use to troubleshoot your configuration and possible call failures.

1. Logs for the SIP call leg can be collected on the CB used for the SIP Proxy:

a. Connect to the WebAdmin (Web Interface)

b. Go to Logs > Detailed Tracing

c. Enable SIP Traffic tracing for the desired duration:

d. When the call has been reproduced, collect the logs by going to Logs > Event logs and download as text

2. Since there's currently no posibility of changing the H.323 related logging levels and log collection on the Web interface as with SIP, this and log collecting can only be taken via the CLI.

To get H.323 related logs to troubleshoot a failing call, follow these steps:

a. SSH to the CB used as the H.323 gateway server

b. Change the H.323 related logging level with the command h323_ gateway trace_ level <level>

0 - trace off 1 - tracing on 2 - adds memory debug every two minutes 3 - adds dump of H.225/H.245 packets

Note : H.323 traces do not disable automatically as with SIP, because there is no timer on this, so you will need to set this back to 0 to turn these traces off after log collection.

c. Run syslog follow to display the current logs

d. To stop the logging, hit ctrl+C

e. Copy the output to Notepad++ for analysis

### Contributed by Cisco Engineers

Joshua Alero

Cisco TAC Engineer

### This Document Applies to These Products

- Meeting Server