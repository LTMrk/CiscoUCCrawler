---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su2-design-guide-uccx-b-1251s-c751d38117
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su2/design/guide/uccx_b_1251su2_solution-design-guide/uccx_b_1252solution-design-gude_chapter_010.html
retrieved_at: 2026-08-16T21:06:59.970247+00:00
---

Solution Design Guide for Cisco Unified Contact Center Express, Release 12.5(1) SU2

# Solution Design Guide for Cisco Unified Contact Center Express, Release 12.5(1) SU2

Updated: April 11, 2022

Chapter: Unified CCX Reference Designs

## Chapter: Unified CCX Reference Designs

# Unified CCX Reference Designs

## Introduction to the Unified CCX Solution Reference Designs

This chapter discusses the reference designs that are available for Unified CCX. Use the Cisco Collaboration Sizing Tool to
                              help you determine the number and types of servers required for any supported deployment model and call processing requirements.
                              Before using that tool, it is necessary to have an understanding of what deployment model you desire.

Cisco Unified Intelligence Center, Cisco Finesse, and Cloud Connect are deployed on the same Virtual Machine (VM) with Unified
                              CCX and support all the Unified CCX reference designs.

The following table depicts the reference designs that are supported in Unified CCX. These models have no bearing on which
                              specific server model is used. The Cisco Collaboration Sizing Tool identifies the minimum server model required. This chapter
                              provides general rules for design and considerations and limitations for each of these reference designs. This information
                              allows a Unified CCX system planner or designer to understand what other similar reference designs are supported. This also
                              helps to understand how to determine the best solution for a given set of requirements.

Unified CCX Reference Design

Unified CCX Components on Server 1

Unified CCX Components on Server 2

Single-Server Non-High Availability Deployment Model—Unified Communication Manager Integration

Engine, Database, Monitoring, Reporting, Desktop, Cisco Identity Service components, Cloud Connect components.

—

Two-Server High Availability Deployment Model—Unified Communication Manager Integration

Engine, Database, Monitoring, Reporting, Desktop, Cisco Identity Service components, Cloud Connect components.

Engine, Database, Monitoring, Reporting, Desktop, Cisco Identity Service components, Cloud Connect components.

Unified CCX deployment model integrated with Unified CME is not supported in 9.0(1) and higher versions.

For hardware requirements, see Cisco Unified CCX Virtualization
                                             Information at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-contact-center-express.html .

The following figure depicts the deployment when integrating Unified CCX with Unified Communications Manager. In this deployment,
                              optional Unified CCX components shown with an asterisk (*) can be added. These components are:

Cisco Unified Work Force Management and Quality Manager .

ASR and TTS can be added in Unified CCX integrated with Unified Communication Manager. ASR and TTS software is not provided
                                          by Cisco. This software must be purchased from other vendors. These vendors can provide design and server sizing requirements
                                          for their software.

## Unified CCX
                        	 General Rules for Design

The following rules apply when designing a Unified CCX deployment:

When deploying for high availability (HA), the Unified CCX servers can be located in the same campus LAN to provide server
                                    redundancy. The Cisco Unified CCX servers can also be located in different sites separated by WAN to provide spatial redundancy.

For HA over LAN deployment, heartbeats are sent every one second and failover occurs if three consecutive heartbeats are missed.
                                          For HA over WAN deployment, heartbeats are sent every second and failover occurs if ten consecutive heartbeats are missed.
                                          These values are not configurable.

You can locate
                                    				the Unified Communications Manager servers that run CTI Managers with which
                                    				Unified CCX communicates in the same campus LAN. In Unified CCX servers that
                                    				are deployed over WAN, for better site redundancy, deploy local Unified
                                    				Communications Manager server at both sites.

The Recording
                                    				component must be redundant, if recording is used in a high availability
                                    				deployment.

All agents for
                                    				a Unified CCX deployment must be using phones that register to the same Unified
                                    				CM cluster. Calls can be received from devices and callers on another Unified
                                    				CM cluster (using intercluster trunks).

Unified CCX
                                    				software versions must be the same for both the master and standby nodes in a
                                    				high availability deployment.

Unified CCX solution works with a combination of software and hardware components, providing an open and flexible environment
                                    for customers to run complex scripts, custom codes, documents, and so on. Overloading any of the software and hardware components
                                    such as virtual memory and CPU could impact the solution performance. Review and optimize the scripts, custom codes, and documents
                                    before they are loaded to the production setup. Also constantly monitor the system component and hardware attributes like
                                    disk space and CPU utilization.

When deploying Quality Management and Workforce Management with Unified CCX, consider the following guidelines:

Unified CCX does not support the use of third-party applications (for example, using TAPI) to control its devices.

For more deployment information about Workforce Management and Quality Management , refer to the Cisco Webex WFO User Guide for Cloud Deployments available at here:

https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/workforce_optimization/Webex_WFO/webex-wfo-user-guide.pdf .

Existing Unified CCX customers with WFO licenses will have to remain on classic licensing as WFO licenses are not supported
                                                in Smart Licensing. However, you can move Unified CCX licenses to Smart Licensing and existing Cisco WFO licenses to Cisco
                                                SolutionsPlus. For more information, contact Cisco Support.

## Reference
                        	 Designs

The following
                           		sections describe the Unified CCX Reference Designs.

### Single-Server
                           	 Non-High Availability Reference Design

Unified
                                 		  CM integration with Unified CCX on a single-server nonhigh availability is for
                                 		  small deployments. This reference design places a single instance of all the
                                 		  Unified CCX software components on the same server and uses Informix Dynamic
                                 		  Server as the database server.

This
                                 		  reference design allows the Unified CCX Engine to fail over to a backup CTI
                                 		  Manager if the primary CTI Manager fails. CTI ports and CTI route points should
                                 		  be grouped into device pools that have the same primary and secondary server
                                 		  list as those used for JTAPI communications with the CTI Managers.

### Two-Server High Availability Reference Design

This reference design can support silent monitoring and recording for agents at any WAN-connected site by using desktop monitoring.
                                 (See the Unified CCX Compatibility related information located at: http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html for a list of phones that support desktop monitoring.) It can also support SPAN port monitoring for agents on the VLAN segment
                                 local to Unified CCX server. This reference design provides redundancy for both recording and silent monitoring for all agents
                                 using desktop monitoring (regardless of location) or agents on the local VLAN using SPAN port monitoring. Silent monitoring
                                 and recording are not possible for agents who are using the Cisco Finesse IP Phone Agent at remote sites. Similarly, silent
                                 monitoring and recording are not possible for agents at remote sites who are using phones that do not support desktop monitoring.

This reference design allows either Unified CCX Engine component to fail over to a backup CTI Manager if the primary server
                                 fails. CTI Ports and CTI Route Points should be grouped into device pools that have the same primary and secondary server
                                 list as that used for JTAPI communications to the CTI Managers.

In HA deployments, historical data comes from the database located in the standby engine node. A higher number of historical
                                             reporting sessions during operating hours is supported for HA deployments.

## Other Design Considerations

Consider the following when designing your Unified CCX system:

High availability requires additional disk space, so historical call reporting capacity may be reduced. Historical call reporting
                                    capacity also depends upon BHCC, hours of operation per day, and days of operation per week.

G.711 call recording requires about 1 MB per minute. G.729 call recording requires about 256 KB per minute.

The following categories of data use hard disk space:

Operating system files, Unified CCX software, and Informix Database Management software

Unified CCX logs

The Unified CCX database (comprised of 4 data stores)

The Unified CM sizing tools assume devices are evenly distributed across all servers. CTI route points are configured as part
                                    of a device pool in the Cisco Unified Communications Manager Server as the primary CTI Manager being used; it may be required
                                    to run the Cisco Unified Communications Manager sizing tool on a per-location or per-server basis.

The Unified CM QSIG (Q Signaling) path replacement feature is not supported for Unified CCX calls.

Unified CM Forced Authorization Codes and Client Matter Codes should be turned off for all route patterns in the Unified
                                    CM cluster that are used by Unified CCX. Enabling these features for route patterns that are not used by Unified CCX does
                                    not affect Unified CCX.

For a list of unsupported features in Unified CM with Unified CCX, refer to the current release notes for Unified CCX.

Unified CCX supports different sets of Finesse IP Phones as agent devices on the Unified CM and Unified CM platform; not
                                    all agent devices can be used as Finesse IP Phone Agent. For a complete list of supported agent devices, see the Unified CCX
                                    Compatibility related information located at: http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html .

Finesse allows each agent to choose and set a language from the language selector drop-down list on the sign-in page.

An agent using Cisco Finesse Agent Desktop can log in using Extension Mobility but the agent phone must be in the Unified
                                    CM cluster that is used by Unified CCX.

Sometimes new releases of Unified CM will not support Unified CCX immediately at Unified CM first customer ship (FCS) time.
                                    Some organizations may be early adopters of new Unified CM releases and may be delayed from migrating to new Unified CM releases
                                    and using new Unified CM features if Unified CCX is installed with that same Unified CM cluster. Therefore, in some situations,
                                    it makes sense to have a separate Unified CM cluster for Unified CCX.

Cisco Jabber runs in two modes: Deskphone Mode and Softphone Mode. Unified CCX only supports Cisco Jabber as an agent device
                                    in Softphone Mode.

Video is now supported if you are using Cisco Jabber as an agent phone. The agent desktop where Jabber is used for video should
                                    comply to the Cisco Jabber hardware requirements listed in the Release Notes for Cisco Jabber for Windows , located at: http://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-release-notes-list.html and Release Notes for Cisco Jabber for Mac located at: http://www.cisco.com/c/en/us/support/unified-communications/jabber-mac/products-release-notes-list.html

The following features are not supported if you are using Cisco Jabber as an agent phone:

Extension Mobility

### Mobile and Remote Access

The Cisco Collaboration Edge architecture includes Unified Communications Mobile and Remote Access (MRA) to enable access
                              by devices that are not in the enterprise network. MRA uses Cisco Expressway to provide secure firewall traversal and support
                              for Unified CM registrations. Unified CM can then provide supported devices with call control, provisioning, messaging, and
                              presence services.

For details on Collaboration Edge, see the documentation at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-system/tsd-products-support-series-home.html . For details on Cisco Expressway deployment and configuration, see the documentation at http://www.cisco.com/c/en/us/support/unified-communications/expressway-series/tsd-products-support-series-home.html . See the Compatability Matrix for your solution for details of device support for MRA.

If Unified CCX uses MRA, consider these points:

The connection between the Cisco Finesse client and server is over a VPN, not over the MRA connection.

If you have VPN split-tunneling configured, you can use Jabber with MRA and the Finesse desktop on the same client machine.
                                    See https://www.cisco.com/c/en/us/support/security/anyconnect-secure-mobility-client/products-installation-and-configuration-guides-list.html for Cisco AnyConnect Mobility Client Split-Tunneling configuration.

If VPN split-tunneling is not available, you can run after splitting them onto two clients.

A remote agent who runs Jabber with MRA on one client machine and the Finesse desktop with a VPN connection on a second client
                                          machine.

A remote agent who runs a Jabber softphone on a laptop that is connected over MRA and runs the Finesse desktop as a Xenapp
                                          thin client.

Certain phones do not support Extension Mobility over MRA.

Unified CCX video deployments do not support MRA.

Certain Contact center features like Agent Greeting and Unified CM-based Silent Monitoring that rely on a phone's BiB are
                                    not supported over MRA.

### Multiple Cisco
                           	 Unified CCX Clusters Integrated with a Single Cisco Unified Communications
                           	 Manager Cluster

You can
                                 		  integrate multiple Unified CCX clusters with a single Cisco Unified
                                 		  Communications Manager cluster.

There is no
                                             			 limit to the number of Unified CCX clusters supported with a single Unified CM
                                             			 cluster as long as the combined agent phones, CTI ports, and CTI route points
                                             			 that are utilized by all Unified CCX clusters are used to size Unified CM.

To determine
                                       				if you need more than one CTI Manager, refer to the Cisco
                                          				  Unified Communications Solution Reference Network Design (SRND) ,
                                       				available at http://www.cisco.com/go/ucsrnd.

If your
                                       				deployment requires more than one CTI Manager, you load-balance the Unified CCX
                                       				and other CTI applications across various CTI Managers in the cluster to
                                       				provide maximum resilience, performance, and redundancy.

For additional information on CTI Manager, refer to the Cisco Unified Communications Solution Reference Network Design (SRND) , available at http://www.cisco.com/go/ucsrnd.

If more than
                                       				one Unified CM primary subscriber is required to support your configuration,
                                       				distribute all agents equally among the Unified CM subscriber nodes. This
                                       				configuration assumes that the busy-hour call attempts (BHCA) is uniform across
                                       				all agents.

Each Unified
                                       				CCX cluster is standalone and independent from other Unified CCX clusters.
                                       				There is no communication or synchronization between the Unified CCX clusters.
                                       				Agents should operate using only one Unified CCX cluster.

Unified CM
                                       				Telephony Triggers (CTI Route Points) and CTI ports should be different across
                                       				Unified CCX clusters.

In the list of
                                       				Resources in Unified CCX Administration, each Unified CCX cluster displays all
                                       				the agents in the Cisco Unified Communications Manager cluster, even though the
                                       				agents can operate and log in to another Unified CCX cluster.

This situation
                                       				requires that the Unified CCX Administrator be aware of which resources are
                                       				associated with each cluster. The Unified CCX Administrator can mitigate this
                                       				situation by having a unique naming convention for resources associated with a
                                       				particular Unified CCX cluster.

This
                                       				deployment is not intended to provide Unified CCX redundancy across different
                                       				Unified CCX clusters. If a Unified CCX cluster fails, the agents that operate
                                       				in this cluster cannot operate in other Unified CCX clusters. If another
                                       				Unified CCX cluster is configured to accept the calls that were originally sent
                                       				to the Unified CCX cluster that failed, there will be no report integration
                                       				between the Unified CCX clusters.

This deployment does not change the characteristics and design considerations of each individual Unified CCX cluster. For
                                       example, within a Unified CCX cluster, high availability is still supported.

If more than one Unified CCX cluster is integrated with the same
                                       				Unified CM cluster, all agents belonging to all the Unified CCX clusters are
                                       				visible to administrators of all the Unified CCX clusters. The administrator
                                       				must be aware of the agents belonging to the Unified CCX cluster that the
                                       				administrator manages and configures.

| Unified CCX Reference Design | Unified CCX Components on Server 1 | Unified CCX Components on Server 2 |
|---|---|---|
| Single-Server Non-High Availability Deployment Model—Unified Communication Manager Integration | Engine, Database, Monitoring, Reporting, Desktop, Cisco Identity Service components, Cloud Connect components. | — |
| Two-Server High Availability Deployment Model—Unified Communication Manager Integration | Engine, Database, Monitoring, Reporting, Desktop, Cisco Identity Service components, Cloud Connect components. | Engine, Database, Monitoring, Reporting, Desktop, Cisco Identity Service components, Cloud Connect components. |

| Note | Unified CCX deployment model integrated with Unified CME is not supported in 9.0(1) and higher versions. For hardware requirements, see Cisco Unified CCX Virtualization
                                             Information at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-contact-center-express.html . |
|---|---|

| Note | ASR and TTS can be added in Unified CCX integrated with Unified Communication Manager. ASR and TTS software is not provided
                                          by Cisco. This software must be purchased from other vendors. These vendors can provide design and server sizing requirements
                                          for their software. |
|---|---|

| Note | For HA over LAN deployment, heartbeats are sent every one second and failover occurs if three consecutive heartbeats are missed.
                                          For HA over WAN deployment, heartbeats are sent every second and failover occurs if ten consecutive heartbeats are missed.
                                          These values are not configurable. |
|---|---|

| Note | Existing Unified CCX customers with WFO licenses will have to remain on classic licensing as WFO licenses are not supported
                                                in Smart Licensing. However, you can move Unified CCX licenses to Smart Licensing and existing Cisco WFO licenses to Cisco
                                                SolutionsPlus. For more information, contact Cisco Support. |
|---|---|

| Note | In HA deployments, historical data comes from the database located in the standby engine node. A higher number of historical
                                             reporting sessions during operating hours is supported for HA deployments. |
|---|---|

| Note | There is no
                                             			 limit to the number of Unified CCX clusters supported with a single Unified CM
                                             			 cluster as long as the combined agent phones, CTI ports, and CTI route points
                                             			 that are utilized by all Unified CCX clusters are used to size Unified CM. |
|---|---|