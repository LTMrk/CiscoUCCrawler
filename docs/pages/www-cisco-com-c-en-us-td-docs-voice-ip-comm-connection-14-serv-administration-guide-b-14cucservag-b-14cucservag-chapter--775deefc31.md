---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-serv-administration-guide-b-14cucservag-b-14cucservag-chapter--775deefc31
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/serv_administration/guide/b_14cucservag/b_14cucservag_chapter_0110.html
retrieved_at: 2026-08-17T03:53:34.962627+00:00
---

Administration Guide for Cisco Unity Connection Serviceability Release 14

# Administration Guide for Cisco Unity Connection Serviceability Release 14

Updated: March 31, 2021

Chapter: Using the Voice
	 Network Map Tool

## Chapter: Using the Voice
	 Network Map Tool

# Using the Voice
                     	 Network Map Tool

This chapter
                        		provides information on using the Voice Network Map Tool in Cisco Unity
                        		Connection Serviceability.

## Understanding the Voice Network Map Tool

The Voice Network Map tool provides a consolidated visual representation of the health of the locations in a Unity Connection
                           site. (The tool also identifies any location in the site that acts as an intersite gateway, but does not display health information
                           about other sites.)

With the tool, you can quickly locate replication problems in a site, and get information about the status of replication
                           between any two locations in the site.

The tool includes a site display, a data display, and a key that explains the meaning of the icons that you may see in the
                           site display.

The site display includes an icon for each location in the Unity Connection site. The icon itself gives you an indicator of
                           the health of the location (or, in some cases, indicates that the tool is unable to gather data from the location).

The data display shows information about the pair of locations that you select in the site display. This information includes
                           whether one location is currently pulling or pushing directory information with the other, and information about the USN,
                           or sequence numbers, of replication messages sent to and from a location. (When two locations are fully synchronized, the
                           Last USN Sent and Last USN Acknowledged values for the location that is sending replication updates equal the Last USN Received
                           value for the location that is receiving updates. During replication, it is normal for the Last USN Acknowledged value to
                           lag behind the Last USN Sent value.) You can also find the push/pull state and USN information in Cisco Unity Connection Administration,
                           but the Voice Network Map tool simplifies access to the information by providing it all in one visual display.

Use the key for more information about the icons in the site display. Move the pointer over an icon in the key to see the
                           information about it. You can view additional icons by selecting the (More) link.

Right-click a location icon for options to access Cisco Unity Connection Serviceability or Cisco Unity Connection Administration
                                       for that location. If the location is a gateway to an intersite link, you can also view a map of the servers in the remote
                                       site.

## Configuring Remote Access to Other Unity Connection Locations in a
                        	 Unity Connection Site

In order for the Voice Network Map tool to
                              		  collect the data that it needs from other locations in the Unity Connection
                              		  site, the location on which you use the tool must have sign-in information for
                              		  other locations in the site. The sign-in information is not replicated between
                              		  locations in the site, so if you intend to use the Voice Network Map tool on
                              		  multiple locations in the site, do the procedure in this section on each
                              		  location on which you use the tool.

The sign-in information is also used when
                                          			 editing objects across the network in Bulk Edit mode in Unity
                                          			 Connection Administration. Changes you make to the sign-in information also
                                          			 affect access to Bulk Edit mode.

In Cisco Unity Connection Administration,
                                       			 expand Networking , then select Unity Connection Location
                                          				Passwords .

On the Search Enterprise Administration
                                       			 Passwords page, select a Unity Connection location from the list.

In the Alias field, enter the username for
                                       			 the account you use to sign in to the remote server. The account must have the
                                       			 System Administrator role.

In the Password field, enter the password
                                       			 for the account you use to sign in to the remote server.

Select Add New .

Select Save .

You may want to configure remote access
                                                      				  only on an as-needed basis. When remote access is no longer needed, you can
                                                      				  delete the sign-in information by checking the check box next to the applicable
                                                      				  account on the Search Enterprise Administration Password page, and selecting
                                                      				  Delete Selected.

Repeat Step 2 through Step 6 as necessary to
                                       			 configure remote access to additional locations in the Unity Connection site.

## Viewing Replication Status Information in the Voice Network Map
                        	 Tool

To use the Voice Network Map
                              		  Tool, you must have configured remote access to other locations in the Unity
                              		  Connection site so that the tool can collect the data it needs. See the “Configuring
                                 			 Remote Access to Other Unity Connection Locations in a Unity Connection Site”
                                 			 section on page 7-1 .

In Cisco Unity Connection Serviceability,
                                       			 from the Tools menu, select Voice Network Map .

On the Voice Network Map page, select the
                                       			 first location for which you would like to view replication status information.

To see the replication state and data about
                                       			 USN messages sent, received, and acknowledged between the location you selected
                                       			 in Step 2 and another location,
                                       			 move the pointer over the second location.

You can quickly change the second location
                                                      				  by moving the pointer to a new location. Alternatively, to “lock” the
                                                      				  information display to a pair of locations, press the Control key and select
                                                      				  the second location. To release the lock, repeat the action of pressing the
                                                      				  Control key and selecting the second location.

To change the first location, select a new
                                       			 location, then repeat Step 3 .

The tool periodically updates the display
                                       			 information based on the update interval you specify. To change the update
                                       			 interval:

Select the Config tab.

In the Update Interval field, enter a
                                             				  value for the frequency at which the display information updates. The minimum
                                             				  value is 15 seconds, and the default value is 30 seconds. Note that the
                                             				  interval is reset to the default each time the Tomcat service is restarted.

Select Save .

To pause periodic updates so that the
                                       			 current data continues to display, select the Pause tab. The tab label
                                       			 changes to Resume , which you select
                                       			 to have the tool resume periodic updates.

To do an immediate update of replication
                                       			 information without waiting for the next update interval, select the Update tab.

| Tip | Right-click a location icon for options to access Cisco Unity Connection Serviceability or Cisco Unity Connection Administration
                                       for that location. If the location is a gateway to an intersite link, you can also view a map of the servers in the remote
                                       site. |
|---|---|

| Note | The sign-in information is also used when
                                          			 editing objects across the network in Bulk Edit mode in Unity
                                          			 Connection Administration. Changes you make to the sign-in information also
                                          			 affect access to Bulk Edit mode. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                       			 expand Networking , then select Unity Connection Location
                                          				Passwords . |
|---|---|
| Step 2 | On the Search Enterprise Administration
                                       			 Passwords page, select a Unity Connection location from the list. |
| Step 3 | In the Alias field, enter the username for
                                       			 the account you use to sign in to the remote server. The account must have the
                                       			 System Administrator role. |
| Step 4 | In the Password field, enter the password
                                       			 for the account you use to sign in to the remote server. |
| Step 5 | Select Add New . |
| Step 6 | Select Save . Tip You may want to configure remote access
                                                      				  only on an as-needed basis. When remote access is no longer needed, you can
                                                      				  delete the sign-in information by checking the check box next to the applicable
                                                      				  account on the Search Enterprise Administration Password page, and selecting
                                                      				  Delete Selected. | Tip | You may want to configure remote access
                                                      				  only on an as-needed basis. When remote access is no longer needed, you can
                                                      				  delete the sign-in information by checking the check box next to the applicable
                                                      				  account on the Search Enterprise Administration Password page, and selecting
                                                      				  Delete Selected. |
| Tip | You may want to configure remote access
                                                      				  only on an as-needed basis. When remote access is no longer needed, you can
                                                      				  delete the sign-in information by checking the check box next to the applicable
                                                      				  account on the Search Enterprise Administration Password page, and selecting
                                                      				  Delete Selected. |
| Step 7 | Repeat Step 2 through Step 6 as necessary to
                                       			 configure remote access to additional locations in the Unity Connection site. |

| Tip | You may want to configure remote access
                                                      				  only on an as-needed basis. When remote access is no longer needed, you can
                                                      				  delete the sign-in information by checking the check box next to the applicable
                                                      				  account on the Search Enterprise Administration Password page, and selecting
                                                      				  Delete Selected. |
|---|---|

| Step 1 | In Cisco Unity Connection Serviceability,
                                       			 from the Tools menu, select Voice Network Map . |
|---|---|
| Step 2 | On the Voice Network Map page, select the
                                       			 first location for which you would like to view replication status information. |
| Step 3 | To see the replication state and data about
                                       			 USN messages sent, received, and acknowledged between the location you selected
                                       			 in Step 2 and another location,
                                       			 move the pointer over the second location. Tip You can quickly change the second location
                                                      				  by moving the pointer to a new location. Alternatively, to “lock” the
                                                      				  information display to a pair of locations, press the Control key and select
                                                      				  the second location. To release the lock, repeat the action of pressing the
                                                      				  Control key and selecting the second location. | Tip | You can quickly change the second location
                                                      				  by moving the pointer to a new location. Alternatively, to “lock” the
                                                      				  information display to a pair of locations, press the Control key and select
                                                      				  the second location. To release the lock, repeat the action of pressing the
                                                      				  Control key and selecting the second location. |
| Tip | You can quickly change the second location
                                                      				  by moving the pointer to a new location. Alternatively, to “lock” the
                                                      				  information display to a pair of locations, press the Control key and select
                                                      				  the second location. To release the lock, repeat the action of pressing the
                                                      				  Control key and selecting the second location. |
| Step 4 | To change the first location, select a new
                                       			 location, then repeat Step 3 . |
| Step 5 | The tool periodically updates the display
                                       			 information based on the update interval you specify. To change the update
                                       			 interval: Select the Config tab. In the Update Interval field, enter a
                                             				  value for the frequency at which the display information updates. The minimum
                                             				  value is 15 seconds, and the default value is 30 seconds. Note that the
                                             				  interval is reset to the default each time the Tomcat service is restarted. Select Save . |
| Step 6 | To pause periodic updates so that the
                                       			 current data continues to display, select the Pause tab. The tab label
                                       			 changes to Resume , which you select
                                       			 to have the tool resume periodic updates. |
| Step 7 | To do an immediate update of replication
                                       			 information without waiting for the next update interval, select the Update tab. |

| Tip | You can quickly change the second location
                                                      				  by moving the pointer to a new location. Alternatively, to “lock” the
                                                      				  information display to a pair of locations, press the Control key and select
                                                      				  the second location. To release the lock, repeat the action of pressing the
                                                      				  Control key and selecting the second location. |
|---|---|