---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-14-systemconfig-cucm-b-system-configuration-guide-14su2-cucm-b-sy-7236fc6bfe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/14/systemConfig/cucm_b_system-configuration-guide-14su2/cucm_b_system-configuration-guide-14_chapter_01101.html
retrieved_at: 2026-08-16T16:30:42.262227+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# System Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: August 7, 2026

Chapter: Configure Enhanced Locations Call Admission Control

## Chapter: Configure Enhanced Locations Call Admission Control

# Configure Enhanced Locations Call Admission Control

## Enhanced Locations Call Admission Control Overview

Enhanced Locations Call Admission Control (CAC) lets you regulate audio quality and video availability over complex WAN topologies
                              and intercluster networks. This includes multi-tier and multi-hop networks.

You can create a model of the complete network topology, indicating the different Locations (LANs) and WAN links that connect
                              those locations. For each location and WAN link, assign bandwidth limits that represent the total bandwidth that is available
                              for all calls over that link at one time. If bandwidth is not available for a particular call, the call is rejected with a
                              busy signal. This prevents audio and video quality from degrading as a result of a WAN link becoming oversubscribed.

The intercluster replication functionality of the Location Bandwidth Manger (LBM) Replication Group lets you replicate your
                              location configuration across an intercluster network, thereby making it easier to manage in large intercluster networks.

### Enhanced Locations CAC Components

This feature uses the following components:

Locations—A Location represents a LAN. It could contain endpoints or simply serve as a transit location between links for
                                    WAN network modeling. Cisco Unified Communications Manager supports up to 2000 locations.

Links—The connection between two locations. When configuring this feature, you assign bandwidth allocations and weights for
                                    each link.

Weight—The relative priority of the link in forming the effective path between any pairs of locations. Weights are used only
                                    when multiple paths exist between two locations. Weights are used to calculate the effective path (the path with the least
                                    cumulative weight).

Bandwidth Allocations—The total bandwidth allocated for a particular type of traffic (audio, desktop video, immersive video)
                                    over a specific link. Bandwidth can also be allocated for intralocation calls (the default setting is Unlimited).

Location Bandwidth Manager (LBM)—A feature service that must be activated in Cisco Unified Serviceability for Enhanced Locations
                                    CAC to work. This service assembles the network model and computes the effective path between locations by adding the weight
                                    of all links and locations between the source and destination, and choosing the path with the least cumulative weight.

### Locations Relationship to Regions

The Locations configuration of Enhanced Locations Call Admission Control works with Regions to manage bandwidth for calls:

The bandwidth allocations within the Region Configuration assigns the total amount of bandwidth that the endpoints in a call
                                    between two regions can use.

The bandwidth allocations within Locations Configuration assigns the total amount of bandwidth that all calls between those
                                    locations can use. For an individual call, the bandwidth within the Regions Configuration is deducted from the amount of bandwidth
                                    that the location configuration makes available. For example, if the Locations configuration specifies that 160 kb/s of bandwidth
                                    is available over a particular link, that link can support two G.711 calls at 80 kb/s each simultaneously.

Do not change the Location Bandwidth Manager bandwidth or link configurations during production hours as that could unecessarily
                                          spike CPU utilization on the server.

Cisco Unified Communications Manger supports up to 2,000 locations and 2,000 regions per cluster.

### Intercluster LBM Replication

The Intercluster Replication capability of the Location Bandwidth Manager Hub Group lets you replicate your locations and
                                 link assignments across the larger intercluster network. You can assign LBMs to the LBM Hub role, which lets them actively
                                 replicate locations and link information across a meshed intercluter network. LBM hubs discover each other through their common
                                 connections and form a fully-meshed replication network. LBMs that are assigned a spoke role participate indirectly in intercluster
                                 replication through the LBM hubs in their cluster.

#### Intercluster Topology Management

There are multiple ways to configure and manage your intercluster network. The following table summarizes two approaches for
                                 configuring and managing the intercluster topology:

Design Approach

Description

Location and Link Management

Use a single cluster to configure and manage bandwidth allocations for all links across the intercluster network. This approach
                                             simplifies the configuration overhead, particularly in deployments with many common locations. The intercluster configuration
                                             approach is as follows:

In the management cluster, configure all locations and links (including bandwidth allocations and weights) for the entire
                                             topology. This information will be replicated to the intercluster network.

For the other clusters in the topology:

Configure locations for the local cluster only. This is solely to associate devices to a location.

Do not configure link information.

Leave all bandwidth allocations in the local cluster as Unlimited . If the management cluster replicates bandwidth allocations that are less than the local cluster, the more restrictive configuration
                                                   will be applied.

Intercluster Enhanced Locations CAC

With this approach:

Within each cluster, configure the local locations and link information to the neighboring cluster only.

Assign link information, including weighth and bandwidth allocation, to neighboring clusters only. The rest of the topology
                                                   gets replicated by the

The Hub_None location must be renamed in each cluster or it will be a common location across clusters.

Each cluster requires a unique Cluster ID.

## Enhanced Locations CAC Prerequisites

Make sure that you understand your LAN and WAN network topology before you attempt to configure this feature. This is required
                              in order to allocate bandwidth for locations and links.

## Enhanced Locations CAC Task Flow

Step 1

Activate Location Bandwidth Manager

The Cisco Location Bandwidth Manager feature service must be running on at least one cluster node.

Step 2

Configure LBM Group

By default, the Cisco CallManager service communicates with the local LBM service. However, LBM groups can be used to manage
                                          this communication, providing an active and standby LBM for redundancy.

Step 3

Configure Locations and Links

Create the locations (LANs) for your network and assign bandwidth allocations for the WAN links that connect those locations.

Step 4

Configure LBM Intercluster Replication Group

Create an intercluster replication group that replicates configured CAC information to other clusters.

Step 5

Configure SIP Intercluster Trunks

Assign the Shadow location to the SIP intercluster trunks in your network.

Step 6

Configure Call Admission Control Service Parameters

Optional. Configure service parameter settings for Call Admission Control. The default settings may be sufficient for many
                                          deployments.

### Activate Location Bandwidth Manager

Step 1

From Cisco Unified Serviceability, choose Tools > Service Activation .

Step 2

From the Server drop-down, select the cluster node on which you want the service to run and click Go.

Step 3

Under CM Services , check the Cisco Location Bandwidth Manager service

Step 4

Click Save .

Step 5

Repeat this task if you want to start the service on addiitonal  nodes.

### Configure LBM Group

The order in which the Cisco CallManager service uses the LBM is as follows:

LBM Group designation

Local LBM (co-resident)

Step 1

From Cisco Unified CM Administration, choose System > Locations > Location Bandwidth Manager Group .

Step 2

Click Add New .

Step 3

Assign a Name to the group.

Step 4

From the Active Member drop-down, select the active member of this group.

Step 5

From the Standby Member drop-down, select a desired standby to be used when the active member is unavailable.

Step 6

Click Save .

### Configure Locations and Links

Step 1

From Cisco Unfiied CM Administration, choose System > Location Info > Location .

Step 2

Click Add New to create a new location.

Step 3

Assign a Name for the location.

Step 4

In the Links - Bandwidth Between This Location and Adjacent Locations area, configure settings for WAN links to a another location:

Select a second location from the Location list box.

Configure the Weight that reflects the relative priority of this link in forming the effective path.

Configure total bandwidth for audio, video, and immersive video (TelePresence) calls.

Repeat these substeps to configure links to any additional locations.

Step 5

Optional. Expand the Intra-location - Bandwidth for Devices Within This Location area and configure total bandwidth allocations for intralocation calls for the newly created location. The default setting
                                          for all media types for these calls is Unlimited .

Step 6

In the Modify Settings to Other Locations area, configure RSVP settings to other locations:

In the Location column select the other location.

Select the RSVP Setting for calls between these locations.

Repeat these substeps to add RSVP settings for calls with additional locations.

Step 7

Click Save .

Step 8

Repeat this procedure to create additional locations and to configure links to and from those new locations.

### Configure LBM Intercluster Replication Group

Step 1

From Cisco Unified CM Administration, choose System > Location Info > Location Bandwidth Manager (LBM) Intercluster Replication Group .

Step 2

Click Add New .

Step 3

Enter a Name for the group.

Step 4

In the Bootstrap Servers area, assign one or more LBM servers to be responsible for replicating connectivity information to other hubs.

Step 5

In the Role Assignments area, use the up and down arrows to select the local LBM servers that will act as hubs, and the LBM servers that will remain
                                          as spokes.

Step 6

Click Save .

### Configure SIP Intercluster Trunks

Step 1

From Cisco Unified CM Administration, choose Device > Trunks .

Step 2

Click Find and select the appropriate intercluster trunk.

Step 3

From the Location drop-down, select Shadow .

Step 4

Complete any other fields that you want in the Trunk Confiiguration window. For help with the fields and their settings, see the online help.

Step 5

Click Save .

Step 6

Repeat this task for any other intercluster trunks that will replicate information for Enhanced Locations Call Admission Control.

### Configure Call Admission Control Service Parameters

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down, select a cluster node.

Step 3

Configure service parameters for the Cisco CallManager service:

From the Service drop-down, select Cisco CallManager .

In the Clusterwide Parameters (Call Admission Control) area, configure any service parameters. For parameter help descriptions, click the name of the parameter in the GUI.

Click Save .

Step 4

Configure settings for the Cisco Location Bandwidth Manager service:

From the Service drop-down, select Cisco Location Bandwidth Manager .

Configure any service parameters that you want. For parameter help descriptions, click the name of the parameter in the GUI.

Click Save .

## Enhanced Locations CAC Interactions Restrictions

The following table displays feature interactions and restrictions for Enhanced Locations Call Admission Control.

Feature

Interactions and Restrictions

LBM Security Mode

By default, the LBM Security Mode is Insecure. You can reconfigure this setting with the LBM Security Mode enterprise parameter. This parameter can be set to Secure , Insecure , or Mixed .

The Mixed setting can be used temporarily to maintain communication while you are securing all of your clusters, following which you
                                          can change the setting to Secure .

After changing this parameter, you must reset all Cisco LBM Service Hubs in the cluster for this to take effect.

Audio Bandwidth Deduction in Video Calls

By default, bandwidth for the audio portion of a video call is deducted from the video pool. You can reconfigure the system
                                          so that the audio portion of a video call is deducted from the audio pool by setting the Deduct Audio Portion from Audio Pool for Video Calls service parameter to True (the default setting is False ).

Video Call Classification

Cisco TelePresence endpoints have a nonconfigurable video call classification of Immersive .

Other endpoints have a nonconfigurable video call classification of Desktop .

For SIP trunks, you can set the video classification (Desktop, Immersive or Mixed) by configuring the Video Call Traffic Class within the associated SIP Profile.

Media Resources

Bandwidth for media resources is not allocated via Call Admissions Control.

Locations Serviceability

The Cisco Unified Serviceability interface contains additional tools for managing and monitoring the Locations topology. For
                                          details, see the "Locations" topics in the Cisco Unified Serviceability Administration Guide .

Session Bandwidth Modifiers

You can assign which Session Bandwidth Modifiers are used by SIP endpoints within the SIP Profile Configuration window.

Bandwidth Allocation Conflicts

If there is a conflict in bandwidth capacity or weight assignment on the common links or locations, the local cluster uses
                                          the minimum of the assigned values.

Device Support

Your system and LBM manage bandwidth for all types of devices, including IP phones, gateways, and H.323 and SIP trunk destinations.
                                          However, intercluster enhanced locations CAC requires SIP ICTs assigned to the system shadow location. All other types of
                                          devices are supported only when assigned to ordinary (fixed) locations.

Network Failures

During network failure conditions, the bandwidth reservation path calculated by Unified Communications Manager might not accurately
                                          reflect network conditions. There is no satisfactory way to allow for this scenario in the model.

Synchronization Issues

The model created by the system is not perfectly synchronized at all times. Use conservative bandwidth allocations to accommodate
                                          this restriction.

Clustering over the WAN

For deployments with clustering over the WAN and local failover, intracluster LBM traffic is already calculated into the WAN
                                          bandwidth calculations.

Flexible DSCP Marking

For additional QoS, you can use DSCP marking to assign markings that prioritize certain types of call flows over others. For
                                          example, you can prioritize audio over video so that even if the network is congested, blocking video media, basic communication
                                          can continue via audio.

You can configure DSCP marking in two ways:

Service Parameters—Configure clusterwide DSCP defaults within the Service Parameter Configuration window's Clusterwide Parameters (System - QoS) section.

SIP Profile—Configure customized DSCP settings in a SIP Profile and apply them to certain groups of SIP devices. This setting
                                                overrides the clusterwide default.

APIC-EM Controller

You can use an APIC_EM Controller to manage SIP media flows for external QoS management. For details, refer to the Feature Configuration Guide for Cisco Unified Communications Manager .

| Note | Do not change the Location Bandwidth Manager bandwidth or link configurations during production hours as that could unecessarily
                                          spike CPU utilization on the server. |
|---|---|

| Design Approach | Description |
|---|---|
| Location and Link Management | Use a single cluster to configure and manage bandwidth allocations for all links across the intercluster network. This approach
                                             simplifies the configuration overhead, particularly in deployments with many common locations. The intercluster configuration
                                             approach is as follows: In the management cluster, configure all locations and links (including bandwidth allocations and weights) for the entire
                                             topology. This information will be replicated to the intercluster network. For the other clusters in the topology: Configure locations for the local cluster only. This is solely to associate devices to a location. Do not configure link information. Leave all bandwidth allocations in the local cluster as Unlimited . If the management cluster replicates bandwidth allocations that are less than the local cluster, the more restrictive configuration
                                                   will be applied. |
| Intercluster Enhanced Locations CAC | With this approach: Within each cluster, configure the local locations and link information to the neighboring cluster only. Assign link information, including weighth and bandwidth allocation, to neighboring clusters only. The rest of the topology
                                                   gets replicated by the The Hub_None location must be renamed in each cluster or it will be a common location across clusters. Each cluster requires a unique Cluster ID. Note It;s critical for replication to name clusters consistenly across all clusters. | Note | It;s critical for replication to name clusters consistenly across all clusters. |
| Note | It;s critical for replication to name clusters consistenly across all clusters. |

| Note | It;s critical for replication to name clusters consistenly across all clusters. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Activate Location Bandwidth Manager | The Cisco Location Bandwidth Manager feature service must be running on at least one cluster node. |
| Step 2 | Configure LBM Group | By default, the Cisco CallManager service communicates with the local LBM service. However, LBM groups can be used to manage
                                          this communication, providing an active and standby LBM for redundancy. |
| Step 3 | Configure Locations and Links | Create the locations (LANs) for your network and assign bandwidth allocations for the WAN links that connect those locations. |
| Step 4 | Configure LBM Intercluster Replication Group | Create an intercluster replication group that replicates configured CAC information to other clusters. |
| Step 5 | Configure SIP Intercluster Trunks | Assign the Shadow location to the SIP intercluster trunks in your network. |
| Step 6 | Configure Call Admission Control Service Parameters | Optional. Configure service parameter settings for Call Admission Control. The default settings may be sufficient for many
                                          deployments. |

| Step 1 | From Cisco Unified Serviceability, choose Tools > Service Activation . |
|---|---|
| Step 2 | From the Server drop-down, select the cluster node on which you want the service to run and click Go. |
| Step 3 | Under CM Services , check the Cisco Location Bandwidth Manager service |
| Step 4 | Click Save . |
| Step 5 | Repeat this task if you want to start the service on addiitonal  nodes. Note Cisco recommends running the Cisco Location Bandwidth Manager service on each subscriber node in the cluster that is also
                                                      running the Cisco CallManager service. | Note | Cisco recommends running the Cisco Location Bandwidth Manager service on each subscriber node in the cluster that is also
                                                      running the Cisco CallManager service. |
| Note | Cisco recommends running the Cisco Location Bandwidth Manager service on each subscriber node in the cluster that is also
                                                      running the Cisco CallManager service. |

| Note | Cisco recommends running the Cisco Location Bandwidth Manager service on each subscriber node in the cluster that is also
                                                      running the Cisco CallManager service. |
|---|---|

| Note | The order in which the Cisco CallManager service uses the LBM is as follows: LBM Group designation Local LBM (co-resident) |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Locations > Location Bandwidth Manager Group . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Assign a Name to the group. |
| Step 4 | From the Active Member drop-down, select the active member of this group. |
| Step 5 | From the Standby Member drop-down, select a desired standby to be used when the active member is unavailable. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unfiied CM Administration, choose System > Location Info > Location . |
|---|---|
| Step 2 | Click Add New to create a new location. |
| Step 3 | Assign a Name for the location. |
| Step 4 | In the Links - Bandwidth Between This Location and Adjacent Locations area, configure settings for WAN links to a another location: Select a second location from the Location list box. Configure the Weight that reflects the relative priority of this link in forming the effective path. Configure total bandwidth for audio, video, and immersive video (TelePresence) calls. Repeat these substeps to configure links to any additional locations. |
| Step 5 | Optional. Expand the Intra-location - Bandwidth for Devices Within This Location area and configure total bandwidth allocations for intralocation calls for the newly created location. The default setting
                                          for all media types for these calls is Unlimited . |
| Step 6 | In the Modify Settings to Other Locations area, configure RSVP settings to other locations: In the Location column select the other location. Select the RSVP Setting for calls between these locations. Repeat these substeps to add RSVP settings for calls with additional locations. |
| Step 7 | Click Save . |
| Step 8 | Repeat this procedure to create additional locations and to configure links to and from those new locations. |

| Step 1 | From Cisco Unified CM Administration, choose System > Location Info > Location Bandwidth Manager (LBM) Intercluster Replication Group . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter a Name for the group. |
| Step 4 | In the Bootstrap Servers area, assign one or more LBM servers to be responsible for replicating connectivity information to other hubs. |
| Step 5 | In the Role Assignments area, use the up and down arrows to select the local LBM servers that will act as hubs, and the LBM servers that will remain
                                          as spokes. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Trunks . |
|---|---|
| Step 2 | Click Find and select the appropriate intercluster trunk. |
| Step 3 | From the Location drop-down, select Shadow . |
| Step 4 | Complete any other fields that you want in the Trunk Confiiguration window. For help with the fields and their settings, see the online help. |
| Step 5 | Click Save . |
| Step 6 | Repeat this task for any other intercluster trunks that will replicate information for Enhanced Locations Call Admission Control. |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down, select a cluster node. |
| Step 3 | Configure service parameters for the Cisco CallManager service: From the Service drop-down, select Cisco CallManager . In the Clusterwide Parameters (Call Admission Control) area, configure any service parameters. For parameter help descriptions, click the name of the parameter in the GUI. Click Save . |
| Step 4 | Configure settings for the Cisco Location Bandwidth Manager service: From the Service drop-down, select Cisco Location Bandwidth Manager . Configure any service parameters that you want. For parameter help descriptions, click the name of the parameter in the GUI. Click Save . |

| Feature | Interactions and Restrictions |
|---|---|
| LBM Security Mode | By default, the LBM Security Mode is Insecure. You can reconfigure this setting with the LBM Security Mode enterprise parameter. This parameter can be set to Secure , Insecure , or Mixed . The Mixed setting can be used temporarily to maintain communication while you are securing all of your clusters, following which you
                                          can change the setting to Secure . After changing this parameter, you must reset all Cisco LBM Service Hubs in the cluster for this to take effect. |
| Audio Bandwidth Deduction in Video Calls | By default, bandwidth for the audio portion of a video call is deducted from the video pool. You can reconfigure the system
                                          so that the audio portion of a video call is deducted from the audio pool by setting the Deduct Audio Portion from Audio Pool for Video Calls service parameter to True (the default setting is False ). |
| Video Call Classification | Cisco TelePresence endpoints have a nonconfigurable video call classification of Immersive . Other endpoints have a nonconfigurable video call classification of Desktop . For SIP trunks, you can set the video classification (Desktop, Immersive or Mixed) by configuring the Video Call Traffic Class within the associated SIP Profile. |
| Media Resources | Bandwidth for media resources is not allocated via Call Admissions Control. |
| Locations Serviceability | The Cisco Unified Serviceability interface contains additional tools for managing and monitoring the Locations topology. For
                                          details, see the "Locations" topics in the Cisco Unified Serviceability Administration Guide . |
| Session Bandwidth Modifiers | You can assign which Session Bandwidth Modifiers are used by SIP endpoints within the SIP Profile Configuration window. |
| Bandwidth Allocation Conflicts | If there is a conflict in bandwidth capacity or weight assignment on the common links or locations, the local cluster uses
                                          the minimum of the assigned values. |
| Device Support | Your system and LBM manage bandwidth for all types of devices, including IP phones, gateways, and H.323 and SIP trunk destinations.
                                          However, intercluster enhanced locations CAC requires SIP ICTs assigned to the system shadow location. All other types of
                                          devices are supported only when assigned to ordinary (fixed) locations. |
| Network Failures | During network failure conditions, the bandwidth reservation path calculated by Unified Communications Manager might not accurately
                                          reflect network conditions. There is no satisfactory way to allow for this scenario in the model. |
| Synchronization Issues | The model created by the system is not perfectly synchronized at all times. Use conservative bandwidth allocations to accommodate
                                          this restriction. |
| Clustering over the WAN | For deployments with clustering over the WAN and local failover, intracluster LBM traffic is already calculated into the WAN
                                          bandwidth calculations. |
| Flexible DSCP Marking | For additional QoS, you can use DSCP marking to assign markings that prioritize certain types of call flows over others. For
                                          example, you can prioritize audio over video so that even if the network is congested, blocking video media, basic communication
                                          can continue via audio. You can configure DSCP marking in two ways: Service Parameters—Configure clusterwide DSCP defaults within the Service Parameter Configuration window's Clusterwide Parameters (System - QoS) section. SIP Profile—Configure customized DSCP settings in a SIP Profile and apply them to certain groups of SIP devices. This setting
                                                overrides the clusterwide default. |
| APIC-EM Controller | You can use an APIC_EM Controller to manage SIP media flows for external QoS management. For details, refer to the Feature Configuration Guide for Cisco Unified Communications Manager . |