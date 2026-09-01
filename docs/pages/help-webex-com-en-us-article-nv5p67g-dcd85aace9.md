---
doc_id: help-webex-com-en-us-article-nv5p67g-dcd85aace9
source_url: https://help.webex.com/en-us/article/nv5p67g
retrieved_at: 2026-09-01T21:38:16.154505+00:00
---

Hybrid
                    Call Service on the Call Connector architecture has gone End of Life
                    (EOL) , so the service is no longer officially supported. Call Connector
                should not be considered for future Expressway capacity planning for Hybrid
                Services.

This article does not cover capacity planning for the Hybrid
                Calendar Service Cisco TMS integration with Office 365 or Cisco TMS integration with
                Google Calendar. For capacity information, see the Deployment Guide for Cisco Webex Hybrid Calendar Service.

Plan Capacity for Hybrid Services

We provide this article to address your capacity planning questions and explain how we calculate user scale. To model your scenario, try the Hybrid Services capacity calculator .

### Planning Considerations

When planning Expressway capacity for your Hybrid Services user population, consider the following questions:

Which Hybrid Services do you need?

The Expressway can host connectors for Hybrid Call Service, Hybrid Calendar Service, and Hybrid Message Service.

How many users do you have, for each service?

The more users you have for each service, the more likely it is that you will want to dedicate Expressway clusters to services. For smaller populations, running multiple connectors on a shared cluster (coresidency) is a valid choice.

Are your needs going to change?

You may want to start small, with one Expressway cluster providing service to a group of early adopters in your organization, and plan growth for a future rollout. You can migrate from a shared model to a dedicated model, or scale your existing cluster, to meet your evolving requirements.

### Contributing Factors

We define a cluster’s capacity in terms of the following variables:

Node size —Each Expressway virtual machine has a “VM size” that is determined at install time by the resources assigned to the VM. The Expressway installation guides describe those requirements. If you already have an Expressway, you can read the VM size on the Status > System information page of the Expressway interface.

Node count —An Expressway cluster may have between one and six nodes. They must be the same node size and run the same version of software.

Service continuity strategy —The services use strategies to ensure
                        continuous service to users. Calendar Service and Message Service use a
                        failover strategy.

The strategies are detailed in the Service Continuity Strategies and Scale
                            of Dedicated Clusters table.

Coresidency —When the connectors share an Expressway cluster, the resources available to each service are significantly lower as compared with the dedicated cluster.

There may also be other Expressway-based services on your connector host, like business to business calling (B2B) or Mobile and Remote Access (MRA). In the limited scenarios where this type of coresidency is supported, the scale numbers we document here are constrained to what we have tested. Beyond what is described in this article, the connector host Expressway cluster must not be shared with other services; this is unsupported.

Service-specific limitations —For example, the Calendar Connector is intended primarily for Microsoft Exchange users and supports a limited number of Office 365 users.

### Calculations for Dedicated Expressway Clusters

We set a hard limit to the number of service users that a dedicated single Expressway can manage (a “cluster of one”), based on evidence that we gather in testing and trials.

We use the service continuity algorithms to extrapolate the single node numbers to multiple node clusters, as explained in the following table. If you want the results without the explanation, see:

Calendar Service Scale

Message Service Scale

Compare

Hybrid Calendar Service

Hybrid Message Service

1. Model

Failover model

Failover model

2. Description

We assign each user to one node in the cluster. This spreads the
                                    users across all nodes.

If a node goes down, we recreate the user assignments from that
                                    node on the other nodes.

When the node comes back up, we rebalance user assignments across
                                    all active nodes.

We assign each user to one node in the cluster. This spreads the
                                    users across all nodes.

If a node goes down, we recreate the user assignments from that
                                    node on the other nodes.

When the node comes back up, we rebalance user assignments across
                                    all active nodes.

3. Formula

U calN = (N-1) * U cal1

U msgN = (N-1) * U msg1

4. Definitions

Where:

U calN is the cluster of N capacity for Calendar
                                    Service users

N is the node count

U cal1 is the single node capacity for Calendar Service
                                    users

Where:

U msgN is the cluster of N capacity for Message Service
                                    users

N is the node count

U msg1 is the single node capacity for Message Service
                                    users

5. Notes

If N=1, there is no failover.

Failover is automatic and mandatory if N>1.

If N=2, the capacity is the same as if N=1, with better
                                    continuity of service.

Scale benefits from N>=3 or by using a larger node size.

If N=1, there is no failover.

Failover is automatic and mandatory if N>1.

If N=2, the capacity is the same as if N=1, with better
                                    continuity of service.

Scale benefits from N>=3 or by using a larger node size.

### Calculations for Shared Expressway Clusters

Our algorithm assumes that coresident connectors proportionately share the resources of a single node. This algorithm conservatively sets the limit for each type of user on the node.

For example, the following table shows the maximum number of users for all the dedicated cases and the coresidency cases on a single, medium Expressway.

10,000

—

Dedicated to Message Service

—

6,500

Shared by Calendar Service and Message Service

4,000

4,000

Shared by Calendar, Call, and Message Services

2,300

2,300

We do not exhaustively list all the coresidency states for all cluster sizes. Instead, you can monitor capacity of your existing Hybrid Services deployment , or use the calculator to plan a new deployment.

The calculator lets you choose connectors, node size, and node count, so you can model your deployment. The remainder of this section explains how it calculates the user numbers from your model.

Just as we did for the dedicated Expressway, we extrapolate the algorithm for shared Expressways to determine user numbers for multiple nodes. The difference from the dedicated cases is that we apply the appropriate service continuity calculation to get the user scale for a particular service on the cluster. We cannot calculate the user scale for the cluster because the cluster hosts competing, user-based, service continuity strategies.

Cluster Purpose

Hybrid Message Service Users for 1,2, and 3 nodes

Dedicated to Message Service

6,500

6,500

13,000

### Additional Contributing Factors

There may be competing demands on the cluster’s resources that will decrease the user capacity. These are the known examples:

Calendar Service —The connector host may also service O365 users. The numbers and calculations shown here assume that only your on-premises Exchange infrastructure provides the Calendar Service. For more on the ‘hybrid’ Calendar Service, we have some numbers and graphs in the Calendar Service section of this article .

Call Processing —The connector host may also process call signalling and media.
                This is effectively a “Business to business” integration between your organization
                and the Webex cloud. This reduces the capacity as described in Coresidency with Other Expressway Solutions .

Monitor Hybrid Service Capacity

You can use Control Hub to view a percentage value of the current user capacity of each of your Hybrid Services Expressway resources. A color bar indicates whether the capacity is within acceptable limits. This view lets you evaluate the health of your hybrid service deployments and guides you as to when you need more Expressways.

Green —Your Expressways are within acceptable capacity limits. (1%–60%)

Amber —You have enough Expressways but you are close to reaching capacity limits. (61%–90%)

Red —You don't have enough Expressways and must add more. (91% and up)

If your Expressways are in a resource group, the capacity indicator appears under a filtered view of the clusters in the resource group.

For deployments without resource groups (default):

From the customer view in https://admin.webex.com , go to Services > Hybrid , and then scroll to the hybrid service cards to view the
                            percentage of capacity used on the Expressway resources for each
                            service.

For deployments with resource groups:

From the customer view in https://admin.webex.com , go to Services > Hybrid , scroll to the hybrid service cards, and then under Resources click View All .

The capacity bar only indicates the capacity for clusters outside of
                                resource groups. If all clusters are part of one or more resource
                                groups or the service has no clusters that are configured, the
                                capacity bar is not displayed.

If the capacity value is N/A , choose a resource group from Filter to review resource groups & capacity .

The value updates to show the percentage of capacity that is used for clusters in that resource group and color-coding to indicate the health.

Things to Keep in Mind

The cluster capacity varies depending on the node size, the number of nodes
                        in the Expressway cluster, how many services are running on the cluster, and
                        the high availability or failover strategy. For more information, see the
                        individual  Calendar and Message scale sections.

Coresidency reduces the user scale for existing services; the capacity algorithm assumes that every user is using all services.

We recommend coresidency when you're trying out multiple services, or if you have a small-scale deployment. For services in production, or for large-scale deployments, we recommend that you run the different hybrid services on dedicated Expressway clusters.

What to do next

To add more Expressways for Hybrid Services, use the deployment guide steps for registering connector hosts to the cloud and adding them to existing clusters:

Hybrid Calendar Service

Hybrid Message Service

Calendar Service Scale

An Expressway cluster's capacity for servicing Hybrid Calendar Service users depends on the size of the constituent Expressway-C nodes, the number of nodes in the Expressway cluster, and the service continuity strategy.

The following table shows the maximum number of users on a single Expressway dedicated to the different Hybrid Calendar environments.

Calendar Environment

Small Expressway

Medium Expressway

Large Expressway

On-premises Exchange only

5,000 users

10,000 users

15,000 users

Office 365 only*

1,000 users

1,000 users

1,000 users

On-premises Exchange and Office 365* (Hybrid Exchange deployments)

Max of 1,000 Office 365 users out of 5,000 total users

Max of 1,000 Office 365 users out of 10,000 total users

Max of 1,000 Office 365 users out of 15,000 total users

* To avoid this scale limitation, we recommend that you use the cloud-based Calendar Service instead of the on-premises connector. For the Expressway-based Hybrid Calendar, the limitation of Office 365 user capacity to 1,000 per cluster is independent of the cluster's node size or count; this limitation derives from interaction with the Microsoft cloud service and not from the scale of the on-premises Expressway deployment.

Note that the user capacity is the same for a cluster of one node and for a cluster of two nodes. This is because Calendar Service uses failover to improve service continuity. All users are assigned to one node when there are two nodes in the cluster; the other node is a redundant backup. See Planning Expressway Cluster Capacity for Hybrid Services Users for a detailed explanation.

An Expressway cluster's capacity for Hybrid Calendar Service users primarily depends on the size and number of nodes in the cluster, and the service continuity strategy. The following table shows the maximum total user capacity that the cluster can handle as you increase nodes (or the node OVA size) on a single dedicated cluster.

In a hybrid Exchange environment with Office 365 users, there is a limit of 1,000 Office 365 users per cluster, independent of the cluster's node count or size. The cloud-based service is the preferred method of handling Office 365 users. We highly recommend that you only temporarily host Office 365 users on Expressway.

This limitation derives from interaction with the Microsoft cloud service and not from the scale of the on-premises Expressway deployment. As an example, if you have a single small Expressway node, your capacity is limited to 1,000 Office 365 users and 4,000 Microsoft Exchange users. If you have a cluster of 6 small nodes, your capacity is limited to 1,000 Office 365 users plus 24,000 Microsoft Exchange users.

Expressway Node Size

1 or 2 Nodes*

3 Nodes

4 Nodes

5 Nodes

6 Nodes

1. Small

5K

10K

15K

20K

25K

2. Medium

10K

20K

30K

40K

50K

3. Large

15K

30K

45K

60K

75K

* Note that the user capacity is the same for a cluster of one node and for a cluster of two nodes. This is because Calendar Service uses fail-over to improve service continuity. All users are assigned to one node when there are two nodes in the cluster; the other node is a redundant backup. See Planning Expressway Cluster Capacity for Hybrid Services Users for a detailed explanation.

### User Assignment Across Hosts and Clusters

By default, the Hybrid Calendar Service automatically assigns and distributes users evenly across all Calendar Connectors in a cluster. The assignment is dynamic based on availability, and the administrator has no control over which particular node an individual user is assigned to.

In cases where an organization has more than one cluster, user distribution is based on multiple factors including cluster availability, current assignment (to reduce flapping during failure recovery), and a sort order based on highest cluster preference. The administrator also has the ability to assign a user or group of users to a resource group. Resource groups are cluster specific, so they allow administrators to constrain assignment of particular sets of users to a specific cluster.

With this basic understanding of user assignment and taking into account the Expressway Calendar Connector prerequisites , an administrator can deploy the appropriate capacity at scale for their organization. Let's look at an example organization of 126,000 users to be enabled for the Hybrid Calendar Service, given the following parameters:

Expressway clusters of 6 nodes using the large OVA template (limit of 15,000 users per node)

No resource groups required

The capacity formula for a single cluster, U calN = (N-1) * U cal1 where N=6 and U cal1 =15,000 (using the large OVA template) yields a maximum of 75,000 users. With 126,000 total users in the calendar service deployment, multiple Calendar Connector host clusters are required. Users would be equally distributed as shown in the following figure:

The Hybrid Calendar Service adds users to cluster A first until the cluster reaches the 75,000 user capacity, and then assigns the remaining users to cluster B. The users are randomly and equally distributed across all nodes within the cluster. This example shows an equal distribution of Calendar Connector host nodes (within each of the two clusters) across data centers RTP & PDX. Each node uses the same OVA template and the follows the Expressway high availability guidelines . The Calendar Connector uses the Expressway clustering logic in a 5+1 redundancy model to allow for high availability scenarios.

With all users assigned to a Calendar Connector, let's now examine what happens when there is a failure in a cluster. The next figure shows a single node failure. Users who were assigned to the failed node, 5A in cluster A, have now failed over to the remaining nodes in that cluster. A single node capacity allows for up to 15,000 users and each node remaining in cluster A adds 2500 users who were originally assigned on node 5A. There is no change or impact to cluster B or to the users assigned on cluster B.

Cluster A is still at maximum capacity, and each of the operational nodes in the cluster is now at maximum capacity, 15,000 users/node. Therefore, if another node in cluster A becomes unavailable, such as node 4A in the next figure, cluster B will now be responsible for picking up the additional user load. The 15,000 users from node 4A are now reassigned to cluster B and equally distributed across all the nodes within cluster B.

When nodes 4A and 5A recover, the users on cluster A will be redistributed across the nodes in the cluster. The users that failed over to cluster B remain on cluster B during this recovery phase to avoid unnecessary user assignments between clusters, as shown in the next figure.

A key item to be aware of in planning a large scale Hybrid Calendar Service deployment is understanding the impact of a failure if it were to occur in the deployment. If we use the same 126,000 user deployment but happen to lose an entire data center, there is a potential for users not being assigned to a Calendar Connector node. To prevent a service outage in this type of scenario, the customer would need a third cluster to redistribute and handle the impacted users.

Message Service Scale

An Expressway cluster's capacity for servicing Hybrid Message users depends on the size of the constituent Expressway nodes, the number of nodes in the cluster, and the service continuity strategy.

The following table shows the maximum number of users on a single Expressway that is used for the Hybrid Message.

Small Expressway

Medium Expressway

Large Expressway

5,000 users

6,500 users

15,000 users

The user numbers are the same for a cluster of one node and for a cluster of two nodes. This is because Message Service uses failover to improve service continuity. Users are distributed evenly across the multiple nodes in the cluster: if one node fails, that node's users are assigned to the other nodes.

Hybrid Services Coresidency

This topic is about sharing a connector host Expressway between the connectors for
                multiple Hybrid Services, including Calendar Service and Message Service. The
                connector host is not shared with other Expressway-based solutions such as MRA and
                B2B.

The connector host cluster's capacity depends on the size of the constituent Expressway nodes, the number of nodes, the connectors that are running on the cluster, and the service continuity strategy. See Planning Expressway Cluster Capacity for Hybrid Services Users for a detailed explanation of these factors.

There is also a calculator for you to model different connector host clusters and see how many users of each service your proposed cluster can support.

In general, we recommend coresidency only for smaller size deployments of up to two nodes. If your deployment exceeds the capacity of a pair of nodes, you should move connectors to Expressway clusters that are dedicated to each specific hybrid service.

### Example: Connector Host Scale with Three Coresident Connectors

The following table shows an example of scale and coresidency. It gives the maximum number of users per cluster , for each service, with different specifications of the connector host cluster. The cluster is shared between Hybrid Calendar (using your on-premises Exchange), hybrid call , and Hybrid Message Service.

Service

Two Small Nodes

Two Medium Nodes

Two Large Nodes

Calendar Service users

1,300

2,300

3,000

Message Service users

1,300

2,300

3,000

Coresidency with Other Expressway Solutions

### Introduction

This topic is about sharing a connector host Expressway with other Expressway-based solutions. When you choose to host connectors on an Expressway that you are using for other purposes, the following important caveats apply:

We cannot support the scalability model that applies to a dedicated connector host Expressway. The user numbers that you derive from reading the other topics in this article, or using the calculator, do not apply when the connector host is shared with other Expressway services.

The combinations of Expressway-based services and hybrid services connectors described in this article, and the associated user numbers, are the only supported scenarios. We have not tested other scenarios, and you cannot expect them to work in your environment.

### Expressway-based Calendar Service with Call Connector and Call Service Traversal

In this scenario, a two node Expressway cluster Hybrid Calendar connectors. The cluster is also doing call traversal for other Cisco calling
                solutions (SIP signaling and media).

The table shows the different calendar environments that you can use with the Expressway-based connector. The Expressway-based Calendar connector is not supported on clusters with more than two nodes. Use the cloud-based connector for greater scale with Office 365 (see Calendar Service Scale ).

Service

Two Small Node Cluster

Two Medium Node Cluster

Two Large Node Cluster

Calendar Service

On-premises Exchange

500 users

1,000 users

1,000 users

Office 365 †

500 users

1,000 users

1,000 users

On-premises Exchange and Office 365 (Hybrid Exchange deployments)

Max 500 users for both

Max 1,000 users for both

Max 1,000 users for both

Call Traversal

200 audio sessions

100 video sessions

200 audio sessions

100 video sessions

1,000 audio sessions

500 video sessions

† To avoid this scale limitation, we recommend that you use the cloud-based Calendar Service instead of the on-premises connector. For the Expressway-based Hybrid Calendar, the limitation of Office 365 user capacity to 1,000 per cluster is independent of the cluster's node size or count; this limitation derives from interaction with the Microsoft cloud service and not from the scale of the on-premises Expressway deployment.

### Calendar with Mobile and Remote Access

In this scenario, an MRA cluster of one or two small Expressway VMs is hosting the
                Calendar Connector. This scenario assumes the cluster is only used for MRA and the
                two connectors. The cluster is limited to one or two small nodes.

Expressway Purpose

Cluster of One Small Expressway-C

Cluster of Two Small  Expressway-Cs

Calendar Service users (On-premises connector to Exchange)

500 users

500 users

Mobile and Remote Access users

100

100

| Expressway Node Size | Hybrid Calendar Service Scale | Hybrid Message Service Scale |
|---|---|---|
| 1. Small | 5000 | 5000 |
| 2. Medium | 10000 | 6500 |
| 3. Large | 15000 | 15000 |

| Compare | Hybrid Calendar Service | Hybrid Message Service |
|---|---|---|
| 1. Model | Failover model | Failover model |
| 2. Description | We assign each user to one node in the cluster. This spreads the
                                    users across all nodes. If a node goes down, we recreate the user assignments from that
                                    node on the other nodes. When the node comes back up, we rebalance user assignments across
                                    all active nodes. | We assign each user to one node in the cluster. This spreads the
                                    users across all nodes. If a node goes down, we recreate the user assignments from that
                                    node on the other nodes. When the node comes back up, we rebalance user assignments across
                                    all active nodes. |
| 3. Formula | U calN = (N-1) * U cal1 | U msgN = (N-1) * U msg1 |
| 4. Definitions | Where: U calN is the cluster of N capacity for Calendar
                                    Service users N is the node count U cal1 is the single node capacity for Calendar Service
                                    users | Where: U msgN is the cluster of N capacity for Message Service
                                    users N is the node count U msg1 is the single node capacity for Message Service
                                    users |
| 5. Notes | If N=1, there is no failover. Failover is automatic and mandatory if N>1. If N=2, the capacity is the same as if N=1, with better
                                    continuity of service. Scale benefits from N>=3 or by using a larger node size. | If N=1, there is no failover. Failover is automatic and mandatory if N>1. If N=2, the capacity is the same as if N=1, with better
                                    continuity of service. Scale benefits from N>=3 or by using a larger node size. |

| Expressway Purpose | Calendar Service Users | Message Service Users |
|---|---|---|
|  |  |  |
| Dedicated to Calendar Service | 10,000 | — |
| Dedicated to Message Service | — | 6,500 |
| Shared by Calendar Service and Message Service | 4,000 | 4,000 |
| Shared by Calendar, Call, and Message Services | 2,300 | 2,300 |

| Cluster Purpose | Hybrid Message Service Users for 1,2, and 3 nodes |
|---|---|
| Dedicated to Message Service | 6,500 | 6,500 | 13,000 |

| Calendar Environment | Small Expressway | Medium Expressway | Large Expressway |
|---|---|---|---|
| On-premises Exchange only | 5,000 users | 10,000 users | 15,000 users |
| Office 365 only* | 1,000 users | 1,000 users | 1,000 users |
| On-premises Exchange and Office 365* (Hybrid Exchange deployments) | Max of 1,000 Office 365 users out of 5,000 total users | Max of 1,000 Office 365 users out of 10,000 total users | Max of 1,000 Office 365 users out of 15,000 total users |

| Expressway Node Size | 1 or 2 Nodes* | 3 Nodes | 4 Nodes | 5 Nodes | 6 Nodes |
|---|---|---|---|---|---|
| 1. Small | 5K | 10K | 15K | 20K | 25K |
| 2. Medium | 10K | 20K | 30K | 40K | 50K |
| 3. Large | 15K | 30K | 45K | 60K | 75K |

| Small Expressway | Medium Expressway | Large Expressway |
|---|---|---|
| 5,000 users | 6,500 users | 15,000 users |

| Service | Two Small Nodes | Two Medium Nodes | Two Large Nodes |
|---|---|---|---|
| Calendar Service users | 1,300 | 2,300 | 3,000 |
| Message Service users | 1,300 | 2,300 | 3,000 |

| Service | Two Small Node Cluster | Two Medium Node Cluster | Two Large Node Cluster |
|---|---|---|---|
| Calendar Service | On-premises Exchange | 500 users | 1,000 users | 1,000 users |
| Office 365 † | 500 users | 1,000 users | 1,000 users |
| On-premises Exchange and Office 365 (Hybrid Exchange deployments) | Max 500 users for both | Max 1,000 users for both | Max 1,000 users for both |
| Call Traversal | 200 audio sessions 100 video sessions | 200 audio sessions 100 video sessions | 1,000 audio sessions 500 video sessions |

| Expressway Purpose | Cluster of One Small Expressway-C | Cluster of Two Small  Expressway-Cs |
|---|---|---|
| Calendar Service users (On-premises connector to Exchange) | 500 users | 500 users |
| Mobile and Remote Access users | 100 | 100 |