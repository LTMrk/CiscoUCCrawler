---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-43b428c53b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_011101.html
retrieved_at: 2026-08-16T17:31:23.572997+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Enhanced Locations Call Admission Control

## Chapter: Configure Enhanced Locations Call Admission Control

# Configure Enhanced Locations Call Admission Control

## Enhanced Locations
                        	 Call Admission Control Overview

Enhanced locations
                           		call admission control (CAC) provides control over WAN bandwidth in complex WAN
                           		topologies as well as distributed deployments, where multiple clusters manage
                           		devices in the same physical sites using the same uplinks. Enhanced locations
                           		CAC also allows you to control call admissions for immersive video calls, such
                           		as TelePresence separately from other video calls.

### Network Modeling

To define how your system handles media, you structure your network model around the concepts of locations and links.

A location represents a local area network (LAN). It could contain endpoints or simply serve as a transit location between
                              links for wide area network (WAN) network modeling.

Links interconnect locations and are used to define bandwidth available between locations. Links represent the WAN link.

Weights are measurements of bandwidth pathways. These are used on links to provide a cost to the effective path. Weights are
                              provided when there is more than one path between any two locations.

Your system  calculates shortest paths (least cost) from all locations to all locations and builds effective paths. These
                              have the least overall weight and are the most efficient pathways.

Your system tracks bandwidth across any link that the network model indicates from originating location to terminating location.

### Location Bandwidth
                           	 Manager

The location
                              		bandwidth manager (LBM) service computes the effective path from source
                              		location to destination location. It provides useful functions behind the
                              		scenes, such as handling bandwidth requests from Unified Communications Manager
                              		call control and replicating bandwidth information within the cluster and
                              		between clusters. You can find the configured and realtime information this
                              		function provides in Serviceability Administration.

Locations Media Resource Audio Bit Rate Policy service parameter
                              		determines the bit rate value to deduct from the audio bandwidth pools within
                              		and between the locations of the parties for an audio-only call when a Media
                              		Resource such as a transcoder is inserted into the media path and for more
                              		complex scenarios. This service parameter does not have any impact if there is
                              		no media in one of the call legs. In such cases, location bandwidth manager
                              		deducts the maximum hop bandwidth configured for the source destination from
                              		the available bandwidth of that location.

Do not change the Location Bandwidth Manager bandwidth or link configurations during production hours as that could unnecessarily
                                          spike CPU utilization on the server.

### Intercluster Enhanced Locations Call Admission Control

The intercluster function extends enhanced locations CAC network modeling across multiple clusters. Each cluster manages its
                              own network topology. They then propogate their topologies to other clusters that are configured In the LBM intercluster replication
                              network.

A shared location is a location that is configured with the same name on clusters participating in a the LBM replication network.

This type of location serves the following purposes:

Enables clusters to share their respective configured topologies with one another

Lets multiple clusters perform CAC on the same locations

## Enhanced Locations Call Admission Control Prerequisites

Unified Communications Manager and location bandwidth manager (LBM) manage bandwidth for all types of devices, including IP
                                    phones, gateways, and H.323 and SIP trunk
                                    destinations. However, intercluster enhanced locations CAC
                                    requires SIP intercluster trunks that are assigned to the system shadow location, which is a special location that has no
                                    links to other locations and no bandwidth allocations. All other
                                    types of devices are supported only when assigned to ordinary
                                    (fixed) locations.

Unified Communications Manager and LBM do not manage bandwidth for media resources. For cases in which media resources change
                                    the
                                    bandwidth requirement for a call, you can change a global parameter setting that determines whether the
                                    minimum or maximum bandwidth is reserved.

## Enhanced Locations Call Admission Control Task Flow

Step 1

Activate the LBM Service

Verify whether the Cisco Location Bandwidth Manager service is activated. For a new system install, you must manually enable
                                          the service on the desired nodes. For enhanced locations CAC to work properly, one instance of this service must run on each
                                          cluster.

Step 2

Create an LBM Group

If LBM is not running on the same node, configure an LBM group and assign the LBM group to the server. The LBM group lets
                                          you optimize network delay and performance. Each server must communicate with an LBM service to determine the available bandwidth
                                          for each call and to deduct bandwidth for the duration of each call.

Step 3

Configure Locations and Location Links

Configure locations to implement call admission control in a centralized call-processing system. A location represents a
                                          local area network (LAN), and can contain endpoints or simply serve as a transit location between links for wide area network
                                          (WAN) network modeling. Locations provide bandwidth accounting within a location as well as in or out of a location. Links
                                          provide bandwidth accounting between locations and interconnect locations.

Step 4

(Optional) Assign Intra-Location Bandwidth

Assign intra-location bandwidth to the location, if you do not want to use the default of unlimited bandwidth. By default,
                                          when you create a new location, a link from the newly added location to the Hub_None is added as well, with unlimited audio
                                          bandwidth, 384 kbps video bandwidth and 384 kbps immersive video bandwidth. You can adjust this allotment to match your network
                                          model.

Step 5

Establish External Communication

Configure the LBM hub group to allow the LBM servers acting as hubs to find LBM servers in remote clusters. This step establishes
                                          external communication with those clusters. An LBM service becomes a hub when an LBM hub group is assigned to it. Any LBM
                                          servers that are assigned an LBM hub group establish communication with all other LBM servers that are assigned the same or
                                          an overlapping LBM hub group.

Step 6

Configure the SIP Intercluster Trunk for Enhanced Location Call Admission

Assign a SIP intercluster trunk (ICT) to the shadow location to establish proper intercluster operation. SIP trunks that are
                                          linked to devices with a specific location, such as SIP gateways, can be assigned to ordinary locations. A shadow location
                                          is a special location that contains no links to other locations and no bandwidth allocations.

Step 7

(Optional) Deduct Audio Bandwidth from Audio Pool for Video Calls

Use this procedure if you want to split the audio and video bandwidth deductions into separate pools for video calls. By default,
                                          the system deducts the bandwidth requirement for both the audio stream and video stream from the video pool for video calls.

### Activate the LBM Service

Verify whether the Cisco Location Bandwidth Manager service is activated. For a new system install, you must manually enable
                                 the service on the desired nodes. For enhanced locations CAC to work properly, one instance of this service must run on each
                                 cluster.

Step 1

From Cisco Unified Serviceability, choose Tools > Service Activation .

Step 2

From the Server drop-down list, choose a server, and then click Go .

Step 3

If needed, check the Cisco Location Bandwidth Manager check box.

Step 4

Click Save .

### Create an LBM Group

If LBM is not running on the same node, configure an LBM group and assign the LBM group to the server. The LBM group lets
                                 you optimize network delay and performance. Each server must communicate with an LBM service to determine the available bandwidth
                                 for each call and to deduct bandwidth for the duration of each call.

Step 1

From Cisco Unified CM Administration, choose System > Location Info > Location Bandwidth Manager Group .

Step 2

Perform one of the following tasks:

- Click Find and then choose an existing LBM group from the resulting list to modify the settings for an existing LBM group.

- Click Add New ro add a new LBM group.

Step 3

Configure the fields on the Location Bandwidth Manager Group Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 4

Click Save .

### Configure Locations and Location Links

Configure locations to implement call admission control in a centralized call-processing system. A location represents a
                                 local area network (LAN), and can contain endpoints or simply serve as a transit location between links for wide area network
                                 (WAN) network modeling. Locations provide bandwidth accounting within a location  as well as in or out of a location. Links
                                 provide bandwidth accounting between locations and interconnect locations.

Step 1

From Cisco Unified CM Administration, choose System > Location Info > Location .

Step 2

Perform one of the following tasks:

- Click Find and then choose an existing location from the resulting list, to modify the settings for an existing location.

- Click Add New to add a new location.

Step 3

Configure the fields on the Location Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 4

Click Save .

### Assign Intra-Location Bandwidth

Assign intra-location bandwidth to the location, if you do not want to use the default of unlimited bandwidth. By default,
                                 when you create a new location, a link from the newly added location to the Hub_None is added as well, with unlimited audio
                                 bandwidth, 384 kbps video bandwidth and 384 kbps immersive video bandwidth. You can adjust this allotment to match your network
                                 model.

Tip

If the audio quality is poor or choppy, lower the bandwidth setting. For example, for ISDN use multiples of 56 kbps or 64
                                             kbps.

Step 1

From Cisco Unified CM Administration, choose System > Location Info > Location .

Step 2

Enter search criteria, click Find , and then choose a location from the resulting list.

Step 3

Click Show Advanced to show the intra-location bandwidth fields.

Step 4

If required, choose the kbps radio button for Audio Bandwidth , and then enter a bandwidth value in the text box.

Step 5

If required, choose the kbps radio button for Video Bandwidth , and then enter a bandwidth value in the text box.

Step 6

If required, choose the kbps radio button for Immersive Video Bandwidth , and then enter a bandwidth value in the text box.

Step 7

Click Save .

### Establish External Communication

Configure the LBM hub group to allow the LBM servers acting as hubs to find LBM servers in remote clusters. This step establishes
                                 external communication with those clusters.   An LBM service becomes a hub when an LBM hub group is assigned to it.   Any
                                 LBM servers that are assigned an LBM hub group establish communication with all other LBM servers that are assigned the same
                                 or an overlapping LBM hub group.

Step 1

From Cisco Unified CM Administration, choose System > Location Info > Location Bandwidth Manager (LBM) Intercluster Replication Group .

Step 2

Perform one of the following tasks:

- Click Find to modify the settings for an LBM intercluster replication group, and choose an existing LBM intercluster replication group
                                             from the resulting list.

- Click Add New to add a new LBM intercluster replication group.

Step 3

Configure the fields on the Location Bandwidth Manager Intercluster Replication Group Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 4

Click Save .

### Configure the SIP Intercluster Trunk for Enhanced Location Call Admission

Assign a SIP intercluster trunk (ICT) to the shadow location to establish proper intercluster operation. SIP trunks that are
                                 linked to devices with a specific location, such as SIP gateways, can be assigned to ordinary locations. A shadow location
                                 is a special location that contains no links to other locations and no bandwidth allocations.

#### Before you begin

You need to have a configured SIP intercluster trunk. See SIP Trunk Configuration Task Flow for more information.

Step 1

From Cisco Unified CM Administration, choose Device > Trunk .

Step 2

Enter search criteria, click Find , and then choose an existing SIP intercluster trunk from the resulting list.

Step 3

From the Location drop-down list, choose Shadow .

Step 4

Click Save .

### Deduct Audio Bandwidth from Audio Pool for Video Calls

Use this procedure if you want to split the audio and video bandwidth deductions  into separate pools for video calls. By
                                 default, the system deducts the bandwidth requirement for both the audio  stream and video stream from the video pool for
                                 video calls.

When you enable  this feature, CAC includes the bandwidth required for the IP/UDP network overhead in the audio bandwidth
                                             deduction. This audio bandwidth deduction equates to the audio bit rate plus the IP/UDP network overhead bandwidth requirement.
                                             The video bandwidth deduction is the video bit rate only.

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the publisher node.

Step 3

From the Service drop-down list, choose Cisco CallManager .

Step 4

From the Clusterwide Parameters (Call Admission Control) area, set the value of the Deduct Audio Bandwidth Portion from Audio Pool for a Video Call service parameter to True .

When you configure the Deduct Audio Bandwidth Portion from Audio Pool for a Video Call service parameter to True , the video and immersive video parameters are considered as media level and not as session level. Hence, for a video call,
                                                         you can allocate audio and video bandwidths from audio and video pools respectively for each region and location. The video
                                                         and immersive video bandwidth limits apply only to the video media stream; not to the combination of the audio and video media
                                                         streams.

Step 5

Click Save .

## Enhanced Locations Call Admission Control Interactions and Restrictions

### Enhanced Locations Call Admission Control Interactions

Feature

Interaction

Bandwidth

If there is a conflict in bandwidth capacity or weight assignment on the common links or locations, the local cluster uses
                                             the minimum of the assigned values.

Device support

Your system and LBM manage bandwidth for all types of devices, including IP phones, gateways, and H.323 and SIP trunk
                                             destinations. However, intercluster enhanced locations CAC
                                             requires SIP ICTs assigned to the system shadow location. All other
                                             types of devices are supported only when assigned to ordinary
                                             (fixed) locations.

### Enhanced Locations Call Admission Control Restrictions

Restriction

Description

Bandwidth Reservation Path

During network failure conditions, the bandwidth reservation
                                             path calculated by Unified Communications Manager might not accurately reflect network
                                             conditions. There is no satisfactory way to allow for this scenario
                                             in the model.

Bandwidth and Video Capabilities

If video capabilities are enabled, then bandwidth for audio will be allocated from video.

Synchronization

The model created by the system is not perfectly synchronized at
                                             all times. Use
                                             conservative bandwidth allocations to accommodate this restriction.

Locations Media
                     			 Resource Audio Bit Rate Policy service parameter determines the bit rate value
                     			 to deduct from the audio bandwidth pools within and between the locations of
                     			 the parties for an audio-only call when a media resource such as a transcoder
                     			 is inserted into the media path and for more complex scenarios. This service
                     			 parameter does not have any impact if there is no media in one of the call
                     			 legs. In such cases, location bandwidth manager deducts the maximum hop
                     			 bandwidth that is configured for the source destination from the available
                     			 bandwidth of that location.

| Note | Do not change the Location Bandwidth Manager bandwidth or link configurations during production hours as that could unnecessarily
                                          spike CPU utilization on the server. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Activate the LBM Service | Verify whether the Cisco Location Bandwidth Manager service is activated. For a new system install, you must manually enable
                                          the service on the desired nodes. For enhanced locations CAC to work properly, one instance of this service must run on each
                                          cluster. |
| Step 2 | Create an LBM Group | If LBM is not running on the same node, configure an LBM group and assign the LBM group to the server. The LBM group lets
                                          you optimize network delay and performance. Each server must communicate with an LBM service to determine the available bandwidth
                                          for each call and to deduct bandwidth for the duration of each call. |
| Step 3 | Configure Locations and Location Links | Configure locations to implement call admission control in a centralized call-processing system. A location represents a
                                          local area network (LAN), and can contain endpoints or simply serve as a transit location between links for wide area network
                                          (WAN) network modeling. Locations provide bandwidth accounting within a location as well as in or out of a location. Links
                                          provide bandwidth accounting between locations and interconnect locations. |
| Step 4 | (Optional) Assign Intra-Location Bandwidth | (Optional) Assign intra-location bandwidth to the location, if you do not want to use the default of unlimited bandwidth. By default,
                                          when you create a new location, a link from the newly added location to the Hub_None is added as well, with unlimited audio
                                          bandwidth, 384 kbps video bandwidth and 384 kbps immersive video bandwidth. You can adjust this allotment to match your network
                                          model. |
| Step 5 | Establish External Communication | Configure the LBM hub group to allow the LBM servers acting as hubs to find LBM servers in remote clusters. This step establishes
                                          external communication with those clusters. An LBM service becomes a hub when an LBM hub group is assigned to it. Any LBM
                                          servers that are assigned an LBM hub group establish communication with all other LBM servers that are assigned the same or
                                          an overlapping LBM hub group. |
| Step 6 | Configure the SIP Intercluster Trunk for Enhanced Location Call Admission | Assign a SIP intercluster trunk (ICT) to the shadow location to establish proper intercluster operation. SIP trunks that are
                                          linked to devices with a specific location, such as SIP gateways, can be assigned to ordinary locations. A shadow location
                                          is a special location that contains no links to other locations and no bandwidth allocations. |
| Step 7 | (Optional) Deduct Audio Bandwidth from Audio Pool for Video Calls | (Optional) Use this procedure if you want to split the audio and video bandwidth deductions into separate pools for video calls. By default,
                                          the system deducts the bandwidth requirement for both the audio stream and video stream from the video pool for video calls. |

| Step 1 | From Cisco Unified Serviceability, choose Tools > Service Activation . |
|---|---|
| Step 2 | From the Server drop-down list, choose a server, and then click Go . |
| Step 3 | If needed, check the Cisco Location Bandwidth Manager check box. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Location Info > Location Bandwidth Manager Group . |
|---|---|
| Step 2 | Perform one of the following tasks: Click Find and then choose an existing LBM group from the resulting list to modify the settings for an existing LBM group. Click Add New ro add a new LBM group. |
| Step 3 | Configure the fields on the Location Bandwidth Manager Group Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Location Info > Location . |
|---|---|
| Step 2 | Perform one of the following tasks: Click Find and then choose an existing location from the resulting list, to modify the settings for an existing location. Click Add New to add a new location. |
| Step 3 | Configure the fields on the Location Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 4 | Click Save . |

| Tip | If the audio quality is poor or choppy, lower the bandwidth setting. For example, for ISDN use multiples of 56 kbps or 64
                                             kbps. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Location Info > Location . |
|---|---|
| Step 2 | Enter search criteria, click Find , and then choose a location from the resulting list. |
| Step 3 | Click Show Advanced to show the intra-location bandwidth fields. |
| Step 4 | If required, choose the kbps radio button for Audio Bandwidth , and then enter a bandwidth value in the text box. |
| Step 5 | If required, choose the kbps radio button for Video Bandwidth , and then enter a bandwidth value in the text box. |
| Step 6 | If required, choose the kbps radio button for Immersive Video Bandwidth , and then enter a bandwidth value in the text box. |
| Step 7 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Location Info > Location Bandwidth Manager (LBM) Intercluster Replication Group . |
|---|---|
| Step 2 | Perform one of the following tasks: Click Find to modify the settings for an LBM intercluster replication group, and choose an existing LBM intercluster replication group
                                             from the resulting list. Click Add New to add a new LBM intercluster replication group. |
| Step 3 | Configure the fields on the Location Bandwidth Manager Intercluster Replication Group Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Trunk . |
|---|---|
| Step 2 | Enter search criteria, click Find , and then choose an existing SIP intercluster trunk from the resulting list. |
| Step 3 | From the Location drop-down list, choose Shadow . |
| Step 4 | Click Save . |

| Note | When you enable  this feature, CAC includes the bandwidth required for the IP/UDP network overhead in the audio bandwidth
                                             deduction. This audio bandwidth deduction equates to the audio bit rate plus the IP/UDP network overhead bandwidth requirement.
                                             The video bandwidth deduction is the video bit rate only. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the publisher node. |
| Step 3 | From the Service drop-down list, choose Cisco CallManager . |
| Step 4 | From the Clusterwide Parameters (Call Admission Control) area, set the value of the Deduct Audio Bandwidth Portion from Audio Pool for a Video Call service parameter to True . Note When you configure the Deduct Audio Bandwidth Portion from Audio Pool for a Video Call service parameter to True , the video and immersive video parameters are considered as media level and not as session level. Hence, for a video call,
                                                         you can allocate audio and video bandwidths from audio and video pools respectively for each region and location. The video
                                                         and immersive video bandwidth limits apply only to the video media stream; not to the combination of the audio and video media
                                                         streams. | Note | When you configure the Deduct Audio Bandwidth Portion from Audio Pool for a Video Call service parameter to True , the video and immersive video parameters are considered as media level and not as session level. Hence, for a video call,
                                                         you can allocate audio and video bandwidths from audio and video pools respectively for each region and location. The video
                                                         and immersive video bandwidth limits apply only to the video media stream; not to the combination of the audio and video media
                                                         streams. |
| Note | When you configure the Deduct Audio Bandwidth Portion from Audio Pool for a Video Call service parameter to True , the video and immersive video parameters are considered as media level and not as session level. Hence, for a video call,
                                                         you can allocate audio and video bandwidths from audio and video pools respectively for each region and location. The video
                                                         and immersive video bandwidth limits apply only to the video media stream; not to the combination of the audio and video media
                                                         streams. |
| Step 5 | Click Save . |

| Note | When you configure the Deduct Audio Bandwidth Portion from Audio Pool for a Video Call service parameter to True , the video and immersive video parameters are considered as media level and not as session level. Hence, for a video call,
                                                         you can allocate audio and video bandwidths from audio and video pools respectively for each region and location. The video
                                                         and immersive video bandwidth limits apply only to the video media stream; not to the combination of the audio and video media
                                                         streams. |
|---|---|

| Feature | Interaction |
|---|---|
| Bandwidth | If there is a conflict in bandwidth capacity or weight assignment on the common links or locations, the local cluster uses
                                             the minimum of the assigned values. |
| Device support | Your system and LBM manage bandwidth for all types of devices, including IP phones, gateways, and H.323 and SIP trunk
                                             destinations. However, intercluster enhanced locations CAC
                                             requires SIP ICTs assigned to the system shadow location. All other
                                             types of devices are supported only when assigned to ordinary
                                             (fixed) locations. |

| Restriction | Description |
|---|---|
| Bandwidth Reservation Path | During network failure conditions, the bandwidth reservation
                                             path calculated by Unified Communications Manager might not accurately reflect network
                                             conditions. There is no satisfactory way to allow for this scenario
                                             in the model. |
| Bandwidth and Video Capabilities | If video capabilities are enabled, then bandwidth for audio will be allocated from video. |
| Synchronization | The model created by the system is not perfectly synchronized at
                                             all times. Use
                                             conservative bandwidth allocations to accommodate this restriction. |