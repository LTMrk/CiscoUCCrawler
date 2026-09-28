---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-networking-guide-b-15cucnetx-b-15cucnetx-chapter-0100-html-8dd83e768e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnetx/b_15cucnetx_chapter_0100.html
retrieved_at: 2026-08-17T03:32:50.307408+00:00
---

Networking Guide for Cisco Unity Connection Release 15

# Networking Guide for Cisco Unity Connection Release 15

Updated: December 18, 2023

Chapter: Making Changes to the Networking Configuration

## Chapter: Making Changes to the Networking Configuration

# Making Changes to the Networking Configuration

## Making Changes to the Networking Configuration

### Removing a Location From a Unity Connection Site

When you remove a location from a Cisco Unity Connection site, it stops
                              		replicating directory information with other locations, and all objects that
                              		are homed on the server are removed from other locations. Likewise, all objects
                              		that are homed on other locations on the site are removed from the server you
                              		are removing.

You should consider the impacts of removing a location from the site
                              		prior to doing so, particularly if you plan to add the location back to the
                              		site later. Consider the following impacts:

Users on the server are removed from distribution lists that are
                                    			 homed on other locations in the site, and users on other locations are removed
                                    			 from distribution lists that are homed on the server you remove. If you later
                                    			 add the server back into the site, you need to update distribution list
                                    			 membership on the re-added server to include any remote users, and update
                                    			 distribution list membership on all other locations in the site to include
                                    			 users on the re-added server.

System call handlers and interview handlers on other locations that
                                    			 are configured to send messages to a user or distribution list that is homed on
                                    			 the server you remove are reconfigured to send messages to the undeliverable
                                    			 messages list of the location. Likewise, system call handlers and interview
                                    			 handlers on the server you remove that are configured to send messages to a
                                    			 user or distribution list that is homed on another location are reconfigured to
                                    			 send messages to the local undeliverable messages list. If you later add the
                                    			 server back into the site, you need to update the recipients for these handlers
                                    			 to use the correct remote object. (Even if you do not plan to add the server
                                    			 back into the site, you should make sure that someone is checking messages that
                                    			 are sent to the undeliverable messages list, or re-assign handlers that use it
                                    			 as a recipient.)

Partitions that are homed on the server are removed from search
                                    			 spaces that are homed on other locations in the site, and partitions that are
                                    			 homed on other locations are removed from search spaces that are homed on the
                                    			 server you remove. If you later add the server back into the site, you need to
                                    			 review the partition membership of search spaces on the re-added server and on
                                    			 all other locations in the site. Depending on the version of Unity Connection
                                    			 on the server and the search space configuration, you may need to manually
                                    			 re-add remote partitions to each search space, or you may need to reorder the
                                    			 partitions within the search space to match the configuration that you had
                                    			 prior to removing the location.

One location in the site retains a copy of search spaces that are
                                    			 homed on the server being removed, and the copy continues to be replicated
                                    			 amongst remaining locations in the site. Likewise, the server being removed
                                    			 makes a copy of remote search spaces that are homed on other locations. The
                                    			 copies replace the original search spaces on any objects that reference them.
                                    			 If you later add the server back into the site, Unity Connection automatically
                                    			 attempts to resolve the ownership of the search space copies to their original
                                    			 location and then deletes the copies. If you do not plan to add the server back
                                    			 into the site, you can reassign object references that use the search space
                                    			 copies to use other search spaces, and then delete the copies.

One location in the site retains a copy of search spaces that are
                                    			 homed on the server being removed, and the copy continues to be replicated
                                    			 amongst remaining locations in the site. Likewise, the server being removed
                                    			 makes a copy of remote search spaces that are homed on other locations. The
                                    			 copies replace the original search spaces on any objects that reference them.
                                    			 If you later add the server back into the site, Unity Connection automatically
                                    			 attempts to resolve the ownership of the search space copies to their original
                                    			 location and then delete the copies. If you do not plan to add the server back
                                    			 into the site, you can reassign object references that use the search space
                                    			 copies to use other search spaces, and then delete the copies.

On each location in the site, there are configuration settings
                                    			 specific to other locations (for example, the fields related to cross-server
                                    			 transfers and SMTP routing). When you remove a server from the site, the
                                    			 settings for all locations in the site are deleted from the server that you
                                    			 remove, and the settings for the server that you remove are deleted from all
                                    			 other locations in the site. If you later add the server back into the site,
                                    			 you need to update the settings for the re-added server on all other locations
                                    			 in the site, and configure the settings for all other locations on the re-added
                                    			 server.

If the location is part of a Cisco Voicemail Organization, all of
                                    			 the impacts listed above also apply for those objects and object properties
                                    			 that are replicated to and from the remote site.

Do the following procedure to remove a location from the site. You can
                              		remove only one Unity Connection location from a site at a time.

Depending on the size of the directory, removing a Unity Connection
                              		location can take a few minutes to a few hours. Even though the operation may
                              		have completed on the local location, it may continue to be in progress on
                              		remote locations. You should wait for the removal operation to complete on all
                              		locations in the site before making additional changes to the site.

#### Removing a
                              	 Location

Step 1

In Cisco
                                             			 Unity Connection Administration on any location in the site, expand Networking>
                                                				Links and select IntraSite
                                                				Links.

Step 2

Check the
                                             			 check box to the left of the Display Name of the location that you want to remove.

Step 3

Select Remove Selected and OK to
                                             			 confirm the removal.

Caution

### Making Changes to
                           	 a Unity Connection Site Gateway

The following
                              		changes are not supported on a Unity Connection site gateway unless you unlink
                              		the gateway from the remote site, remove the gateway from the local site, make
                              		the change, add the gateway back to the local site, and relink the sites:

Replacing the
                                    			 site gateway server or hard disks.

Changing the IP
                                    			 address of the site gateway.

- Renaming the site gateway.

To make any of these
                              		changes, do the following tasks:

Remove the intersite link. Depending on the type of site the gateway is linked to, see either the Removing Intersite Link Between Two Unity Connection Sites, page 5-6 .

If there are
                                    			 other locations in the Unity Connection site, remove the site gateway from the
                                    			 site. See the Removing
                                       				a Location From a Unity Connection Site, page 5-1

Make the change
                                    			 on the site gateway server.

If there are
                                    			 other locations in the Unity Connection site, add the Unity Connection site
                                    			 gateway back into the site. See the Setting
                                       				Up a Unity Connection Site, page 2-1.

Relink the sites. Depending on the type of site the gateway was linked to, see either the Linking Two Unity Connection Sites, page 2-15 .

### Removing Intersite
                           	 Link Between Two Unity Connection Sites

When you remove an
                              		intersite link between two Unity Connection sites, each site gateway stops
                              		synchronizing directory information with the other site, removes all objects
                              		that are homed on the remote site, and removes all configuration information
                              		about the remote site gateway.

You should consider
                              		the impacts of removing an intersite link prior to doing so, particularly if
                              		you plan to relink the sites later. Consider the following impacts:

Users and system
                                    			 distribution lists on each site are removed from distribution lists that are
                                    			 homed on the other site. If you later relink the sites, you need to update
                                    			 distribution list membership to include any remote users and distribution
                                    			 lists.

System call
                                    			 handlers and interview handlers that are configured to send messages to a
                                    			 remote site user or distribution list are reconfigured to send messages to the
                                    			 undeliverable messages list of the location on which the handler is configured.
                                    			 If you later relink the sites, you need to update the recipients for these
                                    			 handlers to use the correct remote object. (Even if you do not plan to relink
                                    			 the sites, you should make sure that someone is checking messages that are sent
                                    			 to the Unity Connection undeliverable messages list, or reassign handlers that
                                    			 use it as a recipient.)

Partitions that
                                    			 were created for remote site locations are removed from search spaces in each
                                    			 Unity Connection site. If you later relink the sites, you need to review the
                                    			 partition membership of the search spaces that are owned on each location in
                                    			 each site. Depending on the version of Unity Connection on the server and the
                                    			 search space configuration, you may need to manually re-add remote partitions
                                    			 to each search space, or you may need to reorder the partitions within the
                                    			 search space to match the configuration that you had prior to removing the
                                    			 intersite link.

On each location
                                    			 in the site, there are cross-server configuration settings specific to other
                                    			 locations. When you unlink the sites, these settings are removed. If you later
                                    			 relink the sites, you need to reconfigure all location-specific settings in
                                    			 both sites.

All intersite
                                    			 messaging, addressing between sites, and intersite auto-attendant features are
                                    			 unavailable after the link is removed.

Do the following procedure to remove an intersite link between two Unity Connection 15 sites. If either of the gateways is
                              a Unity Connection cluster, do the steps for that gateway only on the publisher server.

#### Steps to Remove an
                              	 Intersite Link Between Two Unity Connection Sites

Step 1

On either
                                             			 site gateway, remove the intersite link. This stops synchronization with the
                                             			 remote site and removes all remote site objects from the local site directory.

In Cisco
                                                   				  Unity Connection Administration, expand Networking > Links and select Intersite
                                                      					 Links .

On the
                                                   				  Search Intersite Links page, check the check box next to the intersite link
                                                   				  corresponding to the remote site.

Select Remove
                                                      					 Selected .

At the
                                                   				  warning about deleting associated objects, select OK .

Step 2

Optionally,
                                             			 review the schedule for the Remove Objects Associated With Deleted Remote Sites task.
                                             			 By default, to avoid affecting system performance during business hours, this
                                             			 task runs at once a day at 10:00 p.m., and the intersite link is not fully
                                             			 removed until the task has run.

To review the
                                                				schedule, either select the link to the task that is displayed in the Status
                                                				message on the Search Intersite Links page after you have removed the selected
                                                				intersite link, or expand Tools and select Task
                                                   				  Management ; on the Task Definitions page, select Remove
                                                   				  Objects Associated With Deleted Remote Sites .

Caution

Step 3

To verify that
                                             			 the link has been removed, expand Networking > Links and
                                             			 select Intersite
                                                				Links .

On the Search
                                                				Intersite Links page, if the link has not yet been removed, it is displayed in
                                                				the Intersite
                                                   				  Links table with (Link Removal Pending) listed after the Display Name . If the Remove Objects Associated
                                                   				  With Deleted Remote Sites task has run and the link has been removed, no
                                                				entry is displayed in the I ntersite Links table.

Step 4

Repeat Step
                                                				1 through Step
                                                				3 on the other site gateway.

| Step 1 | In Cisco
                                             			 Unity Connection Administration on any location in the site, expand Networking>
                                                				Links and select IntraSite
                                                				Links. |
|---|---|
| Step 2 | Check the
                                             			 check box to the left of the Display Name of the location that you want to remove. |
| Step 3 | Select Remove Selected and OK to
                                             			 confirm the removal. Caution Until Unity Connection Administration returns a status message
                                                         				indicating that the removal is complete, avoid making other changes on the site
                                                         				(for example, removing another location, joining a new location to the site,
                                                         				creating an intersite link to another site, or initiating a directory push or
                                                         				pull). | Caution | Until Unity Connection Administration returns a status message
                                                         				indicating that the removal is complete, avoid making other changes on the site
                                                         				(for example, removing another location, joining a new location to the site,
                                                         				creating an intersite link to another site, or initiating a directory push or
                                                         				pull). |
| Caution | Until Unity Connection Administration returns a status message
                                                         				indicating that the removal is complete, avoid making other changes on the site
                                                         				(for example, removing another location, joining a new location to the site,
                                                         				creating an intersite link to another site, or initiating a directory push or
                                                         				pull). |

| Caution | Until Unity Connection Administration returns a status message
                                                         				indicating that the removal is complete, avoid making other changes on the site
                                                         				(for example, removing another location, joining a new location to the site,
                                                         				creating an intersite link to another site, or initiating a directory push or
                                                         				pull). |
|---|---|

| Step 1 | On either
                                             			 site gateway, remove the intersite link. This stops synchronization with the
                                             			 remote site and removes all remote site objects from the local site directory. In Cisco
                                                   				  Unity Connection Administration, expand Networking > Links and select Intersite
                                                      					 Links . On the
                                                   				  Search Intersite Links page, check the check box next to the intersite link
                                                   				  corresponding to the remote site. Select Remove
                                                      					 Selected . At the
                                                   				  warning about deleting associated objects, select OK . |
|---|---|
| Step 2 | Optionally,
                                             			 review the schedule for the Remove Objects Associated With Deleted Remote Sites task.
                                             			 By default, to avoid affecting system performance during business hours, this
                                             			 task runs at once a day at 10:00 p.m., and the intersite link is not fully
                                             			 removed until the task has run. To review the
                                                				schedule, either select the link to the task that is displayed in the Status
                                                				message on the Search Intersite Links page after you have removed the selected
                                                				intersite link, or expand Tools and select Task
                                                   				  Management ; on the Task Definitions page, select Remove
                                                   				  Objects Associated With Deleted Remote Sites . Caution Because server performance can be impacted by large deletion
                                                         				activities, you should allow the Remove
                                                            				  Objects Associated With Deleted Remote Sites task to run on the default
                                                         				schedule (or at another time during non-business hours). | Caution | Because server performance can be impacted by large deletion
                                                         				activities, you should allow the Remove
                                                            				  Objects Associated With Deleted Remote Sites task to run on the default
                                                         				schedule (or at another time during non-business hours). |
| Caution | Because server performance can be impacted by large deletion
                                                         				activities, you should allow the Remove
                                                            				  Objects Associated With Deleted Remote Sites task to run on the default
                                                         				schedule (or at another time during non-business hours). |
| Step 3 | To verify that
                                             			 the link has been removed, expand Networking > Links and
                                             			 select Intersite
                                                				Links . On the Search
                                                				Intersite Links page, if the link has not yet been removed, it is displayed in
                                                				the Intersite
                                                   				  Links table with (Link Removal Pending) listed after the Display Name . If the Remove Objects Associated
                                                   				  With Deleted Remote Sites task has run and the link has been removed, no
                                                				entry is displayed in the I ntersite Links table. |
| Step 4 | Repeat Step
                                                				1 through Step
                                                				3 on the other site gateway. |

| Caution | Because server performance can be impacted by large deletion
                                                         				activities, you should allow the Remove
                                                            				  Objects Associated With Deleted Remote Sites task to run on the default
                                                         				schedule (or at another time during non-business hours). |
|---|---|