---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-213794-configure-lo-7e7c9a3d69
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/213794-configure-location-bandwidth-manager-and.html
retrieved_at: 2026-08-21T13:57:44.209772+00:00
---

Configure Location Bandwidth Manager and Related Alerts

# Configure Location Bandwidth Manager and Related Alerts

### Download Options

Updated: October 9, 2018

Document ID: 213794

Contents

## Contents

## Introduction

This document describes the configuration and alerts related to Location Bandwidth Manager (LBM).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of Cisco Unified Communications Manager (CUCM) version 11.5.

### Components Used

The information in this document is based on Cisco Call Manager (CCM) version 11.5.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

The LBM service computes the effective path from source location to destination location. It provides useful functions behind the scenes, such as handling bandwidth requests from Unified Communications Manager call control and replicating bandwidth information within the cluster and between clusters. You can find the configured and real-time information this function provides in Serviceability Administration.

## Configure

### 1. Activate LBM Service

Verify whether the Cisco LBM service is activated. For a new system install, you must manually enable the service on the desired nodes. For enhanced locations CAC to work properly, one instance of this service must run on each cluster.

Step 1

From Cisco Unified Serviceability, navigate to Tools > Service Activation .

Step 2

From the Server drop-down list, choose a server, and then click Go as seen in the image.

Step 3

If needed, check the Cisco Location Bandwidth Manager check box.

Step 4

Click Save .

### 2. Create LBM Group

If LBM is not running on the same node, configure an LBM group and assign the LBM group to the server. The LBM group lets you optimize network delay and performance. Each server must communicate with an LBM service in order to determine the available bandwidth for each call and to deduct bandwidth for the duration of each call.

Step 1

From Cisco Unified CM Administration, navigate to System > Location Info > Location Bandwidth Manager Group .

Step 2

Perform one of these tasks:

- In order to modify the settings for an existing LBM group, enter search criteria, click Find , and then choose an existing LBM group from the resulting list.

- In order to add a new LBM group, click Add New .

Step 3

Configure the fields on the Location Bandwidth Manager Group Configuration window. See the online help for more information about the fields and their configuration options.

Step 4

Click Save as seen in this image.

### 3. Configure Locations and Location Links

Configure locations in order to implement call admission control in a centralized call-processing system. A location represents a Local Area Network (LAN), and can contain endpoints or simply serve as a transit location between links for Wide Area Network (WAN) network modeling. Locations provide bandwidth accounting within a location as well as in or out of a location. Links provide bandwidth accounting between locations and interconnect locations.

Step 1

From Cisco Unified CM Administration, navigate to System > Location Info > Location .

Step 2

Perform these tasks:

- In order to modify the settings for an existing location, enter search criteria, click Find , and then choose an existing location from the resulting list.

- In order to add a new location, click Add New .

Step 3

Configure the fields on the Location Configuration window as per requirements

Step 4

Click Save as shown in this image.

Note : If the inter audio bandwidth for 2 locations has been specified to be 1080kbps and if the inter region codec is G711ulaw ( 64kbps) then approx 16 calls can be active simultaneously (1080/64). Considering this, you can accordingly set the audio and video bandwidth relation.

### 4. Assign Intra-Location Bandwidth

Assign intra-location bandwidth to the location, if you do not want to use the default of unlimited bandwidth. By default, when you create a new location, a link from the newly added location to the Hub_None is added as well, with unlimited audio bandwidth, 384 kbps video bandwidth and 384 kbps immersive video bandwidth. You can adjust this allotment to match your network model.

Note : If the audio quality is poor or choppy, lower the bandwidth setting. For example, for ISDN use multiples of 56 kbps or 64 kbps.

Step 1

From Cisco Unified CM Administration, navigate to System > Location Info > Location .

Step 2

Enter search criteria, click Find , and then choose a location from the resulting list.

Step 3

Click Show Advanced in order to show the intra-location bandwidth fields.

Step 4

If required, choose the kbps radio button for Audio Bandwidth , and then enter a bandwidth value in the text box.

Step 5

If required, choose the kbps radio button for Video Bandwidth , and then enter a bandwidth value in the text box.

Step 6

If required, choose the kbps radio button for Immersive Video Bandwidth , and then enter a bandwidth value in the text box.

Step 7

Click Save as shown in this image.

### 5. Establish External Communication

Configure the LBM hub group to allow the LBM servers acting as hubs to find LBM servers in remote clusters. This step establishes external communication with those clusters. An LBM service becomes a hub when an LBM hub group is assigned to it. Any LBM servers that are assigned an LBM hub group establish communication with all other LBM servers that are assigned the same or an overlapping LBM hub group.

Step 1

From Cisco Unified CM Administration, navigate to System > Location Info > Location Bandwidth Manager (LBM) Intercluster Replication Group .

Step 2

Perform one of these tasks:

- In order to modify the settings for an LBM intercluster replication group, enter search criteria, click Find , and choose an existing LBM intercluster replication group from the resulting list.

- In order to add a new LBM intercluster replication group, click Add New .

Step 3

Configure the fields on the Location Bandwidth Manager Intercluster Replication Group Configuration window. See the online help for more information about the fields and their configuration options.

Step 4

Click Save as shown in this image.

### 6. Configure SIP Intercluster Trunk for Enhanced Location Call Admission Control

Assign a SIP Intercluster Trunk (ICT) to the shadow location to establish proper intercluster operation. SIP trunks that are linked to devices with a specific location, such as SIP gateways, can be assigned to ordinary locations. A shadow location is a special location that contains no links to other locations and no bandwidth allocations.

Step 1

From Cisco Unified CM Administration, navigate to Device > Trunk .

Step 2

Enter search criteria, click Find , and then choose an existing SIP intercluster trunk from the resulting list.

Step 3

From the Location drop-down list, choose Shadow .

Step 4

Click Save .

### 7. Deduct Audio Bandwidth from Audio Pool for Video Calls

Use this procedure if you want to split the audio and video bandwidth deductions into separate pools for video calls. By default, the system deducts the bandwidth requirement for both the audio stream and video stream from the video pool for video calls.

Note : When you enable this feature, CAC includes the bandwidth required for the IP/UDP network overhead in the audio bandwidth deduction. This audio bandwidth deduction equates to the audio bit rate plus the IP/UDP network overhead bandwidth requirement. The video bandwidth deduction is the video bit rate only.

Step 1

From Cisco Unified CM Administration, navigate to System > Service Parameters .

Step 2

From the Server drop-down list, choose the publisher node.

Step 3

From the Service drop-down list, choose Cisco Call Manager .

Step 4

From the Clusterwide Parameters (Call Admission Control) area, set the value of the Deduct Audio Bandwidth Portion from Audio Pool for a Video Call service parameter to True .

Step 5

Click Save .

## Verify

Use this section to confirm that your configuration works properly.

### RTMT Alerts

```
Name : Hub_None->Tampa-MLK
ResourceType : 2
AppID : Cisco Location Bandwidth Manager ClusterID : PUB01-Cluster NodeID : SUB01 TimeStamp : Tue Aug 01 11:15:25 EDT 2018. 
The alarm is generated on Tue Aug 01 11:15:25 EDT 2018
```

Alert Definition:

LocationOutOfResources: This counter represents the total number of times that a call through Locations failed due to the lack of bandwidth.

Explanation: The Location or Link connecting locations has run out of audio/video/immersive bandwidth and hence no further calls can originate or pass through the location/link. The out of resource condition may be temporary due to high number of calls during peak hours and may correct by itself when calls terminate and bandwidth is freed up.

Recommended Action: Consider adding additional bandwidth to the location/link under below option:

System > Location info > Location .

```
Enum Definitions - ResourceType
Value          Definition
1                 Audio bandwidth out of resource
2                 Video bandwidth out of resource
3                 Immersive bandwidth out of resource
```

You can also monitor this instance from CLI:

```
show perf query class "Cisco Locations LBM"
show perf query counter "Cisco Locations LBM" "BandwidthMaximum"
show perf query counter "Cisco Locations LBM" "BandwidthAvailable"
show perf query counter "Cisco Locations LBM" "CallsInProgress
```

Note : In case video bandwidth, you would need to increase by at least 384 kbps in order to allow one more video call to traverse this path. It might be set as high as the your network design supports.

You can also monitor the instances from RTMT as well:

Configure Alerts on RTMT

Ref Guide : RTMT Guide

Error Message:

```
%UC_Location Bandwidth Manager-5-LBMLinkISV: %[RemoteIPAddress=String][LinkID=String][LocalNodeId=UInt][LocalApplicationId=Enum][RemoteApplicationId=Enum][AppID=String][ClusterID=String][NodeID=String]: LBM link to remote application restored.
```

Explanation: This alarm indicates that the LBM has gained communication with the remote LBM. Note that the remote LBM should also indicate LBMLinkISV.

Recommended Action: Informational only; no action is required.

```
Reason Code - Enum Definitions

 

Enum Definitions - LocalApplicationId

Value       Definition
700           LocationBandwidthManager

 

Enum Definitions - RemoteApplicationId

Value      Definition
700          LocationBandwidthManager
```

Error Message:

```
%UC_Location Bandwidth Manager-1-LBMLinkOOS: %[RemoteIPAddress=String][LinkID=String][LocalNodeId=UInt][LocalApplicationID=Enum][RemoteNodeID=UInt][RemoteApplicationID=Enum][AppID=String][ClusterID=String][NodeID=String]: LBM link to remote application is out of service.
```

Explanation: This alarm indicates that the local LBM has lost communication with the remote LBM. This alarm usually indicates that a node has gone out of service (whether intentionally for maintenance or to install a new load for example; or unintentionally due to a service failure or connectivity failure).

Recommended Action: In the Cisco Unified Reporting tool, run a CM Cluster Overview report and check to see if all servers can communicate with the Publisher. Also, check for any alarms that might have indicated a CallManager OR location bandwidth manager failure and take appropriate action for the indicated failure. If the node was taken out of service intentionally, bring the node back into service.

```
Reason Code - Enum Definitions

Enum Definitions - LocalApplicationID

Value        Definition
700           LocationBandwidthManager

 

Enum Definitions - RemoteApplicationID

Value         Definition
700            LocationBandwidthManager
```

## Troubleshoot

This section provides information you can use to troubleshoot your configuration.

In order to troubleshoot further you need these logs from Call manager with the use of RTMT:

- Call Manager Detailed level traces

- Location bandwidth manager traces

| Step 1 | From Cisco Unified Serviceability, navigate to Tools > Service Activation . |
|---|---|
| Step 2 | From the Server drop-down list, choose a server, and then click Go as seen in the image. |
| Step 3 | If needed, check the Cisco Location Bandwidth Manager check box. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, navigate to System > Location Info > Location Bandwidth Manager Group . |
|---|---|
| Step 2 | Perform one of these tasks: - In order to modify the settings for an existing LBM group, enter search criteria, click Find , and then choose an existing LBM group from the resulting list. - In order to add a new LBM group, click Add New . |
| Step 3 | Configure the fields on the Location Bandwidth Manager Group Configuration window. See the online help for more information about the fields and their configuration options. |
| Step 4 | Click Save as seen in this image. |

| Step 1 | From Cisco Unified CM Administration, navigate to System > Location Info > Location . |
|---|---|
| Step 2 | Perform these tasks: - In order to modify the settings for an existing location, enter search criteria, click Find , and then choose an existing location from the resulting list. - In order to add a new location, click Add New . |
| Step 3 | Configure the fields on the Location Configuration window as per requirements |
| Step 4 | Click Save as shown in this image. |

| Step 1 | From Cisco Unified CM Administration, navigate to System > Location Info > Location . |
|---|---|
| Step 2 | Enter search criteria, click Find , and then choose a location from the resulting list. |
| Step 3 | Click Show Advanced in order to show the intra-location bandwidth fields. |
| Step 4 | If required, choose the kbps radio button for Audio Bandwidth , and then enter a bandwidth value in the text box. |
| Step 5 | If required, choose the kbps radio button for Video Bandwidth , and then enter a bandwidth value in the text box. |
| Step 6 | If required, choose the kbps radio button for Immersive Video Bandwidth , and then enter a bandwidth value in the text box. |
| Step 7 | Click Save as shown in this image. |

| Step 1 | From Cisco Unified CM Administration, navigate to System > Location Info > Location Bandwidth Manager (LBM) Intercluster Replication Group . |
|---|---|
| Step 2 | Perform one of these tasks: - In order to modify the settings for an LBM intercluster replication group, enter search criteria, click Find , and choose an existing LBM intercluster replication group from the resulting list. - In order to add a new LBM intercluster replication group, click Add New . |
| Step 3 | Configure the fields on the Location Bandwidth Manager Intercluster Replication Group Configuration window. See the online help for more information about the fields and their configuration options. |
| Step 4 | Click Save as shown in this image. |

| Step 1 | From Cisco Unified CM Administration, navigate to Device > Trunk . |
|---|---|
| Step 2 | Enter search criteria, click Find , and then choose an existing SIP intercluster trunk from the resulting list. |
| Step 3 | From the Location drop-down list, choose Shadow . |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, navigate to System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the publisher node. |
| Step 3 | From the Service drop-down list, choose Cisco Call Manager . |
| Step 4 | From the Clusterwide Parameters (Call Admission Control) area, set the value of the Deduct Audio Bandwidth Portion from Audio Pool for a Video Call service parameter to True . |
| Step 5 | Click Save . |