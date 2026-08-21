---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-213261-understandin-cb753a3ff7
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/213261-understanding-media-resource-groups-and.html
retrieved_at: 2026-08-21T13:57:18.399171+00:00
---

Configure Media Resource Groups and Group Lists

# Configure Media Resource Groups and Group Lists

Updated: April 26, 2018

Document ID: 213261

Contents

## Contents

## Introduction

This document describes how Media Resource Groups (MRGs) and Media Resource Group Lists (MRGLs) are now used in order to allow an administrator to allocate media resources to particular devices. The most common use of MRGs and MRGLs is to restrict media resource usage on a geographic basis.

For example, if you have conference resources at a remote location, you can create an MRGL for the IP phones at the remote location that only allows them to access their local conference bridge resources. This ensures that the conference calls that an IP phone creates at the remote location do not have to use WAN bandwidth for conferencing within the same site. You can also configure the MRGL to have secondary, tertiary resources (and so forth), so that if the conference bridge at a remote location is out of resources or is unavailable, resources from another site can be used as a backup. You can use MRGs and MRGLs for any other media resource (for instance, Music On Hold Servers (MOH), and Transcoding resources).

## Prerequisites

### Requirements

There are no specific requirements for this document .

### Components Used

The information in this document is based on these software  versions:

- CUCM version 11.5.1.12018-1

- Cisco CallManager 11.x and later

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Media Resource Groups and Media Resource Group Lists

An MRGL provides a prioritized grouping of MRGs. An application selects the required media resource, such as an MOH server, from among the available media resources based on the priority order defined in an MRGL.

Media resource management provides access to media resources for all Cisco CallManagers in a cluster. Every Cisco CallManager contains a software component called a Media Resource Manager. The Media Resource Manager locates the necessary media resource in order to connect media streams to complete a feature (for example, MOH, Conferencing, and so forth). The Cisco CallManager uses the Skinny protocol in order to interface to these media resources.

### The Media Resource Manager

The Media Resource Manager manages these media resource types:

- MOH server.

- Unicast conference bridge (CFB).

- Media streaming application server (software media termination point).

- Transcoder (XCODE).

These reasons explain why resources are shared:

- In order to allow both hardware and software devices to coexist within a Cisco CallManager.

- In order to enable Cisco CallManager to share and access resources available within the cluster.

- In order to enable Cisco CallManager to perform load distribution within a group of similar resources.

- In order to enable Cisco CallManager to allocate resources based on user preferences.

Initialization of Cisco CallManager creates a Media Resource Manager. Each Media Termination Point, MOH, Transcoder, and Conference Bridge device defined in the database registers with the Media Resource Manager. The Media Resource Manager obtains a list of provisioned devices from the database and constructs and maintains a table in order to track these resources. The Media Resource Manager uses this table in order to validate registered devices. The Media Resource Manager keeps track of the total devices available in the system. The Media Resource Manager also tracks the devices that have available resources.

When a media device registers, Cisco CallManager creates a controller in order to control this device. After the device is validated, the system advertises its resources throughout the cluster. This mechanism allows the resource to be shared throughout the cluster.

Resource reservation takes place based on search criteria. The given criteria provide the resource type and the MRGL. When the Cisco CallManager no longer needs the resource, resource deallocation occurs. Cisco CallManager updates and synchronizes the resource table after each allocation and deallocation.

### Media Resource Manager Interfaces

The Media Resource Manager interfaces with these major components:

- Call Control

- Media Control

- Media Termination Point Control

- Unicast Bridge Control

- MOH Control

The Call Control software component performs call processing, this includes setup and tear down of connections. Call Control interacts with the feature layer in order to provide services like transfer, hold, conference, and so forth. Call Control interfaces with the Media Resource Manager when it needs to locate a resource in order to set up a conference call and/or MOH features.

The Media Control software component manages the creation and teardown of media streams for the endpoint. Whenever a request for media to be connected between devices is received, Media Control sets up the proper interface in order to establish a stream, which depends on the type of endpoint.

The media layer interfaces with the Media Resource Manager when it needs to locate a resource in order to set up a Media Termination Point. Media Termination Point Control provides the capability to bridge an incoming H.245 stream to an outgoing H.245 stream. Media Termination Point maintains an H.245 session with an H.323 endpoint when the streaming from its connected endpoint stops. Media Termination Point currently supports only codec G.711 and can also transcode a-law to mu-law.

For each Media Termination Point device defined in the database, Cisco CallManager creates a Media Termination Point Control process. This Media Termination Point Control process registers with the Media Resource Manager when it initializes. The Media Resource Manager keeps track of these Media Termination Point resources and advertises their availability throughout the cluster.

Unicast Bridge Control provides the capability to mix a set of incoming unicast streams into a set of composite output streams. Unicast Bridge provides resources in order to implement ad hoc and meet-me conferencing in the Cisco CallManager. For each Unicast Bridge device defined in the database, Cisco CallManager creates a Unicast Control Process. This Unicast Control Process registers with the Media Resource Manager when it initializes. The Media Resource Manager tracks Unicast stream resources and advertises their availability throughout the cluster.

MOH provides the capability to redirect a party on hold to an audio server. For each MOH server device defined in the database, Cisco CallManager creates an MOH control process. This MOH Control Process registers with the Media Resource Manager when it initializes. The Media Resource Manager tracks MOH resources and advertises their availability throughout the cluster. MOH supports both Unicast and Multicast audio sources.

## Configure

### Network Diagram

Cisco CallManager uses the MRGL concept in order to select resources. The selection depends on the geographical assignment of the resources

- MRGs are logical groupings of media resources. A single MRG can contain hardware conference resources, software conference resources, transcoder resources, MOH servers, and software Media Termination Points. An MRG has no user-defined order. All resources in an MRG are considered equal. Therefore, Cisco CallManager loads share between resources of each type in one MRG.

- When transcoding is used with a conference, the transcoder is selected based on the MRGL of the Conference Bridge.

Note : You cannot explicitly configure an MRGL for a Conference Bridge. Therefore, the MRGL is taken first from the Device Pool, and then from the MRG default pool.

- When a phone is put on hold, the MRGL of the device that it put on hold (could be a gateway for offnet calls) determines which MOH server is used to play music to the held device.

- Conference Bridges are chosen based on the MRGL of the conference controller (the party that initiates the conference).

- If a call goes out through a gateway, and Media Termination Point (MTP) is required. The MRGL of the gateway is then used to select the MTP.

- MRGLs are an ordered list of MRGs. All resources in one MRG must be exhausted before Cisco CallManager attempts to use a media resource from another MRG in the same MRGL.

- MRGLs can be associated on a per-device basis, which means that you can give specific devices access to media resources on an individual basis. A second MRGL can also be configured at the device pool level.

- If a device has an MRGL configured at the device pool level as well as on the device itself, the MRGL configured at the device level is searched first, followed by the MRGL on the device pool.

- The last MRGL is the default MRGL. A media resource that is not assigned to an MRG is automatically assigned to the default MRGL. The default MRGL is always searched and it is the last resort if no resources are available in the device-based MRGL and the device pool MRGL or if no MRGLs are configured at any level.

### Configurations

Complete these steps in order to configure your MRG/MRGLs after you have your media resources configured within Cisco CallManager.

Login to the Cisco CallManager Administration page and select Media Resources > Media Resource Group , as shown in the image.

Select Add a New Media Resource Group .

Enter a name for the MRGs. Select the resources that you want to associate with this MRG and then click Insert .

Create another MRG for the remote site resources.

Select all the necessary resources and click Insert .

Navigate Media Resources > Media Resource Group List in order to create an MRGL to associate the MRG(s).

Click Add a New Media Resource Group List .

Here 4 MRGLs are created in this example.

- MRGL1 for the main site resources

- MRGL2 for the remote site resources.

- MRGl3 for redundancy if the media resources are not available at this site, they failover to the remote site resources so that calls do not fail.

- MRGl4 for redundancy if the media resources are not available at the remote site, they failover to the main site resources so that calls do not fail.

When you perform a search on Media Resource Group Lists , you see all four lists that are created.

Associate the MRGL with either the Device Pool for all users or through configuration on the device itself.

The next example shows the configuration of the MRGL on the device itself. When an MRGL is configured directly on the device, that MRGL takes precedence over the Device Pool configuration.

## Verify

There is no specific verification. You can just check on the MRG and MRGL page if the configuration is correct or not as per required

## Troubleshoot

### Problem 1

This error message appears in the Event Viewer:

Error: "ConferenceNoMoreResourcesAvailable - No more Conference Resources available"

Solution:

Complete these steps in order to check if all the hardware conference bridges are registered with the Cisco CallManager.

- Go to the CallManager Admin page and choose Media Resources > Conference Bridge .

- Click Find and check if all the bridges are listed.

Note: Distribute Media Resources in an optimal manner under the Device Pool configuration.

### Problem 2

Fast Busy is Received When Remote Location is called

When you call the IP Contact Center (IPCC) remote location, the phone rings at the remote location, but when the user picks up the phone, a fast busy signal is received.

Solution:

In order to resolve the issue, create separate Media Resource Groups (MRGs) for the software transcoder resources and hardware transcoder resources and make sure that the hardware transcoder resource MRG has first priority in the Media Resource Group List (MRGL).