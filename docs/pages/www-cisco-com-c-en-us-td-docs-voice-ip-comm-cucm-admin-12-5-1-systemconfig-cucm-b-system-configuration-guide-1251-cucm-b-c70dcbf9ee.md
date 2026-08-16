---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-c70dcbf9ee
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0111010.html
retrieved_at: 2026-08-16T17:33:36.811348+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Define Media Resources

## Chapter: Define Media Resources

# Define Media Resources

## Media Resource
                        	 Group Overview

Media resource groups define logical groupings of media servers. You can
                           		associate a media resource group with a geographical location or a site, as
                           		desired. You can also form media resource groups to control the usage of
                           		servers or the type of service (unicast or multicast) that is required.

Media resource groups—A logical grouping a media servers.

Media resource group lists—A prioritized list of media resource
                                    			 groups. An application selects the required media resource, such as a music on
                                    			 hold server from the available media resources according to the priority order
                                    			 that you define in a media resource group list. Media resource group lists,
                                    			 which are associated with devices, provide media resource group redundancy.

Conference Bridge (CFB)

Media Termination Point (MTP)

Music On Hold Server (MOH)

Transcoder (XCODE)

Annunciator (ANN)

After you configure media resources and if you have not defined any
                                       		  media resource groups, all media resources belong to the default group, and all
                                       		  media resources are available to all Cisco Unified Communications Manager s within a given
                                       		  cluster.

## Media Resource
                        	 Group List

A media
                              		  resource group list provides a prioritized grouping of media resource groups.
                              		  An application selects the required media resource, such as a music on hold
                              		  server from the available media resources according to the priority order that
                              		  you define in a media resource group List. Media resource group lists, which
                              		  are associated with devices or device pools, provide media resource group
                              		  redundancy.

## Media Resource
                        	 Group Prerequisites

Ensure that Cisco
                                 			 Unified Communications Manager has media resources to provide
                              		  services, such as annunciator, transcoding, conferencing, music on hold, and
                              		  media termination.

## Media Resource
                        	 Group Task Flow

Step 1

Configure Media Resource Groups .

Step 2

Assign Device to a Media Resource Group .

Assign a
                                          				device to a media resource group.

Order of
                                                      				  assigning a device is not significant.

Step 3

Configure Media Resource Group Lists .

Create media
                                          				resource group list to specify a list of prioritized media resource groups.
                                          				Media resource group lists, which are associated with devices or device pools,
                                          				provide media resource group redundancy.

Order of
                                                      				  assigning a device is significant.

Step 4

Assign Media Resource Group to Media Resource Group List .

Assign the
                                          				newly created media resource group to the media resource group list.

Step 5

Assign Media Resources to Device or Device Pool .

Assign the
                                          				existing or newly created media resource group list to a device or a device
                                          				pool.

Step 6

(Optional) Configure Media Resource Redundancy .

Confirm media
                                          				resources redundancy for a scenario when a media resource fails.

### Configure Media Resource Groups

Step 1

From Cisco Unified CM Administration, choose Media Resources > Media Resource Group .

Step 2

Do either of the following:

- Click Find and select an existing media resource group.

- Click Add New to create a new media resource group.

Step 3

Configure the
                                          			 fields in the Media
                                             				Resource Group Configuration window. See the online help about the
                                          			 fields and their configuration options.

Step 4

Enter a Name and Description for the group.

Step 5

From Available Media Resources , select the resources you want to add to this group, and use the arrows to move the resources to Selected Media Resources .

Step 6

(Optional) To use multicast for Music On Hold audio, check the Use Multi-cast for MOH Audio check box.

Step 7

Click Save .

### Assign Device to a
                           	 Media Resource Group

You can assign
                                 		  devices, such as annunciators (ANN), interactive voice responses (IVR),
                                 		  conference bridges (CFB), media termination points (MTP), music on hold (MOH)
                                 		  servers and transcoders to a media resource group. The order is which you
                                 		  assign the devices is not significant.

#### Before you begin

Configure Media Resource Groups .

Step 1

From the Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Media Resource Group .

Step 2

To configure
                                          			 an existing media resource group, Find
                                             				and List Media Resource Group window, specify the appropriate
                                          			 filters and click Find .

Step 3

To configure
                                          			 new media resource group, click Add
                                             				New .

Step 4

From the Available Media Resources field, choose the one or
                                          			 multiple devices and click the down-arrow key.

Step 5

Click Save .

#### What to do next

Configure Media Resource Group Lists .

### Configure Media Resource Group Lists

Step 1

From Cisco Unified CM Administration, choose Media Resources > Media Resource Group List .

Step 2

Do either of the following:

- Click Find and select an existing list.

- Click Add New and create a new list.

Step 3

Enter a Name for the media resource group list.

Step 4

From Available Media Resource Groups , select the groups you want to add, and use the arrows to move them to Selected Media Resource Groups .

Step 5

Click Save .

### Assign Media
                           	 Resource Group to Media Resource Group List

#### Before you begin

Configure Media Resource Group Lists .

Step 1

From the Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Media Resource Group .

Step 2

To configure
                                          			 an existing media resource group, from the Find and List Media Resource Group window,
                                          			 specify the appropriate filters and click Find .

Step 3

From the Available Media Resources list, select one or
                                          			 multiple media resources and click the down arrow key.

Step 4

Click Save .

#### What to do next

Assign Media Resources to Device or Device Pool .

### Assign Media Resources to Device or Device Pool

Step 1

From the Cisco Unified CM Administration, choose Devices > Phone .

- To add media resources to a device pool, choose System > Device Pools .

- To add media resource directly to an endpoint, choose Device > Phone .

Step 2

Click Find and select the device pool or device to which you want to assign these media resources.

Step 3

From the Media Resource Group List drop-down, select a list.

Step 4

Click Save .

Step 5

Click Apply Config to Selected .

### Configure Media Resource Redundancy

Media resource group lists provide media resource redundancy by
                                 		  specifying a prioritized list of media resource groups. An application can
                                 		  select required media resources from among the available ones according to the
                                 		  priority order that is defined in the media resource list.

To configure media resource groups and media resource group lists for redundancy, perform the Configure Media Resource Groups and Media Resource Group List procedures.

## Media Resource Group Interactions and Restrictions

### Media Resource Group Interactions

Feature

Interaction

Call
                                             					 processing

Call
                                             					 processing uses a media resource group list in the device level if you select
                                             					 the media resource group list. If a resource is not found, call processing may
                                             					 retrieve it from the default allocation.

Call
                                             					 processing uses media resource group list in the device pool only if you do not
                                             					 select a media resource group list in the device level. If a resource is not
                                             					 found, call processing may retrieve it from the default allocation.

Annunciator resource support

Cisco
                                             					 Unified Communications Manager provides annunciator resource support to a
                                             					 conference bridge if the media resource group list that contains the
                                             					 annunciator is assigned to the device pool where the conference bridge exists.

Cisco
                                             					 Unified Communications Manager does not provide annunciator resource support
                                             					 for a conference bridge if the media resource group list is assigned directly
                                             					 to the device that controls the conference.

Video
                                             					 conference

To ensure
                                             					 that only a video conference bridge gets used when a user wants to hold a video
                                             					 conference, add the video conference bridge to a media resource group. Add the
                                             					 media resource group to a media resource group list and assign the media
                                             					 resource group list to the device or device pool that will use the video
                                             					 conference bridge.

### Media Resource Group Restrictions

Restriction

Description

Deletion
                                             					 of a media resource group

You cannot
                                             					 delete a media resource group that is assigned to a Media Resource Group List.

Deletion
                                             					 of a transcoder

You cannot
                                             					 delete a transcoder that is assigned to a media resource group.

Deletion
                                             					 of a media resource

You cannot
                                             					 delete a media resource, such as a conference bridge, that is part of a media
                                             					 resource group unless you first remove the resource from the media resource
                                             					 group or you delete the media resource group that contains the media resource.

| Note | After you configure media resources and if you have not defined any
                                       		  media resource groups, all media resources belong to the default group, and all
                                       		  media resources are available to all Cisco Unified Communications Manager s within a given
                                       		  cluster. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Media Resource Groups . | Configure
                                       			 media resource group to define a logical groupings of media servers. |
| Step 2 | Assign Device to a Media Resource Group . | Assign a
                                          				device to a media resource group. Note Order of
                                                      				  assigning a device is not significant. | Note | Order of
                                                      				  assigning a device is not significant. |
| Note | Order of
                                                      				  assigning a device is not significant. |
| Step 3 | Configure Media Resource Group Lists . | Create media
                                          				resource group list to specify a list of prioritized media resource groups.
                                          				Media resource group lists, which are associated with devices or device pools,
                                          				provide media resource group redundancy. Note Order of
                                                      				  assigning a device is significant. | Note | Order of
                                                      				  assigning a device is significant. |
| Note | Order of
                                                      				  assigning a device is significant. |
| Step 4 | Assign Media Resource Group to Media Resource Group List . | Assign the
                                          				newly created media resource group to the media resource group list. |
| Step 5 | Assign Media Resources to Device or Device Pool . | Assign the
                                          				existing or newly created media resource group list to a device or a device
                                          				pool. |
| Step 6 | (Optional) Configure Media Resource Redundancy . | Confirm media
                                          				resources redundancy for a scenario when a media resource fails. |

| Note | Order of
                                                      				  assigning a device is not significant. |
|---|---|

| Note | Order of
                                                      				  assigning a device is significant. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Media Resources > Media Resource Group . |
|---|---|
| Step 2 | Do either of the following: Click Find and select an existing media resource group. Click Add New to create a new media resource group. |
| Step 3 | Configure the
                                          			 fields in the Media
                                             				Resource Group Configuration window. See the online help about the
                                          			 fields and their configuration options. |
| Step 4 | Enter a Name and Description for the group. |
| Step 5 | From Available Media Resources , select the resources you want to add to this group, and use the arrows to move the resources to Selected Media Resources . |
| Step 6 | (Optional) To use multicast for Music On Hold audio, check the Use Multi-cast for MOH Audio check box. |
| Step 7 | Click Save . |

| Step 1 | From the Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Media Resource Group . |
|---|---|
| Step 2 | To configure
                                          			 an existing media resource group, Find
                                             				and List Media Resource Group window, specify the appropriate
                                          			 filters and click Find . |
| Step 3 | To configure
                                          			 new media resource group, click Add
                                             				New . |
| Step 4 | From the Available Media Resources field, choose the one or
                                          			 multiple devices and click the down-arrow key. The
                                          			 selected devices appear in the Selected Media Resources field. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Media Resources > Media Resource Group List . |
|---|---|
| Step 2 | Do either of the following: Click Find and select an existing list. Click Add New and create a new list. |
| Step 3 | Enter a Name for the media resource group list. |
| Step 4 | From Available Media Resource Groups , select the groups you want to add, and use the arrows to move them to Selected Media Resource Groups . |
| Step 5 | Click Save . Note For endpoints to use these media resources, you must assign the list to a device pool,  gateway port, or to a device. | Note | For endpoints to use these media resources, you must assign the list to a device pool,  gateway port, or to a device. |
| Note | For endpoints to use these media resources, you must assign the list to a device pool,  gateway port, or to a device. |

| Note | For endpoints to use these media resources, you must assign the list to a device pool,  gateway port, or to a device. |
|---|---|

| Step 1 | From the Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Media Resource Group . |
|---|---|
| Step 2 | To configure
                                          			 an existing media resource group, from the Find and List Media Resource Group window,
                                          			 specify the appropriate filters and click Find . |
| Step 3 | From the Available Media Resources list, select one or
                                          			 multiple media resources and click the down arrow key. The
                                          			 selected media resources appear in the Selected Media Resources list. |
| Step 4 | Click Save . |

| Step 1 | From the Cisco Unified CM Administration, choose Devices > Phone . To add media resources to a device pool, choose System > Device Pools . To add media resource directly to an endpoint, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select the device pool or device to which you want to assign these media resources. |
| Step 3 | From the Media Resource Group List drop-down, select a list. |
| Step 4 | Click Save . |
| Step 5 | Click Apply Config to Selected . The Apply Configuration window appears showing the device name and the applicable configuration changes. |

| Feature | Interaction |
|---|---|
| Call
                                             					 processing | Call
                                             					 processing uses a media resource group list in the device level if you select
                                             					 the media resource group list. If a resource is not found, call processing may
                                             					 retrieve it from the default allocation. Call
                                             					 processing uses media resource group list in the device pool only if you do not
                                             					 select a media resource group list in the device level. If a resource is not
                                             					 found, call processing may retrieve it from the default allocation. |
| Annunciator resource support | Cisco
                                             					 Unified Communications Manager provides annunciator resource support to a
                                             					 conference bridge if the media resource group list that contains the
                                             					 annunciator is assigned to the device pool where the conference bridge exists. Cisco
                                             					 Unified Communications Manager does not provide annunciator resource support
                                             					 for a conference bridge if the media resource group list is assigned directly
                                             					 to the device that controls the conference. |
| Video
                                             					 conference | To ensure
                                             					 that only a video conference bridge gets used when a user wants to hold a video
                                             					 conference, add the video conference bridge to a media resource group. Add the
                                             					 media resource group to a media resource group list and assign the media
                                             					 resource group list to the device or device pool that will use the video
                                             					 conference bridge. |

| Restriction | Description |
|---|---|
| Deletion
                                             					 of a media resource group | You cannot
                                             					 delete a media resource group that is assigned to a Media Resource Group List. |
| Deletion
                                             					 of a transcoder | You cannot
                                             					 delete a transcoder that is assigned to a media resource group. |
| Deletion
                                             					 of a media resource | You cannot
                                             					 delete a media resource, such as a conference bridge, that is part of a media
                                             					 resource group unless you first remove the resource from the media resource
                                             					 group or you delete the media resource group that contains the media resource. |