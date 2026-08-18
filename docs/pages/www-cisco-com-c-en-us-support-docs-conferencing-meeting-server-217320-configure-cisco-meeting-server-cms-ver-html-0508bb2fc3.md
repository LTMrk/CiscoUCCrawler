---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-217320-configure-cisco-meeting-server-cms-ver-html-0508bb2fc3
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/217320-configure-cisco-meeting-server-cms-ver.html
retrieved_at: 2026-08-18T23:49:36.838573+00:00
---

Configure Cisco Meeting Server (CMS) Version 3 Next Generation Streamer And Uploader

# Configure Cisco Meeting Server (CMS) Version 3 Next Generation Streamer And Uploader

### Download Options

Updated: August 23, 2021

Document ID: 217320

Contents

## Contents

## Introduction

This document describes the steps to configure and troubleshoot Cisco Meeting Server (CMS) integration with Next Generation Streamer and Uploader. The Next Generation Streamer was introduced from CMS version 3.0 and is Session Initiation Protocol(SIP)-Based.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CMS Callbridge(s) Version 3.0 or later with Recording/Streaming license(s). (one recording license will allow one streaming call)

- Vbrick Distributed Media Engine (DME) (used for publishing the live stream from CMS Streaming service)

- Vbrick Rev (optional: only required if Live Streaming need to be shared outside internal network or multicast

- Network File System (NFS) directory is needed, and it can be setup on Windows Server or Linux.

- For Windows server, follow the steps to Deploy Network File system (NFS) on Windows

- For Linux, follow the steps to Deploy Network File system on Linux

### Components Used

The information in this document is based on these software and hardware versions:

- CMS 3.2 and above with 'Recorder' and/or 'Streamer' license(s). (recorder license will also allow you to stream)

- VBrick Distributed Media Engine (DME) 3.15.0 Rhel7

- Vbrick Rev (Uploader is used with vBrick Rev server. No manual importing of recordings is required)

- Windows Server 2012 R2 with NFS

## Background Information

CMS Version 2.1 and later introduced support for live streaming with the CMS streamer using standard Real-Time Messaging Protocol (RTMP). In CMS 3.0, the Next Generation Streamer was introduced which is a SIP-based component. Prior version than 3.0 used Extensible Messaging and Presence Protocol (XMPP) . CMS version 3.1 and above support RTMPS protocol and thus communcation between the CMS streamer component and external server can be encrypted. This allows for the CMS streamer to integrate with any streaming platform that supports RTMP(S) (Youtube, Facebook, Wowza, and so on). Currently the CMS Streamer has been tested with Vbrick DME as an external streaming server and is the recommended platform for integration.

Live Streaming (Webcast) integration with VBrick DME allow users to watch any live streamed CMS conference anywhere inside the network from different devices. Additionally, when VBrick Rev is used along VBrick DME, this extends this capability for viewing from outside the internal network for every VBrick Rev authorized user.Also, CMS Uploader component simplifies the work flow for uploading Meeting Server recordings to the video content manager, Vbrick, from a configured NFS connected to a Meeting Server. No manual importing of recordings is required. Once the Uploader component is configured and enabled, recordings are pushed from the NFS to Vbrick.

Streamer

The information in this document was created from the devices in a specific lab environment. All of the devices used in here started with cleared (default) configurations. If your network is live, make sure that you understand the potential impact of any command.

Uploader

The Uploader component can be installed on the same server as the Recorder component, or on a separate server. If installed on the same server as the Recorder, then add a couple of vCPUs for it to use. If run on a different server, then use the same server specification as for the Recorder: dedicated VM with a minimum of 4 physical cores and 4GB of RAM.

The Meeting Server running the Uploader will require  Read and Write permissions for the Network File Sharing (NFS). The Uploader must run on a different Meeting Server and not on Call Bridge hosting the conferences.

## Configure

### Network Diagram

There are several scenarios supported to deploy Streamer and Uploader with CMS such as: single callbridge with multiple streaming servers, a callbridge cluster with a single streaming server and callbridge cluster with multiple streaming servers. This document is based on a basic deployment with a cluster of callbridge connecting to a single streamer, Uploader server as all the configuration steps with this scenario apply to other scenarios as well.

As shown in the above image

CMS CallBridge Cluster

CMS Streamer/Recorder

CMS Uploader

VBrick DME For Streaming

VBrick Rev For Streaming

### Configurations

Streamer

It is assumed that the callbridge is already setup and accepting calls.

Step 1. Certificates

The new streamer components do not require to listen https connections, however, it listen to SIP connections , the streamer server must have a valid certificate for TLS communication.

```
streamer> pki csr tac CN:.*.tptac9.com subjectAltName:streamer.tptac9.com
..............
......
Created key file tac.key and CSR tac.csr
CSR file tac.csr ready for download via SFTP
```

Get the certificate signed from local Certificate Authority (CA). Upload the generate certificate using Secure File Transfer Protocol (SFTP) to the Streamer server. Checked to confirm the certificates uploaded successfully.

In this document wildcard certificates are used for streamer. Please use the certificate guide for reference.

https://www.cisco.com/c/dam/en/us/td/docs/conferencing/ciscoMeetingServer/Deployment_Guide/Version-3-1/Certificate-Guidelines-for-all-Deployments-3-1.pdf

```
streamer> pki list
User supplied certificates and keys:
tac.key
tac.cer
ROOTCA.cer
example.key
example.csr
tac.csr
```

Step 2. MMP/SSH Configuration

- Configure the listening interface of the streamer and the SIP TCP and TLS ports to listen on using the MMP command

streamer sip listen <interface> <tcp-port|none> <tls-port|none>

streamer> streamer sip listen a 7000 7001

To use only TLS sip connection. Configure TCP sip connection as "none" the command is below

streamer> streamer sip listen a none 7001

- Apply certificates for the streamer server streamer> streamer sip certs tac.key tac.cer

- Select the quality for streaming

streamer> streamer sip resolution 720p

- Enable streamer

streamer> streamer enable

- Optionally, if TLS is configured, you can perform TLS verification for SIP on the streamer

streamer> tls sip trust ROOTCA.cer

Note : For the TLS connection to be secure we recommend enabling TLS verification. streamer> tls sip verify enable

- Verfiy the configuration information entered above is correct

```
streamer> streamer
Enabled                 : false
SIP interfaces          : tcp a:7000, tls a:7001
SIP key file            : tac.key
SIP certificate file    : tac.cer
SIP CA Bundle file      : none
SIP Resolution          : 720p
SIP traffic trace       : Disabled
Call Limit              : none
```

- Enable the streamer by using command: " streamer enable ". All message must show "SUCCESS" as below

```
streamer> streamer enable
SUCCESS: Key and certificate pair match
SUCCESS: Streamer enabled
```

Step 3. API configuration

This configuration is performed in the CMS hosting CallBridge. Below, API on Webadmin interface of CMS. Any REST client like Postman, Poster can also be used to perform this. Once the new SIP streamer is enabled, it can be configured and used in the Call Bridge under /callProfiles for sipStreamerUri.

To use API on CMS server. Go To  Webadmin > Configuration > API

- Create Call Profile

- Configure sipStreamuri=demo@streamer.com & StreamingMode= Automatic/Manual

```
The user part of the configured "sipStreamuri" (i.e. the part before '@' symbol) has no significant meaning, and for the new SIP streamer component, although required, it can usually be anything, e.g. "streamer@streamer.com".The important part of the URI is the "domain" part.
```

Configure sipStreamuri=demo@streamer.com & StreamingMode= Automatic/Manual

- Add the created streamer callProfile above to the /system/profiles. This is a global configuration and the configured "sipStreamerUri" will be used for streamer operation.

Add the callProfile to system/profiles

- Add the VBrick 'streamURL' to the space(s) used for streaming. For reference, a space called 'Stream' was created using the CMS web interface

Space used for Streaming

- Modify the space to add “StreamURL”. The 'streamURL' in the following format: rtmp://<VBrickBroadcastUsername>:<VBrickBroadcastPassword>@<VBrick IP or FQDN>/live/NameoftheStream . In example I configured it as “rtmp://broadcast:broadcast@10.106.81.40/live/SpaceStream77”

Step 4. Create "Outbound Rules"

Configure, a custom URI that maps to an outboundDialPlan rule (the domain can be anything for example "streamer.com"). Please configure an outboundDialPlan rule to match the domain used in streamerUri to route.

Create outbound rules

As shown in the above image, for SIP streamer, if default ports for SIP (5060,5061) are not used, then It is mandatory to specify ports in the configuration of the streamer and include the following port number to connect to the " sip proxy to use " field when outboundDialPlanRule is configured for the service.

```
streamer> streamer
Enabled                 : true
SIP interfaces          : tcp a:7000, tls a:7001
SIP key file            : tac.key
SIP certificate file    : tac.cer
SIP CA Bundle file      : none
SIP Resolution          : 720p
SIP traffic trace       : Disabled
Call Limit              : none
```

Uploader

- Specify the NFS and directory where recordings will be stored that the Uploader will monitor

streamer> uploader nfs 192.168.15.38:Recording

- Specify the Meeting Server that the Uploader will query for recording information

streamer> uploader cms host join.mextp.local

- Specify the Web Admin port on the Meeting Server running the Call Bridge

streamer> uploader cms port 445

- Specify the user with API access on the Meeting Server running the Call Bridge

streamer> uploader cms user apiadmin streamer> uploader cms password Please enter password:

- Add the certificate bundle from CMS to the Meeting Server trust store Create a certificate bundle (crt-bundle) holding a copy of the Root CA’s certificate and all intermediate certificates in the chain for the Web Admin on the Meeting Server running the Call Bridge. streamer> uploader cms trust ROOTCA.cer

- Configure the Vbrick host and the port to which the Uploader will connect streamer> uploader rev host ciscotac.rev-na.demo.vbrick.com streamer> uploader rev port 443

Note : The port defaults to 443 unless otherwise specified​

- Add a Vbrick Rev user who has API permission to upload video recordings streamer> uploader rev user tacuser streamer> uploader rev password Please enter password:

- Add the certificate bundle to the Vbrick Rev trust store

Create a certificate bundle (crt-bundle) holding a copy of the Root CA’s certificate and all intermediate certificates in the chain for the Vbrick Rev serve streamer> uploader rev trust vbrickbundle.cer

- Check uploader configuration and enable uploader

```
streamer> uploader
Enabled                          : false
NFS hostname                     : 192.168.15.38
NFS directory                    : Recording
CMS host                         : join.mextp.local
CMS port                         : 445
CMS user                         : apiadmin
CMS trust bundle                 : ROOTCA.cer
Vbrick Rev hostname              : ciscotac.rev-na.demo.vbrick.com
Vbrick Rev port                  : 443
Vbrick Rev username              : tacuser
Vbrick Rev trust bundle          : brick.cer
View access                      : Public
cospace_member_access            : edit
recording_owned_by_cospace_owner : false
fallback_owner                   : admin
comments_enabled                 : true
ratings_enabled                  : true
downloads_enabled                : true
active_upon_upload               : true
delete_after_upload              : false
```

If configuration is correct, use " uploader enable " command to enable the Uploader component. All message must show "SUCCESS" as shown below.

```
streamer> uploader enable
SUCCESS: uploader enabled
```

## Verify

Streamer

Streaming working and a sip streaming call connected

Uploader

You can see log for a successful event in syslog follow of uploader.

```
Jun 17 22:24:41.867 user.info cms-02 Uploader[1]: scanning directory: /mnt/recordings/forwardedCalls
Jun 17 22:24:41.867 user.info cms-02 Uploader[1]: scanning directory: /mnt/recordings/spaces
Jun 17 22:24:41.869 user.info cms-02 Uploader[1]: checking the status of /mnt/recordings/spaces/8a7076e2-6db6-47e9-98ee-3bd063e32559/20210618032309+0000_vid-id=c4605aaf-dc49-4cd7-9174-c46185ba1983@vbrick.mp4
Jun 17 22:24:41.870 user.info cms-02 Uploader[1]: Getting from: https://ciscotac.rev-na.demo.vbrick.com:443/api/v1/videos/c4605aaf-dc49-4cd7-9174-c46185ba1983/status
Jun 17 22:24:42.035 user.info cms-02 Uploader[1]: Received vbrick response status code: 200
Jun 17 22:24:42.035 user.info cms-02 Uploader[1]: vbrick response: main.vbrickStatusResp{Status:"Ready"}
Jun 17 22:24:42.035 user.info cms-02 Uploader[1]: file 20210618032309+0000_vid-id=c4605aaf-dc49-4cd7-9174-c46185ba1983@vbrick.mp4 vid c4605aaf-dc49-4cd7-9174-c46185ba1983 status Ready
Jun 17 22:24:42.035 user.info cms-02 Uploader[1]: Getting from: https://ciscotac.rev-na.demo.vbrick.com:443/api/v1/videos/c4605aaf-dc49-4cd7-9174-c46185ba1983/playback-url
Jun 17 22:24:42.200 user.info cms-02 Uploader[1]: Received vbrick response 200
```

## Troubleshooting

Streamer

1. No License

Streamer required "recorder" licnese on the server having callbridge component. If that is not there, or insufficient license is present, then errors as shown below will be seen in Event Logs.

Make sure to add required license. Status of license can be checked CLI using the command "license"

```
cms1> license
Feature: callbridge status: Activated expiry: 2023-Apr-28 (690 days remain)
Feature: turn status: Activated expiry: 2023-Apr-28 (690 days remain)
Feature: webbridge status: Activated expiry: 2023-Apr-28 (690 days remain)
Feature: customizations status: Activated expiry: 2023-Apr-28 (690 days remain)
Feature: local_license_mode status: Activated expiry: 2023-Apr-28 (690 days remain)
Feature: recording status: Activated expiry: 2023-Apr-28 (690 days remain)
Feature: personal status: Activated expiry: 2023-Apr-28 (690 days remain)
Feature: shared status: Activated expiry: 2023-Apr-28 (690 days remain)
```

2.TLS port

• If TLS port configured and no certificates are applied. Configure certs for streamer to use TLS

• If certificate are not available. Configure the TCP port only

```
streamer> streamer sip listen a 7000 7001
streamer> streamer enable
FAILURE: TLS port set but no certificates configured
FAILURE: Streamer configuration not complete
```

Now you have 2 options, either to remove TLS Port, or to add SIP TLS Trust and Streamer Certificate

Cisco recommends to have TLS Port enabled.

3. RTMP Sream not configured correctly

You will see error in logs

```
daemon.info streamer streamer-sip[2280]:  144500.368 : INFO    : call 3: retrieved stream URL from RTCP: "rtmp://broadcast:broadcast@10.106.81.40/test"
daemon.info streamer streamer-sip[2280]:  144500.368 : INFO    : call 3: parsing rtmp://broadcast:broadcast@10.106.81.40/test
daemon.info streamer streamer-sip[2280]:  144500.368 : INFO    : call 3: RTMP stream="test"
daemon.info streamer streamer-sip[2280]:  144500.368 : INFO    : call 3: RTMP server="rtmp://10.106.81.40:1935/test"
daemon.info streamer streamer-sip[2280]:  144500.370 : INFO    : call 3: Connected to RTMP server
daemon.info streamer streamer-sip[2280]:  144500.370 : INFO    : call 3: C2 pending - len 1536
daemon.info streamer streamer-sip[2280]:  144500.370 :         : call 3: snd: create new chunk stream 2
daemon.info streamer streamer-sip[2280]:  144500.370 :         : call 3: snd: create new chunk stream 3
daemon.info streamer streamer-sip[2280]:  144500.370 : INFO    : call 3: RTMP sent chunk size of 4096 and connect message
daemon.info streamer streamer-sip[2280]:  144500.410 : ERROR   : call 3: connection : far end closed connection 5
```

Please check the procedure in streamer configuration and configure RTMP URL correctly in the  format " rtmp://<VBrickBroadcastUsername>:<VBrickBroadcastPassword>@<VBrick IP or FQDN>/live/NameoftheStream"

4.Call Routing Related Issues

Because the CMS streamer is a SIP-based client and as discussed earlier, it requires routing to be in place. This could cause scenarios where calls might fail. Consider this example, where the CMS Callbridge sent an outbound call, but it failed with the following ' transaction timeout - no provisional responses sending INVITE' error

```
2021-06-28  17:37:02.412  Info     user 'guest300535034' starting streaming (space 'test')
2021-06-28  17:37:02.413  Info     API call leg bc0917df-589c-4628-887d-79481d322fed in call 63f0b174-831e-4a12-b4ee-27186d4162af (API call 00286960-9af9-4d5d-9ca7-20dd40425292)
2021-06-28  17:37:02.413  Info     call 44: outgoing SIP call to "demo@streamer.com" from space "test"
2021-06-28  17:37:02.413  Info     call 44: configured - API call leg bc0917df-589c-4628-887d-79481d322fed with SIP call ID "7d37a80e-7996-4e8d-aa87-77c9d4729cec"
2021-06-28  17:37:04.482  Info     call 42: receiver report 1 interval for rx video 0 = 6113ms (period 6108ms) 00000000
2021-06-28  17:37:22.074  Info     call 44: falling back to unencrypted control connection...
2021-06-28  17:37:54.075  Info     call 44: ending; local SIP teardown with reason 7 (transaction timeout - no provisional responses sending INVITE) - not connected after 0:52
2021-06-28  17:37:54.075  Info     call 44: destroying API call leg bc0917df-589c-4628-887d-79481d322fed
2021-06-28  17:37:54.076  Info     streaming call leg for space 'test' disconnected with reason 7 (transaction timeout - no provisional responses sending INVITE)
```

Review the Outbound calls settings on the CMS Callbridge servers to validate the location it is being sent to and if being set correctly. Also check if the callprofile is configured with correct streamer URI and same is associated with Cospace.

Uploader

1. Vbrick detials not correct.

You can see error in Uploader log

```
Jun 27 11:29:27.864 user.info streamer Uploader[1]: Received vbrick response 500
Jun 27 11:29:27.864 user.info streamer Uploader[1]: posting to: https://sales.vbrick.com:443/api/v1/user/login
Jun 27 11:29:47.870 user.info streamer Uploader[1]: Received vbrick response 500
Jun 27 11:29:47.870 user.err streamer Uploader[1]: Failed to initialise Vbrick Client
Jun 27 11:29:47.870 user.err streamer Uploader[1]: vbrick returned status code: 500
```

Make sure to have configured the correct credentials and port for the vbrick server.  Also make sure Uploader should be able to reach CMS callbridge webadmin port.

### Revision History

1.0

23-Aug-2021

Initial Release

### Contributed by Cisco Engineers

Abhishek Pal

Cisco TAC Engineer

Anand Dubey

Cisco TAC Engineer

Dipin Divakaran

Cisco TAC Engineer

### This Document Applies to These Products

- Meeting Server

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 23-Aug-2021 | Initial Release |