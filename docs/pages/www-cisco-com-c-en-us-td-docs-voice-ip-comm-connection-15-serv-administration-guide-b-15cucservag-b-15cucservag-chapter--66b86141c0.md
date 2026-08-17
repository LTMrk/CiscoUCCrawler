---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-serv-administration-guide-b-15cucservag-b-15cucservag-chapter--66b86141c0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/serv_administration/guide/b_15cucservag/b_15cucservag_chapter_0111.html
retrieved_at: 2026-08-17T03:44:56.319842+00:00
---

Administration Guide for Cisco Unity Connection Serviceability Release 15

# Administration Guide for Cisco Unity Connection Serviceability Release 15

Updated: December 18, 2023

Chapter: Using the Voice Network Map Tool in HTTPS Networking

## Chapter: Using the Voice Network Map Tool in HTTPS Networking

# Using the Voice Network Map Tool in HTTPS Networking

## Understanding the Voice Network Map Tool in HTTPS Networking

The Voice Network Map tool provides a consolidated visual representation of the health of the locations in an HTTPS Cisco Unity
                           Connection network.

With the tool, you can quickly locate replication problems in a network, and get information about the status of replication
                           between any two or more locations in the network.

The tool includes a network display, a data display, and a key that explains the meaning of the icons that you may see in
                           the network display.

The network display includes an icon for each location in the HTTPS network. The icon itself gives you an indicator of the
                           health of the location (or, in some cases, indicates that the tool is unable to gather data from the location). For example,
                           if the password for a particular location is not set, then the corresponding message is displayed when you hover the mouse
                           on the location in the network display.

The data display shows the information about the pair of locations that you select in the network display. This information
                           includes Host Address, Display Name, Last Sync Time, Replication Set, Max USN, Last USN and the SYNC MODE between two locations
                           in the network. For more information on the fields associated with directory synchronization, navigate to the corresponding
                           page on Cisco Unity Connection Administration and see Help > This Page.

Use the key for more information about the icons in the network display. Move the pointer over an icon in the key to see the
                           information about it. You can view additional icons by selecting the (More) link.

Tip

Right-click a location icon for options to access Cisco Unity Connection Serviceability or Cisco Unity Connection Administration
                                       for that location.

## Configuring Remote Access to Other Unity Connection Locations in an
                        	 HTTPS Network

In order for the Voice Network Map tool to
                              		  collect the data that it needs from other locations in an HTTPS network, the
                              		  location on which you use the tool must have sign-in information for other
                              		  locations in the HTTPS network. The sign-in information is not replicated
                              		  between locations in the network, so if you intend to use the Voice Network Map
                              		  tool on multiple locations in the network, do the procedure in this section on
                              		  each location on which you use the tool.

The sign-in information is also used when
                                          			 editing objects across the network in Bulk Edit mode in Unity
                                          			 Connection Administration. Changes you make to the sign-in information also
                                          			 affect access to Bulk Edit mode.

Step 1

In Cisco Unity Connection Administration,
                                       			 expand Networking , then select Unity Connection Location
                                          				Passwords .

Step 2

On the Search Enterprise Administration
                                       			 Passwords page, select a Unity Connection location from the list.

Step 3

In the Alias field, enter the username for
                                       			 the account you use to sign in to the remote server. The account must have the
                                       			 System Administrator role.

Step 4

In the Password field, enter the password
                                       			 for the account you use to sign in to the remote server.

Step 5

Select Add New .

Step 6

In Stored Enterprise Administration
                                       			 Passwords, check the check box corresponding to the Unity Connection location
                                       			 for which you want to configure the remote access.

Step 7

Select Save .

Tip

You may want to configure remote access
                                                      				  only on an as-needed basis. When remote access is no longer needed, you can
                                                      				  delete the sign-in information by checking the check box next to the applicable
                                                      				  account on the Search Enterprise Administration Password page, and selecting
                                                      				  Delete Selected.

Step 8

Repeat Step 2 through Step 7 as necessary to
                                       			 configure remote access to additional locations in the HTTPS network.

## Viewing Replication Status Information in Voice Network Map
                        	 Tool

To use the Voice Network Map
                              		  Tool, you must have configured remote access to other locations in the HTTPS
                              		  network so that the tool can collect the data it needs. See the “Configuring
                                 			 Remote Access to Other Unity Connection Locations in an HTTPS Network” section
                                 			 on page 8-2 .

Step 1

In Cisco Unity Connection Serviceability,
                                       			 from the Tools menu, select Voice Network Map .

Step 2

On the Voice Network Map page, select the
                                       			 first location for which you would like to view replication information.

Step 3

To see the replication information, such as
                                       			 replication set and Last USN associated with the remote location that you
                                       			 selected in Step 2 and another location,
                                       			 move the pointer over the second location.

You can also view the directly and
                                          				indirectly connected locations with respect to the reference location in an
                                          				HTTPS network using VNMAP tool.

If you hover the pointer on any location
                                                					 in the network display without selecting the location, the following
                                                					 information is displayed in data display section:

Host Address

Display Name

Retry Queue Size

Tip

You can quickly change the second
                                                                  							 location by moving the pointer to a new location. Alternatively, to “lock” the
                                                                  							 information display to a pair of locations, press the Control key and select
                                                                  							 the second location. To release the lock, repeat the action of pressing the
                                                                  							 Control key and selecting the second location.

Step 4

To change the first location, select a new location, then repeat Step 3 .

Step 5

The tool periodically updates the display information based on the
                                       			 update interval you specify. To change the update interval:

Select the Config tab.

In the Update Interval field, enter a
                                                					 value for the frequency at which the display information updates. The minimum
                                                					 value is 15 seconds, and the default value is 30 seconds. Note that the
                                                					 interval is reset to the default each time the Tomcat service is restarted.

Select Save .

Step 6

To pause periodic updates so that the current data continues to
                                       			 display, select the Pause tab. The tab label
                                       			 changes to Resume , which you select
                                       			 to have the tool resume periodic updates.

Step 7

To do an immediate update of replication information without
                                       			 waiting for the next update interval, select the Update tab.

| Tip | Right-click a location icon for options to access Cisco Unity Connection Serviceability or Cisco Unity Connection Administration
                                       for that location. |
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
| Step 6 | In Stored Enterprise Administration
                                       			 Passwords, check the check box corresponding to the Unity Connection location
                                       			 for which you want to configure the remote access. |
| Step 7 | Select Save . Tip You may want to configure remote access
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
| Step 8 | Repeat Step 2 through Step 7 as necessary to
                                       			 configure remote access to additional locations in the HTTPS network. |

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
                                       			 first location for which you would like to view replication information. |
| Step 3 | To see the replication information, such as
                                       			 replication set and Last USN associated with the remote location that you
                                       			 selected in Step 2 and another location,
                                       			 move the pointer over the second location. You can also view the directly and
                                          				indirectly connected locations with respect to the reference location in an
                                          				HTTPS network using VNMAP tool. If you hover the pointer on any location
                                                					 in the network display without selecting the location, the following
                                                					 information is displayed in data display section: Host Address Display Name Retry Queue Size Tip You can quickly change the second
                                                                  							 location by moving the pointer to a new location. Alternatively, to “lock” the
                                                                  							 information display to a pair of locations, press the Control key and select
                                                                  							 the second location. To release the lock, repeat the action of pressing the
                                                                  							 Control key and selecting the second location. | Tip | You can quickly change the second
                                                                  							 location by moving the pointer to a new location. Alternatively, to “lock” the
                                                                  							 information display to a pair of locations, press the Control key and select
                                                                  							 the second location. To release the lock, repeat the action of pressing the
                                                                  							 Control key and selecting the second location. |
| Tip | You can quickly change the second
                                                                  							 location by moving the pointer to a new location. Alternatively, to “lock” the
                                                                  							 information display to a pair of locations, press the Control key and select
                                                                  							 the second location. To release the lock, repeat the action of pressing the
                                                                  							 Control key and selecting the second location. |
| Step 4 | To change the first location, select a new location, then repeat Step 3 . |
| Step 5 | The tool periodically updates the display information based on the
                                       			 update interval you specify. To change the update interval: Select the Config tab. In the Update Interval field, enter a
                                                					 value for the frequency at which the display information updates. The minimum
                                                					 value is 15 seconds, and the default value is 30 seconds. Note that the
                                                					 interval is reset to the default each time the Tomcat service is restarted. Select Save . |
| Step 6 | To pause periodic updates so that the current data continues to
                                       			 display, select the Pause tab. The tab label
                                       			 changes to Resume , which you select
                                       			 to have the tool resume periodic updates. |
| Step 7 | To do an immediate update of replication information without
                                       			 waiting for the next update interval, select the Update tab. |

| Tip | You can quickly change the second
                                                                  							 location by moving the pointer to a new location. Alternatively, to “lock” the
                                                                  							 information display to a pair of locations, press the Control key and select
                                                                  							 the second location. To release the lock, repeat the action of pressing the
                                                                  							 Control key and selecting the second location. |
|---|---|