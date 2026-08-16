---
doc_id: www-cisco-com-c-en-us-td-docs-solutions-cvd-collaboration-hybrid-12xy-hybcvd-hms-html-687516e1e1
source_url: https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Collaboration/hybrid/12xy/hybcvd/hms.html
retrieved_at: 2026-08-16T18:26:06.046171+00:00
---

Preferred Architecture for Cisco Webex Hybrid Services, CVD

# Preferred Architecture for Cisco Webex Hybrid Services, CVD

Updated: April 27, 2020

Chapter: Cisco Webex Video Mesh

## Chapter: Cisco Webex Video Mesh

## Cisco Webex Video Mesh

Revised: May 31, 2019

Cisco Webex Video Mesh is a component of Webex Hybrid Services that allows organizations to deploy an instance of Webex media processing on-premises. This means that Webex Teams devices and applications can terminate media on-premises instead of sending all media to the cloud. SIP endpoints registered to Cisco Unified Communications Manager (Unified CM) can also use Video Mesh services when dialing into Webex Meetings.

## Overview

The central component of Cisco Webex Video Mesh is the Video Mesh Node, which can be deployed in clusters (see Figure 4-1 ). The Video Mesh Node is packaged as an OVA file and is installed on a Cisco Unified Computing System (UCS) or specification-based server in the organization’s data center(s). The Video Mesh Node registers to Webex, and all management tasks are performed in the Webex Control Hub. Webex Teams devices and applications can send audio, video, and shared screen content to a Video Mesh Node. Cisco Webex Board traffic is sent to the Webex cloud media services. SIP endpoints registered to Cisco Unified CM can send audio, video, and shared screen content to a Video Mesh Node when joining Webex Meetings. Unified CM SIP endpoints include SIP desktop phones, SIP video endpoints, SIP room systems, and Cisco Jabber running in softphone mode.

Figure 4-1 Cisco Webex Video Mesh High-Level Architecture

### Core Components

The core components for Webex Video Mesh include:

- Cisco Webex Video Mesh Node

- Cisco Webex Control Hub

- Cisco Webex

### Key Benefits

The benefits of Webex Video Mesh include:

- Improved call quality as media stays local, which reduces latency and packet loss

- Reduced consumption of Internet bandwidth

- On-premises deployment simplicity via Webex

### Hardware Requirements

Webex Video Mesh Node software can be downloaded from the Webex Control Hub ( https://admin.webex.com ). The software is packaged as an OVA file that can be installed on VMware ESXi 6 (or later) with VMware vSphere 6 (or later). Table 4-1 lists the supported hardware options.

Table 4-1 Hardware Requirements for Webex Video Mesh Nodes 1

Cisco Meeting Server 1000

72 vCPUs

60 GB main memory

250 GB local hard disk space

Specification-based configuration

46 vCPUs

60 GB main memory

250 GB local hard disk space

2.6 GHz Intel Xeon E5-2600v3 or later processor

1. For additional hardware requirements, refer to the Cisco Webex Video Mesh Data Sheet , available at https://www.cisco.com/c/en/us/solutions/collateral/unified-communications/spark-hybrid-services/datasheet-c78-738153.html .

### Webex Video Mesh Ports and Protocols

The Webex Video Mesh Nodes must be accessible from the corporate network. The nodes also need access to Webex for some services such as signaling and media cascading. Table 4-2 , Table 4-3 , Table 4-4 , and Table 4-5 list the ports that must be open for successful deployment of Webex Video Mesh.

Table 4-2 lists the ports required for management of the Video Mesh Nodes.

Table 4-2 Traffic Signatures for Management of Video Mesh Nodes

Administrator computer

Video Mesh Node

Management device IP address

ANY

TCP

HTTPS

Video Mesh Node

443

Video Mesh Node

Webex cloud media services

Video Mesh Node IP address

ANY

TCP

HTTPS

ANY

443

Video Mesh Node

Webex cloud media services

Video Mesh Node IP address

ANY

UDP

NTP

ANY

123 2

Video Mesh Node

Webex cloud media services

Video Mesh Node IP address

ANY

UDP

DNS

ANY

53 1

Video Mesh Node

Webex cloud media services

Video Mesh Node IP address

ANY

TCP

HTTPS

*.docker.io

*.wbx2.com

*.webex.com

443

Video Mesh Node #1

Video Mesh Node #2

Video Mesh Node #1 IP address

ANY

TCP

HTTPS

Video Mesh Node #2 address

5000

5001

2. UDP ports 53 and 123 are not required if you are using local DNS and NTP resources.

Table 4-3 details the port requirements for cascade signaling from the Video Mesh Nodes to the Webex cloud media services.

Table 4-3 Traffic Signatures for Cascade Signaling to the Webex Cloud Media Services

Video Mesh Node

Webex cloud media services

ANY

ANY

TCP

ANY

444

Table 4-4 details the port requirements for Webex Meetings media traffic.

Table 4-4 Traffic Signatures for Webex Real-Time Media (Egress Direction 3 )

Webex Teams application or endpoint

Webex cloud media services

52000 to 52099

5004

UDP

TCP 5

Audio

Webex Teams application or endpoint

Webex cloud media services

52100 to 52299

5004

UDP

TCP 3

Video

Webex Teams application or endpoint

Video Mesh Node

52000 to 52099

5004

UDP 3

Audio

Webex Teams application or endpoint

Video Mesh Node

52100 to 52299

5004

UDP 3

Video

Video Mesh Node

Webex cloud media services

52500 to 62999

5004

UDP/SRTP 6

Audio

Video Mesh Node

Webex cloud media services

63000 to 65500

5004

UDP/SRTP 4

Video

Video Mesh Node

Video Mesh Node

52500 to 62999

5004

UDP/SRTP 4

Audio

Video Mesh Node

Video Mesh Node

63000 to 65500

5004

UDP/SRTP 4

Video

3. Egress direction is from the endpoint to Webex.

4. As elsewhere in this document, Audio in this table refers to audio streams of voice-only calls, audio streams of video calls, and related RTCP packets; while Video refers to video streams (main video and presentations or content) and related RTCP packets.

5. UDP is preferred for media traffic. However, if the UDP connection fails, Webex Teams applications can fail-over to TCP for media traffic.

6. TCP can also be used for media cascades from Video Mesh Node to Video Mesh Node, and from Video Mesh Node to the Webex cloud media services. However, UDP is preferred, and TCP can affect media quality.

Table 4-5 lists the port range requirements to allow SIP endpoints to use Webex Video Mesh services.

Table 4-5 Port Range Requirements to Allow SIP Endpoints to Use Webex Video Mesh Services

Unified CM SIP signaling to Video Mesh cluster

Unified CM

Video Mesh Node

5060

5060

TCP

SIP endpoint signaling to Video Mesh cluster

SIP Endpoint

Video Mesh Node

5060 to 5062

5060 to 5062

TCP

SIP endpoint media to Video Mesh cluster

SIP Endpoint

Video Mesh Node

ANY

52500 to 62999 for audio

63000 to 65500 for video

UDP

For more information on the ports and protocols required for Webex, refer to the latest version of the following documents:

- Cisco Webex Teams Firewall Traversal whitepaper, available at

https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/cloudCollaboration/spark/whitepapers/cisco-wbxt-firewall-traversal-whitepaper.pdf

- Deployment Guide for Cisco Webex Video Mesh , available at

https://www.cisco.com/c/en/us/support/unified-communications/spark/products-installation-guides-list.html

## Architecture

Before deploying Webex Video Mesh Nodes, consider the following factors:

- Number of Webex Teams endpoints per site

- Number of SIP endpoints registered to Cisco Unified CM per site

- Available Internet edge bandwidth per site

- Corporate network architecture

- Number of local participants (located on the corporate network) and number of remote participants (located on the Internet) in Webex Meetings

- Webex Video Mesh Node hardware requirements

After you have evaluated the above factors for your deployment, identify the locations for installing the Video Mesh clusters. The next step is deployment of the Video Mesh Nodes. The Video Mesh Node software can be downloaded from the Webex Control Hub. Once installed and powered on, the Video Mesh Nodes should be configured with relevant network details such as IP, DNS, and NTP addresses.

After installing the Video Mesh Nodes, the next step is to register them to Webex. Video Mesh Node registration is performed via the Webex Control Hub. Video Mesh Nodes must be assigned to a cluster. A cluster can represent a geographical region for Webex Teams endpoints to use for media termination. The IP address of the installed Video Mesh Node is entered into the Webex Control Hub, which registers the node to Webex. More nodes can be added to the cluster at any time.

### Video Mesh Cluster Discovery for Webex Teams Endpoints

When a Webex Teams endpoint starts up, it registers to Webex. Webex then returns the addresses of cloud media services as well as Video Mesh Node clusters provisioned for that Webex Teams organization. Next the Webex Teams endpoint performs a number of tests to determine where it should send media when in a meeting.

The first test that the Webex Teams endpoint performs is a reachability test to see if it can connect to the cluster(s). If a Video Mesh Node is not reachable, the Webex Teams endpoint will not use it to terminate media when in a meeting. When Webex Teams endpoints are roaming outside of the corporate network, if they are not connected to a VPN, reachability tests to Video Mesh Nodes will fail unless the Video Mesh Nodes are exposed to the Internet (not recommended). In this situation, Webex Teams endpoints will send media to the Webex cloud media services when in a meeting.

The second test that the Webex Teams endpoint performs is a STUN test to determine the round-trip delay time (RTD) between the endpoint and the media node (cloud and hybrid). In most cases, for an on-premises Webex Teams endpoint, a Video Mesh cluster should have a shorter RTD than cloud media services. The Webex Teams endpoint reports the results of the STUN test to Webex. Webex then assigns the Webex Teams endpoint to send media to a node in the cluster with the lowest round-trip delay time.

Webex Teams endpoints perform these tests in the background when one of the following events occurs:

- Webex Teams endpoint startup

- A network change event

- Media service cache expiry

The cache expiry time for media node discovery is 2 hours. When new Video Mesh Nodes are added to a deployment, it may take Webex Teams endpoints up to 2 hours to recognize this event. Restarting a Webex Teams endpoint will force the endpoint to perform connectivity and STUN tests again and to recognize the new Video Mesh Node.

### Deploying Video Mesh Nodes on the Corporate Network

The Video Mesh cluster can be deployed on the corporate network or in the demilitarized zone (DMZ). We recommend deploying the Video Mesh cluster in the corporate network to allow corporate network-based Webex Teams endpoints to discover the cluster and thus save bandwidth at the Internet edge. Roaming Webex Teams endpoints will not discover internally deployed Video Mesh Nodes and will connect to Webex for media services. Deploying Video Mesh Nodes on the corporate network also allows Unified CM to connect over SIP without having to open TCP port 5060 on the DMZ internal firewall.

Deploying the Video Mesh cluster in the DMZ allows roaming Webex Teams endpoints (Webex Teams endpoints that are not connected to the corporate network directly or via VPN) to discover and send media to the Video Mesh cluster instead of sending media directly to the Webex cloud media services. However, a DMZ-based deployment of the Video Mesh cluster is not recommended due to the following reasons:

- The external firewall will need to allow UDP traffic from ANY port to the address of the Video Mesh Nodes via port 5004, so that roaming Webex Teams endpoints can send media to the nodes. This is not a preferred approach.

- DMZ-based deployment can lead to cases where media is sent from the corporate network to a Video Mesh cluster in the DMZ and back to the corporate network. This can happen when two internal Webex Teams endpoints are in a meeting. Both endpoints will send media from the corporate network to the Video Mesh cluster in the DMZ.

### Deploying Video Mesh Clusters in Large Population Centers

Video Mesh clusters should be deployed in sites with large numbers of Webex Teams endpoints. Deploying the Video Mesh Nodes in such sites provides the biggest bandwidth savings, as endpoints will discover and send media to the local Video Mesh cluster instead of media being routed over the WAN to a remote Video Mesh cluster or media being routed to Webex. As a best practice, deploy a small Video Mesh cluster initially. Clusters can be increased in size and number, based on traffic patterns monitored via the Webex Control Hub.

The example scenario in Figure 4-2 shows a large campus site with a large number of Webex Teams devices. The large campus site has direct Internet access (DIA) as well as MPLS WAN connectivity to a branch office. The branch office has a small number of Webex Teams endpoints and has MPLS WAN connectivity to the campus site. The branch office in this case must route traffic destined for the Internet via the MPLS WAN to the campus site’s Internet edge router.

Figure 4-2 Media Paths from Webex Teams Endpoints to Webex

When Webex Teams endpoints in the campus and branch office start up, they register to Webex. This organization does not have any Video Mesh Nodes deployed, so the Webex Teams endpoints will send media directly to Webex when in a meeting. The Webex Teams endpoints in the campus site will route media to Webex via the Internet edge router, while the Webex Teams endpoints in the branch office will route media via the MPLS WAN to the campus site and to Webex via the Internet edge, as illustrated in Figure 4-2 .

As the number Webex Teams endpoints at the campus site increases, bandwidth usage at the Internet edge increases. As the number of Webex Teams endpoints at the branch site increases, bandwidth usage at the WAN edge between the campus and branch site increases, and so does the bandwidth usage at the Internet edge.

If we consider that the average media bandwidth required for a Webex Teams endpoint while in a meeting is 2 Mbps, we can determine the bandwidth required for Webex Meetings in this organization as the sum of the bandwidth usage for all endpoints actively in a meeting:

- Internet edge bandwidth required (Mbps) = (campus(n) + branch(n)) ∗ 2

- WAN edge bandwidth required (Mbps) = branch(n) ∗ 2

Where campus(n) is the number of Webex Teams endpoints actively in a meeting at the campus site, and branch(n) is the number of Webex Teams endpoints actively in a meeting at the branch site.

Typically busy hour call attempts (BHCA) are used to determine the number of concurrent calls required in this type of calculation (that is, the number of campus and branch endpoints actively in a meeting). Without knowledge of the BHCA of the deployed Webex Teams endpoints or the number of maximum concurrent calls during the busy hour, a good starting point is 1 concurrent call for every 4 users. So if there are 100 users, then 25 concurrent calls could be assumed. This number would change based on the type of business and user groups, but 25% is a reasonable initial estimate when the number of concurrent calls is unknown.

Note that Webex Teams endpoints can use more than 2 Mbps of bandwidth when in a meeting. Webex Teams endpoints consistently use 80 kbps to send and receive audio. Video rates can vary greatly depending on a number of factors, including endpoint type, multi-stream capabilities, and negotiated bit rate.

Deploying a Video Mesh cluster in the campus site reduces Internet edge bandwidth requirements for Webex Meetings by keeping the media local.

When Webex Teams endpoints in the campus and branch office start up, they register to Webex. If a Video Mesh cluster is deployed, Webex will provide the Webex Teams endpoints with the addresses of the Webex cloud media services and the Video Mesh cluster.

The Webex Teams endpoints perform a connectivity test to the Video Mesh cluster and the Webex cloud media services. The Video Mesh cluster connectivity test should be successful because the Video Mesh cluster is reachable from anywhere on the corporate network. The connectivity test to the Webex cloud media services should also be successful.

The Webex Teams endpoints then perform a STUN test to calculate round-trip delay (RTD) time to available media node clusters (cloud and Video Mesh). The Webex Teams endpoints at the campus site are located at the same site as the Video Mesh cluster, so the RTD to the Video Mesh cluster should be lower than the RTD to the Webex cloud media services. The Webex Teams endpoints at the branch site route STUN tests via the WAN to the Video Mesh cluster and out the Internet edge to the Webex cloud media services. The RTD to the Video Mesh cluster should be shorter than the RTD to the Webex cloud media services. Based on the results of the STUN tests, the Webex Teams endpoints will send media to the Video Mesh cluster when in a meeting, as illustrated in Figure 4-3 .

Note that the Webex Teams endpoints will perform this action of testing the connectivity and RTD to the clusters each time the endpoint starts up, at a network change, or after the 2-hour cache has expired.

Figure 4-3 Media Paths from Webex Teams Endpoints to the Video Mesh Cluster

Webex Teams endpoints at the campus site will route media to the Video Mesh cluster, while Webex Teams endpoints at the branch site will route media over the WAN to the Video Mesh cluster. Since there are no Webex Teams endpoints roaming outside of the corporate network (Webex Teams endpoints that are not connected to the corporate network directly or via VPN) in this scenario, and there is sufficient meeting capacity in the Video Mesh cluster, Webex media will not traverse the Internet edge, thus saving bandwidth usage to the Internet. WAN edge bandwidth usage will still be based on the number of Webex Teams endpoints in the branch site connected to a Webex meeting. Therefore, as the number of Webex Teams endpoints on the corporate network increases, so does the bandwidth savings to the Internet by deploying Video Mesh Nodes.

### Cascading

The Video Mesh cluster creates a media cascade to the Webex cloud media services if the Webex meeting includes an endpoint that is not using that specific Video Mesh cluster for media termination. This can happen when:

- A Webex Teams endpoint is roaming outside of the corporate network

- The Video Mesh cluster is full

- An endpoint that is not a Webex Teams endpoint is in the meeting (for example, a Webex Meetings application sending media directly to the Webex cloud media services)

When a roaming Webex endpoint starts up, it performs connectivity tests to Video Mesh clusters provisioned in the organization. If the Webex Teams endpoint is outside of the corporate network, connectivity tests will fail and the Webex Teams endpoint will register to the Webex cloud media services for media termination. This scenario assumes that the Webex Teams endpoint is not connected to the corporate network via VPN and that the Video Mesh cluster is deployed on the corporate network and not in the DMZ.

Figure 4-4 depicts an example deployment with four participants attending a Webex meeting. There are three Webex Teams devices on the corporate network, and they have registered with a Video Mesh cluster for media termination. This included one Webex Teams endpoint in the branch office connected via a WAN. There is also one roaming Webex Teams application that has registered to the Webex cloud media services for media termination. When the meeting starts, the Video Mesh cluster creates a media cascade link to the Webex cloud media services.

Figure 4-4 Cisco Video Mesh Cluster Cascading to the Webex Cloud Media Services

The media cascade link created in this scenario carries multiple video streams sent by the three corporate network-based Webex Teams endpoints from the Video Mesh cluster to the Webex cloud media services. Each endpoint can also send multiple streams. The purpose of the multiple streams being sent in the cascade link is to allow the roaming endpoint to receive multiple streams (if capable) and to control the video layout (for example, setting the video layout to show the active speaker main video and up to five picture-in-picture frames, or to show the video layout in equal segments regardless of who is the active speaker).

The Video Mesh cluster can send the video of up to six endpoints per meeting to Webex in the cascade link. Each endpoint may send more than one stream and/or resolution (multistream capabilities).

The example deployment in Figure 4-5 shows a Webex meeting with eight participants. Seven participants are using Webex Teams endpoints that are connected to the corporate network, and one participant is roaming.

Figure 4-5 Webex Video Mesh Cluster Cascading Example

The seven Webex Teams endpoints on the corporate network in Figure 4-5 have registered to the Video Mesh cluster, and the roaming Webex Teams endpoint has registered to the Webex cloud media services. Because there is a roaming participant, the Video Mesh cluster will create a media cascade link to Webex. The cascade link can carry a maximum of six participant’s audio/video streams to Webex. In this scenario there are seven meeting participants sending media to the Video Mesh cluster. The cascade link will carry the last six active speakers' video streams from the Video Mesh cluster to Webex, and it will carry one participant’s video from Webex to the Video Mesh cluster (because there is only one roaming Webex Teams endpoint in this scenario). Note that the cascade link from Webex to the Video Mesh cluster can also carry a maximum of six participant’s video.

The following considerations apply to Video Mesh clusters and cascade links:

- The Video Mesh cluster provides more bandwidth savings at the Internet edge as the number of on-premises participants in a single meeting increases above six.

- Each participant’s device can send multiple streams, depending on the video layout requested by the devices.

- The bandwidth requirement at the WAN edge is not affected by the placement of a Video Mesh cluster in the campus site. Media is still sent and received over the WAN to/from the Video Mesh cluster. In general, WAN bandwidth is more expensive than direct Internet access bandwidth, therefore direct Internet access from the remote sites is preferred for Webex Teams endpoints.

- As the number of concurrent meetings increases, the likelihood is that there will be more cascade links created due to roaming or remote participants. Cascade links can use a large amount of bandwidth in both directions. You should plan for and continuously monitor these bandwidth usage requirements in your organization. Use the Webex Control Hub reporting feature to monitor how Webex Video Mesh services are being used.

If the available Video Mesh clusters in an organization are at full capacity, Webex Teams endpoints will be directed to use Webex cloud media services for media termination. In Figure 4-6 , the Video Mesh cluster is serving a large number of Webex Teams endpoints attending meetings, and it reaches its full capacity. There are two Webex Teams devices on the corporate network in a meeting with each other. Both devices are registered to the Video Mesh cluster for media. A third Webex Teams endpoint on the corporate network joins the meeting. Webex is aware that the available Video Mesh cluster is full, so it directs the third Webex Teams endpoint to register with the Webex cloud media services. The Video Mesh Node creates a cascade link to the Webex cloud media services, and all three participants are now in the meeting.

Figure 4-6 Webex Video Mesh Cluster Cascading Due to Capacity Limit

Webex provides overflow for Webex Teams endpoints that cannot send media to a Video Mesh cluster when it has reached full capacity. The cascade link bridges the Video Mesh cluster to Webex.

Multistream Cascading

The multistream technology applied to Webex Teams endpoints also applies to the cascade link. For example, a Video Mesh Node can send multiple video streams per endpoint inside the cascade link to Webex. For details, see the Multistream Cascading section in the Bandwidth Management chapter.

### Clustering

Video Mesh Nodes should be deployed in clusters. A cluster of nodes provides larger capacity than a single Video Mesh Node. It also provides redundancy in case a single node becomes unavailable for any reason. The Video Mesh Nodes are in an active/active state in a cluster.

When a Webex Teams endpoint discovers a Video Mesh cluster, Webex assigns the endpoint to use a particular node in that cluster. Two Webex Teams endpoints in the same site, attending the same meeting, will typically be assigned to the same Video Mesh Node by Webex. However, Webex Teams endpoints attending the same meeting may be assigned to different nodes in the cluster if one of the nodes becomes full. In that case the meeting will be cascaded across the nodes in the cluster, as illustrated in Figure 4-7 .

Figure 4-7 Webex Video Mesh Cluster Cascading

We recommend deploying the Video Mesh cluster in a single site and not clustered over a WAN. Clustering Video Mesh Nodes over a WAN can lead to inefficient media paths, such as hairpinning of media between data centers, which causes increased bandwidth consumption. Having media cascade to Webex is a more efficient use of bandwidth than having media cascade between nodes located over a WAN, for the following reasons:

- Media hairpinning can be avoided

- WAN edge bandwidth is generally much more expensive than Internet edge bandwidth

Deploying a cluster in a single site avoids the scenario of Video Mesh Nodes cascading over the WAN. For example, Figure 4-8 shows a deployment with two Video Mesh clusters. Cluster A is deployed in Campus A, and Cluster B is deployed in Campus B. A Webex Teams endpoint in Campus A and a Webex Teams endpoint in Campus B join a meeting. The Webex Teams endpoint in Campus A is assigned to a Video Mesh Node in Cluster A (lowest RTD time), and the Webex Teams endpoint in Campus B is assigned to a Video Mesh Node in Cluster B (lowest RTD time). Each Webex Teams endpoint sends media to its assigned node. Because the two assigned Video Mesh Nodes being sent media from the endpoints in the meeting are in different clusters, they each cascade media to Webex. There is no hairpinning of media in this case, and the WAN edge bandwidth is not impacted.

Figure 4-8 Webex Video Mesh Cluster per Site

There is no maximum limit to the number of nodes you can deploy in a Video Mesh cluster. As busy hour calling rates increase, the bandwidth requirements at the Internet edge will increase; and depending on the network architecture, the WAN edge bandwidth requirements might also increase. Adding more nodes to a Video Mesh cluster will increase the cluster capacity.

We do not recommend deploying a Video Mesh cluster in every location. Due to the distributed nature of most meetings, deploying a Video Mesh cluster in every location will not lead to bandwidth savings. Instead, we recommend deploying Video Mesh clusters in locations that host regular localized meetings.

Also, we recommend starting with a small number of Video Mesh Nodes in each cluster, and then growing the clusters over time based on usage monitored and reported in the Webex Control Hub.

The following considerations apply to Video Mesh clusters:

- Extra capacity can be added to the Video Mesh cluster by adding more nodes.

- Adding more nodes to the Video Mesh cluster increases hardware requirements. Hardware costs should be weighed against bandwidth costs when considering whether to add more nodes to the cluster to avoid cascade links due to capacity limitations.

- Cascade links are created for meetings with roaming or remote participants, regardless of cluster capacity.

### Direct Internet Access and Centralized Internet Access

Some organizations deploy their network in such a way that only certain sites have direct Internet access (DIA). In this type of deployment, DIA is usually available at large campus sites only, and the organization’s branch sites are provisioned with connectivity to an MPLS WAN network. Branch site applications that access services on the public Internet will route traffic via the WAN to the closest site with DIA. This can lead to inefficient traffic routes, especially for real-time traffic such as audio and video.

MPLS WAN bandwidth is typically much more expensive than direct Internet bandwidth. Providing direct Internet access to branch offices can help provide the most efficient media paths for Webex Teams endpoints.

For branch sites that do not have a Video Mesh cluster deployed but that do have direct Internet access and WAN connectivity to a campus site, we recommend connecting the branch sites’ Webex Teams endpoints to the Webex cloud media services instead of to a Video Mesh cluster located at the campus site. This means that the branch sites’ Webex Teams devices and applications will route their media traffic via the Internet edge to the Webex cloud media services instead of routing media over the WAN. This can be configured by blocking access to the IP addresses of all Video Mesh Nodes at the WAN edge firewall (but only at branch offices with direct Internet access). When Webex Teams endpoints in the branch office perform connectivity tests to the Video Mesh cluster, connectivity will fail and the endpoints will connect to the Webex cloud media services.

### Deploying Video Mesh Nodes in Sites with Direct Internet Access

Deploy Video Mesh clusters only in sites that have direct Internet access. Video Mesh clusters will often have to cascade media streams to Webex. Cascading media over the MPLS WAN can use large amounts of WAN bandwidth and lead to inefficient media paths.

Deploying a Video Mesh cluster in a branch office that does not have direct Internet access can sometimes provide bandwidth savings if that branch has regular Webex meetings with local Webex Teams endpoints only. However, with this deployment model, WAN bandwidth consumption increases if the Webex meetings include roaming participants. Because most meetings have participants distributed in a number of locations, both on the corporate network and on the public network, we recommend that you do not deploy Video Mesh clusters in sites that do not have direct Internet access.

Deploying Video Mesh clusters in sites with no direct Internet access can lead to various issues such as:

- Cascaded media might be routed over the WAN to a site with direct Internet access.

- Webex Teams endpoints might send media to a remote Video Mesh Node over the WAN instead of using their direct Internet access (not ideal and can use WAN resources inefficiently).

Deploying Video Mesh clusters only in sites that have direct Internet access will ensure that media cascaded links are not sent over the MPLS WAN, as illustrated in Figure 4-9 .

Figure 4-9 Webex Video Mesh Cluster Deployed in a Site with Direct Internet Access

### Deploying Video Mesh Nodes in Sites with HTTP(S) Proxy Servers

Cisco Webex Video Mesh supports transparent inspecting and non-inspecting proxies (see Figure 4-10 ). You can tie these proxies to your Webex Video Mesh deployment so that you can secure and monitor traffic from the enterprise out to the cloud. You can use the Webex Video Mesh administration interface for certificate management and overall connectivity status after you implement the proxy with the nodes.

The following proxy types are supported by Video Mesh:

- Transparent Proxy (non-inspecting) — Video Mesh nodes are not aware that they are going through a proxy and should not require any changes to work with a non-inspecting proxy.

- Transparent Proxy (tunneling or inspecting) — Video Mesh nodes are not aware that they are going through a proxy. No http(s) configuration changes are necessary on Video Mesh; however, the Video Mesh nodes need a root certificate so that they trust the proxy. Inspecting proxies are typically used by IT to enforce policies regarding which websites can be visited and which types of content are not permitted. This type of proxy decrypts all of your http and https traffic.

Figure 4-10 Proxy Support for Video Mesh Nodes

### Deploying Webex Video Mesh for SIP Endpoints

SIP endpoints registered to Cisco Unified CM can send audio, video, and screen share content to a Webex Video Mesh cluster when joining Webex Meetings, provided that the Webex Meetings site is configured to allow Webex Video Mesh.

The following statements describe how Unified CM SIP endpoints can use Webex Video Mesh for Webex Meetings (see Figure 4-11 ).

- A Unified CM SIP trunk can be pointed to nodes in a Video Mesh Cluster.

- A Unified CM SIP trunk to a Video Mesh cluster may be secured with TLS, and SIP endpoint media through the Video Mesh cluster may be encrypted.

- A Unified CM SIP route pattern can route calls based on a specific domain (for example, sitename.webex.com) via the SIP trunk to a node in the Video Mesh cluster.

- The Video Mesh Node will signal to Webex to set up a meeting, and Webex will determine the cluster node where the meeting will be hosted.

- The Video Mesh Node will then signal to Unified CM to indicate which node in the cluster should be used for media.

- The SIP endpoint will send media to the selected node.

The Video Mesh cluster will cascade media to Webex if:

- There is a participant in the meeting using the Webex Meetings App

- There is a participant in the meeting hosted on a different Video Mesh cluster

- There is a participant in the meeting sending media directly to Webex

If there are no nodes available, (for example, the cluster is at capacity), Unified CM can route the call to Webex via Cisco Expressway by using the route list logic of Unified CM in response to a failure message sent by the Video Mesh cluster.

Figure 4-11 SIP Endpoints Sending Media via a Video Mesh Cluster

### Deploying Video Mesh Clusters in Large Population Centers

The best practices for where to deploy Video Mesh clusters for Webex Teams endpoints also apply for Unified CM SIP endpoints. Video Mesh Clusters should be:

- Deployed on the corporate network

- Deployed in high population centers

- Not clustered over a WAN

- Deployed in sites with direct Internet access (DIA)

Analytics should also be monitored continuously to determine if more nodes are required in a particular location. For more details, see the section on Monitoring Analytics .

### SIP Trunk Design

Configure a SIP trunk on Unified CM to point to a Webex Video Mesh cluster to route SIP calls to a Video Mesh Node. The SIP trunk can be pointed to a maximum of 16 Video Mesh Nodes.

The trunk should point to a Video Mesh cluster that will host meetings for endpoints that register to that Unified CM cluster. The closer the endpoints are to the Video Mesh cluster, the more efficient the call flows and bandwidth usage become. For example, endpoints on the same LAN as the Video Mesh cluster will send media directly to the cluster, and thus the media will not traverse a WAN.

We recommend pointing the trunk to Video Mesh Nodes from a single Video Mesh cluster, and pointing the trunk to all nodes within the cluster (16 maximum). Run on all Active Unified CM Nodes should also be enabled on the SIP trunk to ensure efficient traffic signaling in Unified CM. Pointing a SIP trunk to a single cluster will ensure that meetings are hosted on that cluster (unless the cluster reaches capacity). This provides more control and predictability of where meetings will occur and how much bandwidth will be needed. It also allows the administrator to expand the Video Mesh cluster by adding more nodes if more SIP endpoints are configured on the Unified CM cluster.

The Unified CM SIP trunk will determine which node in the Video Mesh cluster is used for call setup. Webex determines which node within that Video Mesh cluster hosts the meeting (that is, the node to which endpoints send media).

The trunk should be configured with the FQDN of all Video Mesh Nodes in the cluster (up to 16 nodes). This will allow for high availability so that if a node becomes unavailable, the call will be set up using a different available node configured in the SIP trunk. The destination port for each Video Mesh Node FQDN should be set to port 5060 (SIP over TCP) or 5061 (SIP over TLS).

For example, Figure 4-12 shows Site A with a Unified CM cluster and a Video Mesh cluster containing 3 nodes. The nodes have FQDNs vmn-1-siteA.ent-pa.com, vmn-2-siteA.ent-pa.com, and vmn-3-siteA.ent-pa.com.

Figure 4-12 SIP Trunk Configured to Point to a Video Mesh Cluster

The SIP trunk in Figure 4-12 should be configured as shown in Table 4-6 to point to the Video Mesh Nodes.

Table 4-6 SIP Trunk Configuration Settings

1

vmn-1-siteA.ent-pa.com

5060 or 5061

2

vmn-2-siteA.ent-pa.com

5060 or 5061

3

vmn-3-siteA.ent-pa.com

5060 or 5061

As more nodes are added to the cluster to provide more capacity, the new nodes should be added to the SIP trunk.

This configuration for Site A ensures that all SIP endpoints registered to the Site A Unified CM cluster will use the Site A Video Mesh cluster for Webex Meetings. Assuming endpoints registering to the Site A Unified CM are geographically nearby, this will provide the best use of bandwidth.

The SIP trunk must have an associated SIP Profile. Most SIP Profile defaults apply; however, ensure that the following items are set:

- Set Early Offer support for voice and video calls to Best Effort (no MTP inserted) .

- Set SIP OPTIONS Ping to enabled .

- Set Allow Presentation Sharing using BFCP to enabled

### Secured SIP Trunk and Media Encryption to Video Mesh Cluster

Video Mesh nodes support SIP trunk TLS and media encryption for SIP endpoints registered to Unified CM. There are a few requirements for this support as well as a few benefits.

Benefits:

- Secured signaling and media encryption end-to-end

- Roster List with Video Mesh cascade links — This feature requires the entire media flow to be encrypted end-to-end.

Requirements:

- Unified CM must be in mixed mode.

- All Video Mesh nodes must be enabled with secured trunks within the organization, and the feature must be enabled on the Control Hub at the organization level.

- If encryption is enabled, it will be required between SIP endpoints and the Video Mesh nodes. This means that SIP endpoints must have a certificate [locally significant certificate (LSC) recommended] and a device security profile with encryption enabled. Endpoints without a certificate and an encryption-enabled security profile will not be able to connect to the Video Mesh nodes.

Additional trunk configuration settings when using SIP over TLS:

- Enable sRTP Allowed

- Calling and Connecting Party Info Format: Deliver URI and DN in connected party, if available.

- Destination Port: 5061

- Video Mesh Trunk Security Profile

Trunk security profile configuration settings when using SIP over TLS:

- Device Security mode: Encrypted

- Incoming and outgoing: TLS

- X.509 Subject Name: Enter the common name of the Video Mesh node certificate

- SIP V.150 Outbound SDP offering filter: Use Default Filter

For more information about SIP Profile and SIP trunking best practices as well as security best practices, refer to the latest version of the Preferred Architecture for Cisco Collaboration Enterprise On-Premises Deployments , available at https://www.cisco.com/go/pa .

### Dial Plan Updates

Unified CM SIP endpoints can use Video Mesh clusters for terminating media for Webex Meetings only. SIP point-to-point calls or SIP calls that are not dialing into a Webex meeting do not use Video Mesh.

SIP endpoints typically dial into a Webex meeting via a SIP URI. The Unified CM dial plan must be modified to route calls as required for Webex Meetings.

Create a SIP route pattern in Unified CM to route calls based on a specific domain pattern via a specific route list and route group configuration. The route group should contain configured SIP trunks and can also be used to provide redundancy.

The SIP route pattern should be configured with the domain name for the Webex site. The domain name is usually in the format of sitename .webex.com. For example, if organization ent-pa.com has been configured with a Webex site of ent-pa.webex.com, then SIP endpoints in this organization will dial host-details@ent-pa.webex.com to join a Webex meeting. For this example, the SIP route pattern should be configured as shown in Table 4-7 .

Table 4-7 SIP Route Pattern Example

IPv4 Pattern

ent-pa.webex.com

SIP Trunk/Route List

Route list for Webex Meetings

Create a route group is created for the Video Mesh cluster. The SIP trunk pointing to the Video Mesh cluster should be added to the Route Group Selected Devices.

Create a route list and add the route group to the top of the list in Selected Groups. This is the route list for Webex Meetings for Webex site ent-pa.webex.com on Unified CM. Specify the route list in the SIP Trunk/Route List field when you configure the SIP route pattern.

In the scenario shown in Figure 4-13 , the SIP endpoint dials 123@ent-pa.webex.com.

Figure 4-13 Routing a Call from a SIP Endpoint

For the example in Figure 4-13 , Unified CM routes the call via the Webex Meetings route list and route group to the Video Mesh cluster SIP trunk, according to how the SIP route pattern interprets the domain pattern ent-pa.webex.com. Unified CM routes the call invite to the node specified by the SIP trunk. (If multiple destinations are specified in the SIP trunk, a single destination is chosen randomly.) The Video Mesh Node then signals to Webex to set up a meeting. Webex then creates the meeting on one of the nodes in the Video Mesh cluster. Note that the node hosting the meeting might not be the same node that initially set up the meeting via the SIP trunk. If the node hosting the meeting reaches full capacity, another node in the cluster will be used and an intra-cluster cascade will be formed. (The intra-cluster cascade routes from node to node, not via Webex.)

If the cluster becomes full, the meeting will have to cascade to Webex to handle the overflow. This will occur automatically if a Webex Teams endpoint or application joins the meeting. The Unified CM dial plan must be modified to allow SIP endpoints to fail over to Webex (via Expressway) if the cluster becomes full.

Create a SIP trunk to an Expressway that can route to the Internet. The same Expressway that is being used for the Webex Hybrid Call Service may be used for this purpose, subject to capacity limits.

Create a route group for Expressway and add it to the route list previously created for Webex Meetings. Ensure that the Webex Video Mesh cluster route group is at the top of the list of Selected Groups in the route list configuration (see Figure 4-14 ). The Expressway route group should be second in the list. This will ensure that the Webex Video Mesh cluster route group will be used as priority. As the cluster reaches full capacity, it will return a SIP 4 xx failure response to Unified CM. Unified CM will then fail over to the Expressway route group and send calls via the Expressway SIP trunk to Expressway and on to Webex.

Figure 4-14 Webex Meetings Route List Configuration

Figure 4-15 shows that a call dialed to 123@ent-pa.webex.com is rejected by the Video Mesh cluster due to the cluster being at full capacity. Based on the second route group in the list, the route list then routes the call to the Expressway SIP trunk, then to Expressway, and on to Webex.

Figure 4-15 Call Being Rerouted Due to Video Mesh Cluster Being at Full Capacity

If many calls are failing over to the Webex cloud media services via Expressway, you should add more nodes to the Video Mesh cluster to handle the load requirements.

### Deploying Video Mesh Services for Multiple Unified CM Clusters

Each Cisco Unified CM cluster should point to a single Video Mesh cluster. We do not recommend pointing a Unified CM cluster to multiple Video Mesh clusters because doing so can result in endpoints that are part of the same meeting sending media to different clusters, resulting in unnecessary cascades to the cloud.

Deploy Video Mesh clusters in sites with large user populations. For the most efficient use of bandwidth, deploy Video Mesh clusters in sites with direct Internet access (DIA), and near to the endpoints. This may result in the need for multiple Video Mesh clusters for geographically dispersed deployments. Consider the example in Figure 4-16 , where there are two sites, A and B. Both sites have:

- Large user populations

- Direct Internet access

Each site in Figure 4-16 has a Unified CM cluster, and a Video Mesh cluster has been deployed in each site. The endpoints in each site are registered to the local Unified CM cluster. Unified CM Cluster A has a SIP trunk pointing to Video Mesh Cluster A, and Unified CM Cluster B has a SIP trunk pointing to Video Mesh Cluster B.

Figure 4-16 Multiple Video Mesh Clusters for Multiple Large Sites

When SIP endpoints in Site A dial into a Webex meeting, they will send media to Video Mesh Cluster A. If all of the endpoints in the meeting are endpoints registered to the Site A Unified CM cluster, all media will remain on-premises, and there will not be overflow to the cloud (assuming the Video Mesh cluster has enough capacity).

If an endpoint registered to the Site B Unified CM cluster dials into the same Webex meeting, the endpoint will route media to Video Mesh Cluster B, as defined by the SIP route pattern on Unified CM Cluster B. Webex will signal to Video Mesh Cluster A and Video Mesh Cluster B to cascade media (cascade is internally initiated) to Webex, so that all endpoints can participate in the same Webex meeting. The media cascade will be sent direct to Webex via the Internet Edge router, as shown in Figure 4-17 .

Figure 4-17 Media Cascaded to Webex if Meeting Participants Are in Different Clusters

### Endpoint Experience

Any of the following types of endpoints can join a Webex meeting:

- Webex Teams application

- Webex Teams device

- SIP endpoint registered to Unified CM

- Webex Meetings application

Depending on the endpoint type used to join a meeting, there may be a difference in the user experience. Webex Teams applications and devices have the same approach for Video Mesh cluster discovery and connectivity as well as a similar mid-call experience, including:

- Video multi-streaming

- Roster support

SIP endpoints discover and connect to a Video Mesh cluster based on the Unified CM configuration. SIP endpoints currently do not offer video multi-streaming or roster support.

The Webex Meetings application does not use Video Mesh for meetings; instead, it connects directly to Webex. The Webex Meeting application does offer roster support.

Figure 4-18 shows an example of the media flows when there are different types of endpoint in the same Webex Meeting.

Figure 4-18 Media Flows for Different Types of Endpoints in the Same Webex Meeting

The Webex Meeting in Figure 4-18 has participants joining via SIP endpoints, Webex Teams applications, Webex Teams devices, and Webex Meetings applications. The SIP endpoints send media to the Video Mesh cluster; the Webex Teams applications and devices also send media to the Video Mesh cluster; and the Webex Meetings Apps send media directly to Webex. The Video Mesh cluster then cascades the media to Webex to allow all endpoints to participate in the same meeting.

## Monitoring Analytics

Use the Webex Control Hub to generate various reports that detail usage analytics. Calling reports are very useful when planning a Webex Video Mesh deployment. We recommend monitoring the reports regularly so that you can grow and modify the Webex Video Mesh deployment architecture over time, depending on how your organization utilizes the service.

Reports are available at https://admin.webex.com via the Video Mesh tab in the Reports section. Reports can be generated for specific Video Mesh clusters or for the entire organization, and data can be displayed based on a specific time period. Utilization reports display graphs based on a selected time range, and they show (see Figure 4-19 ):

- Total Calls — Total call legs handled by the organization (cloud and hybrid)

- Overflowed to Cloud — Number of call legs that overflowed to Webex due to the capacity of the Video Mesh clusters being exceeded

- Cluster Availability — Video Mesh cluster uptime based on the specified time range

Figure 4-19 Example Media Utilization Report

Note A call leg represents a single participant attending a Webex meeting. For example, a Webex meeting with five participants contains five call legs.

Planning for the deployment location and sizing of Webex Video Mesh is complex due to the number of variables that make up a meeting, including:

- Number of meetings in a busy hour

- Number of participants per meeting

- Location of participants in a meeting

- Type of endpoints in a meeting

- Time zone overlap

Other variables that should be taken into account include:

- Internet bandwidth availability at a particular site

- WAN bandwidth availability at a particular site

One size or deployment model does not fit all organizations. Regular monitoring of reports can assist with planning and modifying the initial deployment to better serve the needs of the organization.

The report in Figure 4-19 shows 2356 call legs created for Webex meetings by this organization over a 24 hour period, for a specific Video Mesh cluster. All 2356 call legs were hosted on-premises, with zero call legs overflowed to Webex, which indicates that this Video Mesh cluster has enough capacity. As the Webex deployment grows for this organization, more users and endpoints will likely lead to more meetings and the possibility that the capacity of the Video Mesh cluster will be exceeded. Monitoring the reports regularly will provide feedback to the administrator that can be used to plan for that growth.

We also recommend comparing Webex Media Reports to actual bandwidth usage based on the organization’s existing monitoring tools. This will provide an overall view of how the organization’s network capacity is affected by Webex meetings. As the Webex deployment grows and overflow to the Webex cloud media services increases, more nodes can be added to the Video Mesh cluster to provide more capacity. Factors such as cost of bandwidth and cost of hardware should be considered when making the decision to add more nodes.

In summary, follow these general guidelines for Webex Video Mesh deployments:

- Begin with a small deployment. Deploy a few Video Mesh Nodes in small clusters.

- Continuously monitor Webex Control Hub reports to understand meeting patterns for the organization.

- Add Video Mesh Nodes to clusters as needed.

Cascade Bandwidth Reports

It is very complex to predict the bandwidth usage of the Video Mesh cascade link due to the number of variables involved. Webex Control Hub provides detailed reporting to monitor cascade link bandwidth usage, as illustrated in Figure 4-20 .

Figure 4-20 Cluster Cascade Link Bandwidth Utilization Report

The report in Figure 4-20 details the bandwidth usage for an organization’s Webex Video Mesh cluster cascade link. The organization has 10 clusters configured, with names based on geographical locations. The illustration indicates that the San Jose cluster peaked at 508.81 Mbps of bandwidth for cascading on May 03. This value is cascade transmit (Tx) and receive (Rx) bandwidth. We recommend monitoring this report regularly. Based on the report, decisions can be made regarding whether to add more Video Mesh Node capacity to a cluster, or whether to provision more bandwidth to a site.

The reports can be further refined to detail Tx and Rx bandwidth for a specific cluster, as shown in Figure 4-21 .

Figure 4-21 Tx and Rx Bandwidth Detail Report

If the Tx bandwidth is much higher than the Rx bandwidth, it generally means that meetings are localized with fewer remote participants. If the Rx bandwidth is much higher than the Tx bandwidth, it generally means that there are more remote participants attending meetings using that Video Mesh cluster.

## Webex Video Mesh Deployment Process

Follow these high-level steps to deploy Webex Video Mesh Nodes:

1. Identify sites where Video Mesh clusters will be deployed.

2. Download and install the Video Mesh Node software.

3. Configure the network settings on each Video Mesh Node.

4. Register the Video Mesh Nodes to the Webex organization.

Once you have identified the sites where the Video Mesh clusters will be deployed, you can begin installation of nodes. Download the Video Mesh Node from the Webex Control Hub, then perform the following steps to deploy the Video Mesh Nodes:

1. Deploy the Video Mesh Node OVA file.

2. Power on the Video Mesh Node and set a new password.

a. Power on the Video Mesh Node by right-clicking on the virtual machine in the host list, and choose Power > Power On .

b. Open the Console to the Video Mesh Node.

c. Login to the Video Mesh Node.

Username: admin

Password: cisco

d. On initial login, you will be prompted to change the password. For the current password, type the default password listed above and press Enter . Type the new password, then press Enter and confirm the new password.

e. Press Enter to proceed past the Unauthorized Access screen.

3. Set the network configuration on the Video Mesh Node.

a. From the main menu of the Video Mesh Node console, type 2 and press Enter to choose Edit Configuration .

b. From the screen that describes the effect of changes to the Video Mesh Node, press Enter .

c. Select Static for IP addressing.

d. On the Configure Video Mesh Node screen, configure the network details. The settings that have a * next to their name are mandatory.

Ensure that the IP address is reachable on the internal network.

Ensure that the DNS address is resolvable on the internal network.

e. After completing the network configurations, tab to Save and press Enter .

f. At the prompt to reboot, press Enter .

4. Register the Video Mesh Node to Webex.

a. Once this process has begun, it must be completed within 60 minutes. Ensure that any browser popup blockers are disabled or that an exception is applied for admin.webex.com .

b. From the browser, open admin.webex.com and login with an administrator account.

c. Select Services .

d. From the Video Mesh card, select Set up .

e. Select Yes, I'm ready to register my Video Mesh Node and click Next .

f. Because this is the initial setup of Webex Video Mesh for your organization, there are no clusters configured. Create a cluster by typing a name. We recommend naming clusters based on their geographical location or the name of a data center. In the second field, enter the IP address of the installed Video Mesh Node. Click Next .

g. On the next screen, click Go To Node . A new browser opens, connecting to the Video Mesh Node. You can accept the certificate warnings.

h. Select Allow Access to the Video Mesh Node and click Continue . The Video Mesh Node will perform a number of connectivity tests for Webex services.

i. If tests are successful, go to the browser tab for Cisco Webex Control Hub . The Video Mesh card should show a status of Operational, indicating that node registration is now complete.

More nodes can be added to the configured cluster by clicking Resources from the Video Mesh card and selecting the existing cluster from the Register Video Mesh Node window.

More clusters can be added to the deployment by specifying a new cluster name from the Register Video Mesh Node window.

| Platform | Specifications |
|---|---|
| Cisco Meeting Server 1000 | 72 vCPUs 60 GB main memory 250 GB local hard disk space |
| Specification-based configuration | 46 vCPUs 60 GB main memory 250 GB local hard disk space 2.6 GHz Intel Xeon E5-2600v3 or later processor |

| 1. For additional hardware requirements, refer to the Cisco Webex Video Mesh Data Sheet , available at https://www.cisco.com/c/en/us/solutions/collateral/unified-communications/spark-hybrid-services/datasheet-c78-738153.html . |
|---|

| Source | Destination | Source Address | Source Port | Protocol | Destination Address | Destination Port |
|---|---|---|---|---|---|---|
| Administrator computer | Video Mesh Node | Management device IP address | ANY | TCP HTTPS | Video Mesh Node | 443 |
| Video Mesh Node | Webex cloud media services | Video Mesh Node IP address | ANY | TCP HTTPS | ANY | 443 |
| Video Mesh Node | Webex cloud media services | Video Mesh Node IP address | ANY | UDP NTP | ANY | 123 2 |
| Video Mesh Node | Webex cloud media services | Video Mesh Node IP address | ANY | UDP DNS | ANY | 53 1 |
| Video Mesh Node | Webex cloud media services | Video Mesh Node IP address | ANY | TCP HTTPS | *.docker.io *.wbx2.com *.webex.com | 443 |
| Video Mesh Node #1 | Video Mesh Node #2 | Video Mesh Node #1 IP address | ANY | TCP HTTPS | Video Mesh Node #2 address | 5000 5001 |

| 2. UDP ports 53 and 123 are not required if you are using local DNS and NTP resources. |
|---|

| Source | Destination | Source Address | Source Port | Protocol | Destination Address | Destination Port |
|---|---|---|---|---|---|---|
| Video Mesh Node | Webex cloud media services | ANY | ANY | TCP | ANY | 444 |

| Source IP Address | Destination IP Address | Source UDP Ports | Destination UDP Ports | Protocol | Media Type 4 |
|---|---|---|---|---|---|
| Webex Teams application or endpoint | Webex cloud media services | 52000 to 52099 | 5004 | UDP TCP 5 | Audio |
| Webex Teams application or endpoint | Webex cloud media services | 52100 to 52299 | 5004 | UDP TCP 3 | Video |
| Webex Teams application or endpoint | Video Mesh Node | 52000 to 52099 | 5004 | UDP 3 | Audio |
| Webex Teams application or endpoint | Video Mesh Node | 52100 to 52299 | 5004 | UDP 3 | Video |
| Video Mesh Node | Webex cloud media services | 52500 to 62999 | 5004 | UDP/SRTP 6 | Audio |
| Video Mesh Node | Webex cloud media services | 63000 to 65500 | 5004 | UDP/SRTP 4 | Video |
| Video Mesh Node | Video Mesh Node | 52500 to 62999 | 5004 | UDP/SRTP 4 | Audio |
| Video Mesh Node | Video Mesh Node | 63000 to 65500 | 5004 | UDP/SRTP 4 | Video |

| 3. Egress direction is from the endpoint to Webex. 4. As elsewhere in this document, Audio in this table refers to audio streams of voice-only calls, audio streams of video calls, and related RTCP packets; while Video refers to video streams (main video and presentations or content) and related RTCP packets. 5. UDP is preferred for media traffic. However, if the UDP connection fails, Webex Teams applications can fail-over to TCP for media traffic. 6. TCP can also be used for media cascades from Video Mesh Node to Video Mesh Node, and from Video Mesh Node to the Webex cloud media services. However, UDP is preferred, and TCP can affect media quality. |
|---|

| Description | Source IP Address | Destination IP Address | Source Ports | Destination Ports | Protocol |
|---|---|---|---|---|---|
| Unified CM SIP signaling to Video Mesh cluster | Unified CM | Video Mesh Node | 5060 | 5060 | TCP |
| SIP endpoint signaling to Video Mesh cluster | SIP Endpoint | Video Mesh Node | 5060 to 5062 | 5060 to 5062 | TCP |
| SIP endpoint media to Video Mesh cluster | SIP Endpoint | Video Mesh Node | ANY | 52500 to 62999 for audio 63000 to 65500 for video | UDP |

| Destination (Node) # | Destination Address | Destination Port |
|---|---|---|
| 1 | vmn-1-siteA.ent-pa.com | 5060 or 5061 |
| 2 | vmn-2-siteA.ent-pa.com | 5060 or 5061 |
| 3 | vmn-3-siteA.ent-pa.com | 5060 or 5061 |

| Configuration Field | Setting |
|---|---|
| IPv4 Pattern | ent-pa.webex.com |
| SIP Trunk/Route List | Route list for Webex Meetings |