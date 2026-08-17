---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-https-networking-b-15cuchttpsnet-b-14cuchttpsnet-chapter-011-h-c62abb24d2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/https_networking/b_15cuchttpsnet/b_14cuchttpsnet_chapter_011.html
retrieved_at: 2026-08-17T03:43:49.191852+00:00
---

HTTPS Networking Guide for Cisco Unity Connection Release 15

# HTTPS Networking Guide for Cisco Unity Connection Release 15

Updated: December 18, 2023

Chapter: Making Changes to HTTPS Networking Configuration

## Chapter: Making Changes to HTTPS Networking Configuration

# Making Changes to HTTPS Networking Configuration

## Making Changes to HTTPS Networking Configuration

### Migration from
                           	 Legacy Network to HTTPS Network

When you remove an HTTPS link from an HTTPS network, the network
                              		gets divided into two parts. However, if you remove an HTTPS location from an
                              		HTTPS network, the network gets divided into the equal number of parts as the
                              		number of HTTPS links associated with the removed location.Then the each part
                              		of the network can be termed as a subtree. A subtree can be of the following
                              		two types with respect to a particular location:

Local
                                       				subtree : The subtree to which a Unity Connection location belongs is termed
                                    			 as local subtree.

Remote
                                       				subtree : The other subtree(s) to which a Unity Connection does not belong
                                    			 is termed as remote subtree.

For example, in figure 4-1 if you remove HTTPS link between
                              		location 1 and 2, it gets divided into two subtrees. One subtree comprising of
                              		locations 2, 5, and 6 whereas another comprising of locations 1, 3, 4, 7, 8, 9,
                              		and 10. Now with respect to location 2, the network of locations 5 and 6
                              		becomes local subtree. However, the network of locations 1, 3, 4, 7, 8, 9, and
                              		10 becomes the remote subtree for location 2.

### Removing an HTTPS Link Between Two Unity Connection Locations

When you remove an HTTPS link between two
                              		Unity Connection locations, each location stops synchronizing directory
                              		information with the locations on the other side of the HTTPS link (which is
                              		referred as subtree), removes all objects that are homed on the remote subtree,
                              		and removes all configuration information about the mediator location. The
                              		mediator location is the location through which a location communicates with
                              		the rest of the network. We recommend that you carefully consider the impacts
                              		of removing an HTTPS link prior to doing so, particularly if you plan to relink
                              		the subtrees later. Consider the following impacts:

Users, contacts, and system distribution lists
                                    			 on the local subtree are removed from distribution lists that are homed on the
                                    			 remote subtree and vice-versa. If you later relink the subtrees, you need to
                                    			 update distribution list membership to include any users, contacts, and
                                    			 distribution lists that belong to the remote subtree.

System call handlers and interview handlers
                                    			 that are configured to send messages to a remote subtree user, contact, or
                                    			 distribution list are reconfigured to send messages to the undeliverable
                                    			 messages list of the location on which the handler is configured. If you later
                                    			 relink the subtrees, you need to update the recipients for these handlers to
                                    			 use the correct remote object. (Even if you do not plan to relink the subtrees,
                                    			 you should make sure that someone is checking messages that are sent to the
                                    			 Connection undeliverable messages list, or reassign handlers that use it as a
                                    			 recipient.)

Partitions that were created for remote
                                    			 subtree locations are removed from search spaces in each Connection location in
                                    			 local subtree. If you later relink the subtrees, you need to review the
                                    			 partition membership of the search spaces that are owned on each location in
                                    			 each subtree. You need to manually re-add remote partitions to each search
                                    			 space or you may need to reorder the partitions within the search space to
                                    			 match the configuration that you had prior to removing the HTTPS link.

On each location in the network, there are
                                    			 cross-server and SMTP routing configuration settings specific to other
                                    			 locations. When you remove an HTTPS link, these settings are removed and need
                                    			 to be configured again if you later re-add the HTTPS link.

All HTTPS messaging, addressing between
                                    			 locations, and auto-attendant features unavailable after the HTTPS link is
                                    			 removed.

Do the following procedure to remove an HTTPS link between two Unity Connection 15 locations. If either of the location is
                              a Unity Connection cluster, do the steps for that location only on the publisher server.

#### Removing an HTTPS
                              	 Link

Step 1

On either of
                                             			 the locations, remove the HTTPS link. This stops synchronization with the
                                             			 remote subtree and removes all remote subtree objects from the local subtree
                                             			 directory.

In
                                                   				  Cisco Unity Connection Administration, expand Networking and select HTTPS Links .

Check the
                                                   				  check box next to the HTTPS link that you want to remove.

Select Remove Selected .

At the
                                                   				  warning about deleting associated objects, select OK to confirm the removal.

Step 2

Navigate to
                                             			 the Search
                                                				HTTPS link page of the other location and select Sync button next
                                             			 to the HTTPS link that you want to remove. Make sure that the status for the
                                             			 HTTPS link is “Link
                                                				Removal Pending” .

Step 3

Optionally,
                                             			 review the schedule for the Remove Objects Associated With Deleted Network
                                                				Location task. By default, to avoid affecting system performance
                                             			 during business hours, this task runs at once a day at 10:00 p.m., and the
                                             			 HTTPS link is not fully removed until the task has run.

To review the
                                                				schedule, either select the link to the task that is displayed in the Status
                                                				message on the Search HTTPS Links page after you have removed the selected
                                                				HTTPS link, or expand Tools and select Task
                                                   				  Management ; on the Task Definitions page, select Remove Objects Associated
                                                   				  With Deleted Network Location .

Caution

Step 4

To verify that
                                             			 the link has been removed, expand Networking , and select HTTPS
                                                				Links .

Step 5

Repeat Step
                                                				3 through Step
                                                				4 on the other location also.

### Removing a Location from an HTTPS Network

When you remove a location from an HTTPS network, it stops replicating directory information with other locations in the network
                              and all the objects that are homed on the server are removed from other locations. Similarly, all the objects that are homed
                              on other locations of the network are removed from the server you are removing.

We recommend that you carefully consider the impacts of removing a location from the network prior to doing so, particularly
                              if you plan to add the location back to the network later. Consider the following impacts:

Users on the server are removed from distribution lists that are homed on other locations in the network, and users on other
                                    locations are removed from distribution lists that are homed on the server you remove. Later on, if you add the server back
                                    into the network, you need to update the distribution list membership on the re-added server to include any remote users,
                                    and update distribution list membership on all other locations in the network to include users on the re-added server.

System call handlers and interview handlers on other locations that are configured to send messages to a user, contact, or
                                    distribution list that is homed on the server you remove are reconfigured to send messages to the undeliverable messages list
                                    of the location. Likewise, system call handlers and interview handlers on the server you remove that are configured to send
                                    messages to a user, contact, or distribution list that is homed on another location are reconfigured to send messages to the
                                    local undeliverable messages list. If you later add the server back into the network, you need to update the recipients for
                                    these handlers to use the correct remote object. (Even if you do not plan to add the server back into the network, you should
                                    make sure that someone is checking messages that are sent to the undeliverable messages list, or reassign handlers that use
                                    it as a recipient.)

Partitions that are homed on the server are removed from search spaces that are homed on other locations in the network, and
                                    partitions that are homed on other locations are removed from search spaces that are homed on the server you remove. Later
                                    on, if you add the server back into the network, you need to review the partition membership of search spaces on the re-added
                                    server and on all other locations in the network. You need to manually re-add remote partitions to each search space or you
                                    may need to reorder the partitions within the search space to match the configuration that you had prior to removing the location.

One location in the network retains a copy of search spaces that are homed on the server being removed, and the copy continues
                                    to be replicated amongst remaining locations in the network. Likewise, the server being removed makes a copy of remote search
                                    spaces that are homed on other locations. The copies replace the original search spaces on any objects that reference them.
                                    Later on, if you add the server back into the network, Unity Connection automatically attempts to resolve the ownership of
                                    the search space copies to their original location and then delete the copies. If you do not plan to add the server back into
                                    the network, you can reassign object references that use the search space copies to use other search spaces, and then delete
                                    the copies.

On each location in the network, there are configuration settings specific to other locations (for example, the fields related
                                    to cross-server transfers and SMTP routing). When you remove a server from the network, the settings for all locations in
                                    the network are deleted from the server that you remove, and the settings for the server that you remove are deleted from
                                    all other locations in the network. Later on, if you add the server back into the network, you need to update the settings
                                    for the re-added server on all other locations in the network, and configure the settings for all other locations on the re-added
                                    server.

Do the following procedure to remove a location from the HTTPS network:

Using “Remove Self from Site” Option

It is recommended that you remove only one Unity Connection location from a network at a time.

Depending on the size of the directory, removing a Unity Connection location can take a few minutes to a few hours. Even though
                              the operation may have completed on the local location, it may continue to be in progress on remote locations. We recommend
                              that you wait for the removal operation to complete on all locations in the network before making additional changes to the
                              network.

#### Using “Remove Self
                              	 from Site” Option

You can use this option to remove a Unity Connection location
                                    		  from the network using its own Cisco Unity Connection Administration interface.

Step 1

Remove the self-location from the network. This stops
                                             			 synchronization with the other locations in the network and removes all remote
                                             			 objects from the directory of the deleted location.

In Cisco Unity Connection Administration, expand Networking, and
                                                   				  then select HTTPS Links .

Select Remove Self from Site .

At the warning about deleting associated objects, select OK to confirm the removal. The status of all the
                                                   				  locations on the Search HTTPS page becomes “Link Removal Pending ”.

Step 2

Synchronize other associated HTTPS link with the deleted
                                             			 location.

Navigate to the Cisco Unity Connection Administration page of
                                                   				  each associated HTTPS link.

In Cisco Unity Connection Administration, expand Networking , and then select HTTPS Links .

On the Search HTTPS link page, select Sync button next to the HTTPS link that you want to
                                                   				  remove. Make sure that the status for the HTTPS link is “Link Removal Pending” .

Step 3

Optionally, review the schedule for the Remove Objects Associated
                                                				With Deleted Network Location task. By default, to avoid affecting
                                             			 system performance during business hours, this task runs at once a day at 10:00
                                             			 p.m., and the HTTPS link is not fully removed until the task has run.

To review the schedule, either select the link to the task that
                                                				is displayed in the Status message on the Search HTTPS Links page after you
                                                				have removed the selected HTTPS link, or expand Tools and select Task
                                                   				  Management ; on the Task Definitions page, select Remove Objects Associated With Deleted Network
                                                   				  Location.

Caution

Step 4

To verify that the link has been removed, expand Networking, and
                                             			 select HTTPS Links.

On the Search HTTPS Links page, if the link has not yet
                                                				been removed, it is displayed in the HTTPS Links table with (Link Removal
                                                				Pending) listed after the Display Name . If the Remove Objects Associated With Deleted Network
                                                   				  Location task has run and the link has been removed, the entry for
                                                				the deleted link is not displayed in the HTTPS Links table.

Step 5

Repeat Step 3 and Step 4 on the
                                             			 other associated HTTPS links also.

### Making Changes to
                           	 a Unity Connection Location

The following changes are not supported on a Unity Connection
                              		location unless you unlink the location from the network. To make the changes
                              		in a Unity Connection location, you need to remove the location from the
                              		network, make the change, and add the location back to the network:

Replacing the Unity Connection location or replacing the hard
                                    			 disk of the selected location.

Changing the IP address of the Unity Connection location.

Renaming the Unity Connection location.

To make any of these changes, do the following tasks:

Remove the Unity Connection location. See the “ Removing
                                       				a Location from an HTTPS Network ” section.

Make the change on the Unity Connection location according to the instructions in the “ Maintaining Cisco Unity Connection Server ” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection, Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

Relink the Unity Connection location to the network. See the “ Linking
                                       				Unity Connection Servers with HTTPS Link ” section.

### Updating Directly
                           	 Connected Nodes in HTTPS Networking for IP or Hostname Change

In case of IP or Hostname Change for a location, the IP or
                                 		  Hostname needs to be updated on all the directly connected nodes for the
                                 		  respective location in a HTTPS network.

Step 1

Find all directly connected nodes in the HTTPS network. Login to
                                          			 Cisco Unity Connection Administration and navigate to Networking and then select HTTPS
                                             				Links .

Step 2

Login to Cisco Unity Connection Administration of all the nodes
                                          			 found in previous step.

Step 3

Navigate to Netwoking and select HTTPS
                                             				Links and then modify the IP or Hostname.

| Note | If the location that you are removing from the network is
                                       		a Unity Connection cluster, it is recommended to remove through the publisher
                                       		server only. |
|---|---|

| Step 1 | On either of
                                             			 the locations, remove the HTTPS link. This stops synchronization with the
                                             			 remote subtree and removes all remote subtree objects from the local subtree
                                             			 directory. In
                                                   				  Cisco Unity Connection Administration, expand Networking and select HTTPS Links . Check the
                                                   				  check box next to the HTTPS link that you want to remove. Select Remove Selected . At the
                                                   				  warning about deleting associated objects, select OK to confirm the removal. |
|---|---|
| Step 2 | Navigate to
                                             			 the Search
                                                				HTTPS link page of the other location and select Sync button next
                                             			 to the HTTPS link that you want to remove. Make sure that the status for the
                                             			 HTTPS link is “Link
                                                				Removal Pending” . |
| Step 3 | Optionally,
                                             			 review the schedule for the Remove Objects Associated With Deleted Network
                                                				Location task. By default, to avoid affecting system performance
                                             			 during business hours, this task runs at once a day at 10:00 p.m., and the
                                             			 HTTPS link is not fully removed until the task has run. To review the
                                                				schedule, either select the link to the task that is displayed in the Status
                                                				message on the Search HTTPS Links page after you have removed the selected
                                                				HTTPS link, or expand Tools and select Task
                                                   				  Management ; on the Task Definitions page, select Remove Objects Associated
                                                   				  With Deleted Network Location . Caution Because server performance can be impacted by large deletion
                                                         				activities, we strongly recommend that you allow the Remove Objects Associated With Deleted Network
                                                            				  Location task to run on the default schedule (or at another time
                                                         				during non-business hours). | Caution | Because server performance can be impacted by large deletion
                                                         				activities, we strongly recommend that you allow the Remove Objects Associated With Deleted Network
                                                            				  Location task to run on the default schedule (or at another time
                                                         				during non-business hours). |
| Caution | Because server performance can be impacted by large deletion
                                                         				activities, we strongly recommend that you allow the Remove Objects Associated With Deleted Network
                                                            				  Location task to run on the default schedule (or at another time
                                                         				during non-business hours). |
| Step 4 | To verify that
                                             			 the link has been removed, expand Networking , and select HTTPS
                                                				Links . On
                                             			 the Search HTTPS
                                                				Links page, if the link has not yet been removed, it is displayed
                                             			 in the HTTPS
                                                				Links table with (Link Removal Pending) listed after the Display Name . If the Remove Objects Associated
                                                				With Deleted Network Location task has run and the link has been
                                             			 removed, the entry for the deleted link is not displayed in the HTTPS Links
                                             			 table. |
| Step 5 | Repeat Step
                                                				3 through Step
                                                				4 on the other location also. |

| Caution | Because server performance can be impacted by large deletion
                                                         				activities, we strongly recommend that you allow the Remove Objects Associated With Deleted Network
                                                            				  Location task to run on the default schedule (or at another time
                                                         				during non-business hours). |
|---|---|

| Step 1 | Remove the self-location from the network. This stops
                                             			 synchronization with the other locations in the network and removes all remote
                                             			 objects from the directory of the deleted location. In Cisco Unity Connection Administration, expand Networking, and
                                                   				  then select HTTPS Links . Select Remove Self from Site . At the warning about deleting associated objects, select OK to confirm the removal. The status of all the
                                                   				  locations on the Search HTTPS page becomes “Link Removal Pending ”. |
|---|---|
| Step 2 | Synchronize other associated HTTPS link with the deleted
                                             			 location. Navigate to the Cisco Unity Connection Administration page of
                                                   				  each associated HTTPS link. In Cisco Unity Connection Administration, expand Networking , and then select HTTPS Links . On the Search HTTPS link page, select Sync button next to the HTTPS link that you want to
                                                   				  remove. Make sure that the status for the HTTPS link is “Link Removal Pending” . |
| Step 3 | Optionally, review the schedule for the Remove Objects Associated
                                                				With Deleted Network Location task. By default, to avoid affecting
                                             			 system performance during business hours, this task runs at once a day at 10:00
                                             			 p.m., and the HTTPS link is not fully removed until the task has run. To review the schedule, either select the link to the task that
                                                				is displayed in the Status message on the Search HTTPS Links page after you
                                                				have removed the selected HTTPS link, or expand Tools and select Task
                                                   				  Management ; on the Task Definitions page, select Remove Objects Associated With Deleted Network
                                                   				  Location. Caution Because server performance can be impacted by large deletion
                                                         				activities, we strongly recommend that you allow the Remove Objects Associated With Deleted Network
                                                            				  Location task to run on the default schedule (or at another time
                                                         				during non-business hours). | Caution | Because server performance can be impacted by large deletion
                                                         				activities, we strongly recommend that you allow the Remove Objects Associated With Deleted Network
                                                            				  Location task to run on the default schedule (or at another time
                                                         				during non-business hours). |
| Caution | Because server performance can be impacted by large deletion
                                                         				activities, we strongly recommend that you allow the Remove Objects Associated With Deleted Network
                                                            				  Location task to run on the default schedule (or at another time
                                                         				during non-business hours). |
| Step 4 | To verify that the link has been removed, expand Networking, and
                                             			 select HTTPS Links. On the Search HTTPS Links page, if the link has not yet
                                                				been removed, it is displayed in the HTTPS Links table with (Link Removal
                                                				Pending) listed after the Display Name . If the Remove Objects Associated With Deleted Network
                                                   				  Location task has run and the link has been removed, the entry for
                                                				the deleted link is not displayed in the HTTPS Links table. |
| Step 5 | Repeat Step 3 and Step 4 on the
                                             			 other associated HTTPS links also. |

| Caution | Because server performance can be impacted by large deletion
                                                         				activities, we strongly recommend that you allow the Remove Objects Associated With Deleted Network
                                                            				  Location task to run on the default schedule (or at another time
                                                         				during non-business hours). |
|---|---|

| Step 1 | Find all directly connected nodes in the HTTPS network. Login to
                                          			 Cisco Unity Connection Administration and navigate to Networking and then select HTTPS
                                             				Links . |
|---|---|
| Step 2 | Login to Cisco Unity Connection Administration of all the nodes
                                          			 found in previous step. |
| Step 3 | Navigate to Netwoking and select HTTPS
                                             				Links and then modify the IP or Hostname. |