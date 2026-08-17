---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-administration-guide-b-14cucsag-b-14cucsag-chapter-01001-html-df0b7d36aa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag/b_14cucsag_chapter_01001.html
retrieved_at: 2026-08-17T02:26:07.594257+00:00
---

System Administration Guide

# System Administration Guide

Updated: December 18, 2025

Chapter: Networking

## Chapter: Networking

# Networking

- VPIM (Voice Profile for Internet Mail) Network: Involves creating a network of different locations, such as Unity Connection
                              and Cisco Unity based on VPIM protocol that allows different voice messaging systems to exchange voice and text messages over
                              the Internet or any TCP/IP network. For more information on VPIM network, see the "VPIM Networking in Cisco Unity Connection"
                              chapter of the Networking Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnetx.html .

- Legacy Network: Involves creating a network of different locations, such as Unity Connection and Cisco Unity using intrasite
                              and intersite links. For more information on legacy network, see the Networking Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnetx.html .

- Cisco Unity Connection Survivable Remote Site Voicemail Network: Involves creating a network of multiple branches (Unity Connection
                              SRSV) and central (Unity Connection) location based on client-server architecture. Cisco Unity Connection Survivable Remote
                              Site Voicemail (Unity Connection SRSV) is a backup voicemail solution that allows you to receive voice messages during WAN
                              outages. For more information on Unity Connection SRSV, see the Complete Reference Guide for Cisco Unity Connection Survivable Remote Site Voicemail (SRSV) for Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/srsv/guide/b_15cucsrsvx.html .

```
run cuc dbquery unitydirdb update tbl_configuration set valuebool = 1 where 
fullname = 'System.Security.EnableSha256'
```

## Legacy Links

Legacy links include intrasite and intersite links. In a legacy or digital network, you can create, edit, or delete an intrasite
                           or an intersite link.

### Intrasite Links

You can connect multiple Unity Connection locations in an organization through an intrasite link. The network of locations
                              connected through intrasite links is referred to as Unity Connection site.

#### Configuring an
                              	 Intrasite Link

Step 1

In Cisco Unity Connection Administration, expand Networking > Legacy
                                                   				  Links and select Intrasite Links .

Step 2

Configure an
                                             			 intrasite link (For information on each field, select Help > This Page.):

To add an intrasite link, select Join Site. On the Join Site
                                                      					 page, enter the required information and select Auto Join Site or Upload based
                                                      					 on the option that you select in the Method Used to Join Site field.

To edit an intrasite link, select the intrasite link that you
                                                      					 want to edit. On the Edit Intrasite Link page, enter the required information
                                                      					 and select Save.

To delete an intrasite link:

On the Search Intrasite Links page, select the intrasite link
                                                      					 that you want to delete.

Select Remove Selected or Remove Self from Site.

### Intersite Links

You can connect multiple Unity Connection sites through intersite links.

#### Configuring an Intersite Link

Step 1

In Cisco Unity Connection Administration,
                                             			 expand Networking > Legacy Links and select Intersite Links .

Step 2

Configure an intersite link (For information on each field, select
                                             			 Help > This Page.):

To add an intersite link, select Add. On
                                                      					 the New Intersite Link page appears, enter the required information and select
                                                      					 Link.

To edit an intersite link, select the
                                                      					 intersite link that you want to edit. On the Edit Intersite Link page, enter
                                                      					 the required information and select Save.

To delete an intersite link:

On the Search Intersite Links page,
                                                      					 select the intersite link that you want to delete.

Select Remove Selected.

## Branch Management

Branch Management node allows you to perform various tasks, such as viewing branch synchronization results and updating branch
                           information.

### Branches

You can add one or more branches associated with a central Unity Connection location where each branch acts as a backup voicemail
                              solution for receiving voice messages during WAN outages.

#### Configuring a Branch

Step 1

In Cisco Unity Connection Administration,
                                             			 expand Networking > Branch Management and select Branches .

The Branch Listing page appears displaying
                                                				the currently configured branches.

Step 2

Configure a branch (For information on each field, select Help
                                             			 > This Page.):

To add a branch, select Add New. The New
                                                      					 Branch page appears. Enter the required information and select Link.

To edit a branch, select the branch that
                                                      					 you want to edit. On the Edit Branch page, enter the required information and
                                                      					 select Save.

To delete a branch:

On the Branch Listing page, select the
                                                      					 branch that you want to delete.

Select Deleted Selected.

#### Branch Synch Results

You can view the details, such as synchronization type and start date associated with the different branches connected to
                                 a central Unity Connection location.

In Cisco Unity Connection Administration, expand Networking > Branch Management and then select Branch Synch Results . The Branch Synch Results page appears displaying the details of the currently configured branches. For information on each field, see Help> This Page.

## HTTPS Links

HTTPS links allows you to create a network that is more scalable both in terms of number of Unity Connection locations and
                           the total directory size.

### Configuring an HTTPS Link

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Networking > and then select > HTTP(S) Links .

The Search HTTP(S) Links page appears
                                             				displaying the details of the currently configured HTTPS links.

Step 2

Configure an HTTPS link (For information on each field, select
                                          			 Help > This Page.):

To add an HTTPS link, select Add. On the
                                                   					 New HTTP(S) Link page, enter the required information and select Link.

To edit an HTTPS link, select the HTTPS
                                                   					 link that you want to edit. On the Edit HTTPS Link page, enter the required
                                                   					 information and select Save.

To delete an HTTPS link:

On the Search HTTP(S) Links page, select
                                                   					 the HTTPS link that you want to delete.

Select Remove Selected or Remove Self
                                                   					 from Site.

## Locations

You can view a brief description (type and display name) of all the locations connected to a Unity Connection location.

To view the locations, in Cisco Unity Connection Administration, expand Networking and then select Locations . For information on each field, see Help> This Page.

## VPIM

Unity Connection supports the Voice Profile for Internet Mail (VPIM) protocol, an industry standard that allows different
                           voice messaging systems to exchange voice and text messages over the Internet or any TCP/IP network.

### Configuring an HTTPS Link

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Networking > and then select > HTTP(S) Links .

The Search HTTP(S) Links page appears
                                             				displaying the details of the currently configured HTTPS links.

Step 2

Configure an HTTPS link (For information on each field, select
                                          			 Help > This Page.):

To add an HTTPS link, select Add. On the
                                                   					 New HTTP(S) Link page, enter the required information and select Link.

To edit an HTTPS link, select the HTTPS
                                                   					 link that you want to edit. On the Edit HTTPS Link page, enter the required
                                                   					 information and select Save.

To delete an HTTPS link:

On the Search HTTP(S) Links page, select
                                                   					 the HTTPS link that you want to delete.

Select Remove Selected or Remove Self
                                                   					 from Site.

## Connection Location Passwords

You can configure remote access to other
                              		  Cisco Unity Connection Administration locations in the network by saving login
                              		  credentials of all the locations on one location.

Step 1

In Cisco Unity Connection Administration,
                                       			 expand Networking > and then select > Connection Location
                                             				  Passwords.

The Search Enterprise Administration
                                          				Passwords page displays the currently configured location passwords.

Step 2

Configure a location password (For
                                       			 information on each field, select Help > This Page.):

To add a location password:

Select the location from the Connection
                                                					 Location drop-down and enter the required information.

Select Add New and then select Save.

To delete a location password:

On the Search Enterprise Administration
                                                					 Passwords page, select the location for which you want to delete the
                                                					 credentials.

Select Delete Selected.

| Note | A Cisco Unity location cannot be connected in an HTTPS network. |
|---|---|

| Note | It is recommended to upgrade all nodes in the Networking to Release 15 SU2 or later to ensure smooth operation and avoid replication
                                          issues. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Networking > Legacy
                                                   				  Links and select Intrasite Links . The Search
                                             			 Intrasite Links page appears displaying the currently configured intrasite
                                             			 links. |
|---|---|
| Step 2 | Configure an
                                             			 intrasite link (For information on each field, select Help > This Page.): To add an intrasite link, select Join Site. On the Join Site
                                                      					 page, enter the required information and select Auto Join Site or Upload based
                                                      					 on the option that you select in the Method Used to Join Site field. To edit an intrasite link, select the intrasite link that you
                                                      					 want to edit. On the Edit Intrasite Link page, enter the required information
                                                      					 and select Save. To delete an intrasite link: On the Search Intrasite Links page, select the intrasite link
                                                      					 that you want to delete. Select Remove Selected or Remove Self from Site. |

| Step 1 | In Cisco Unity Connection Administration,
                                             			 expand Networking > Legacy Links and select Intersite Links . The Search Intersite Links page appears displaying the currently
                                             			 configured intersite links. |
|---|---|
| Step 2 | Configure an intersite link (For information on each field, select
                                             			 Help > This Page.): To add an intersite link, select Add. On
                                                      					 the New Intersite Link page appears, enter the required information and select
                                                      					 Link. To edit an intersite link, select the
                                                      					 intersite link that you want to edit. On the Edit Intersite Link page, enter
                                                      					 the required information and select Save. To delete an intersite link: On the Search Intersite Links page,
                                                      					 select the intersite link that you want to delete. Select Remove Selected. |

| Step 1 | In Cisco Unity Connection Administration,
                                             			 expand Networking > Branch Management and select Branches . The Branch Listing page appears displaying
                                                				the currently configured branches. |
|---|---|
| Step 2 | Configure a branch (For information on each field, select Help
                                             			 > This Page.): To add a branch, select Add New. The New
                                                      					 Branch page appears. Enter the required information and select Link. To edit a branch, select the branch that
                                                      					 you want to edit. On the Edit Branch page, enter the required information and
                                                      					 select Save. To delete a branch: On the Branch Listing page, select the
                                                      					 branch that you want to delete. Select Deleted Selected. |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Networking > and then select > HTTP(S) Links . The Search HTTP(S) Links page appears
                                             				displaying the details of the currently configured HTTPS links. |
|---|---|
| Step 2 | Configure an HTTPS link (For information on each field, select
                                          			 Help > This Page.): To add an HTTPS link, select Add. On the
                                                   					 New HTTP(S) Link page, enter the required information and select Link. To edit an HTTPS link, select the HTTPS
                                                   					 link that you want to edit. On the Edit HTTPS Link page, enter the required
                                                   					 information and select Save. To delete an HTTPS link: On the Search HTTP(S) Links page, select
                                                   					 the HTTPS link that you want to delete. Select Remove Selected or Remove Self
                                                   					 from Site. |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Networking > and then select > HTTP(S) Links . The Search HTTP(S) Links page appears
                                             				displaying the details of the currently configured HTTPS links. |
|---|---|
| Step 2 | Configure an HTTPS link (For information on each field, select
                                          			 Help > This Page.): To add an HTTPS link, select Add. On the
                                                   					 New HTTP(S) Link page, enter the required information and select Link. To edit an HTTPS link, select the HTTPS
                                                   					 link that you want to edit. On the Edit HTTPS Link page, enter the required
                                                   					 information and select Save. To delete an HTTPS link: On the Search HTTP(S) Links page, select
                                                   					 the HTTPS link that you want to delete. Select Remove Selected or Remove Self
                                                   					 from Site. |

| Step 1 | In Cisco Unity Connection Administration,
                                       			 expand Networking > and then select > Connection Location
                                             				  Passwords. The Search Enterprise Administration
                                          				Passwords page displays the currently configured location passwords. |
|---|---|
| Step 2 | Configure a location password (For
                                       			 information on each field, select Help > This Page.): To add a location password: Select the location from the Connection
                                                					 Location drop-down and enter the required information. Select Add New and then select Save. To delete a location password: On the Search Enterprise Administration
                                                					 Passwords page, select the location for which you want to delete the
                                                					 credentials. Select Delete Selected. |