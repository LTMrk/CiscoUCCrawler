---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-administration-guide-b-14cucsag-b-14cucsag-chapter-01111-html-d5f744fec9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag/b_14cucsag_chapter_01111.html
retrieved_at: 2026-08-17T02:26:32.792363+00:00
---

System Administration Guide

# System Administration Guide

Updated: December 18, 2025

Chapter: Video

## Chapter: Video

# Video

## Video

Cisco Media Sense is now end of life and end of support, hence Unity Connection will no longer provide the Video Messaging
                                       feature for users.For more information on Cisco Media Sense EOL, see https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/mediasense/eos-eol-notice-c51-738857.html .

In Unity Connection,
                           		a user or an outside caller can also send video message to another user using
                           		video enabled end point in case of Ring No Answer (RNA). A user can also record
                           		a greeting in video format from a video enabled end point.

- Video Messaging chapter of Design Guide for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/guide/b_15cucdg.html

- Video Compatibility Matrix
                                 		  section of Compatibility
                                    			 Matrix for Cisco Unity Connection available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/compatibility/matrix/b_cucclientmtx.html .

### Task List for
                           	 Configuring Video Messaging

Do the following tasks to enable video messaging for the users:

- In Cisco Unity Connection
                                          				Administration, expand Class of
                                             				  Service and select Class of
                                             				  Service .

- On the Search Class of
                                          				Service page, select the class of service applied to the voicemail users.

- On the Edit Class of
                                          				Service page, in the Enable
                                             				  Video section, check the check boxes depending on your requirement. (For
                                          				more information on each field, see Help> This Page).

- Select Save .

Install the Cisco MediaSense video server. For more information,
                                    			 see the Installing
                                       				and Configuring Cisco MediaSense section.

Configure video services in Unity Connection. Ensure that the
                                    			 current video call is not exceeding 20 concurrent video sessions as supported
                                    			 in Unity Connection.

Make sure that the video server with which Unity Connection
                                                				integrates for the storage and retrieval of video messages and greetings is in
                                                				the active state.

For more information, see the Configuring
                                       				Video Services section.

You can also use the Bulk Administration Tool (BAT) to configure
                                                				video service accounts. For more information on configuring video service
                                                				accounts using BAT tool, see the Bulk
                                                   				  Administration Tool section.

- Configure the video
                                 		  resolution for video messages and greetings associated with a port group. For
                                 		  more information on configuring port group, see the Codec Advertising section
                                 		  in Telephony
                                    			 Integration chapter.

- Configure the number of
                                 		  expiration days for video messages after which the video part of a video
                                 		  message get expired and only audio part is retained as a voice message. For
                                 		  more information on configuring message expiration policy, see the Message
                                 		  Recording Expiration section in the Message
                                    			 Storage chapter.

### Installing and
                           	 Configuring Cisco MediaSense

Cisco MediaSense is a video server that integrates with Unity
                                 		  Connection to support the recording, playback, and storage of audio and video
                                 		  recordings.

Step 1

Download and install Cisco MediaSense:

For information, see the “Cisco MediaSense Installation” chapter
                                             				of Installation and Administration Guide for Cisco MediaSense Release 9.0(1),
                                             				available at http://www.cisco.com/en/US/docs/voice_ip_comm/cust_contact/contact_center/mediasense/901/inst_admin/CUMS_BK_IFE33F4B_00_mediasense-install-and-admin-guide_chapter_010.html .

Step 2

Access Cisco MediaSense Administration:

From a web browser on any computer in your Unified
                                                				  Communications network, go to http://servername/oraadmin.

The servername is the IP address of the server where you have
                                                   					 installed Cisco MediaSense.

A Security Alert message may appear, prompting you to accept the
                                                				  self-signed security certificate, if you have not already installed it. This
                                                				  security message may not appear if you have already installed a security
                                                				  certificate. The Cisco MediaSense Administration Authentication page appears.

Enter the Application Administrator User ID and Password and
                                                				  select Log In.

Step 3

Select the video file from Cisco MediaSense:

In Cisco MediaSense Administration, select Media File
                                                   					 Management > Add .

On the Add Media File page, enter a title for the video to be
                                                				  uploaded. Make sure that the title name of the image should be
                                                				  CiscoUnityConnectionLogo.mp4.

(Optional) Enter a description of the file.

Browse to select the Cisco logo in the File field and select Save .

You can either select a customized logo from your system or can
                                                         				  select the standard Cisco logo.

The customized logo must be in MP4 format and should meet the
                                             				following specifications:

H.264 constrained baseline profile

Resolution 1080p, 720p, 480p, or 360p

Audio AAC-LC (MediaSense converts it to AAC-LD upon import)

48000 Hz sampling frequency

Mono

Maximum 2GB file size

Step 4

Disable Cisco
                                          			 Media Sense Prune Policy:

Cisco
                                             				MediaSense has a default setting of pruning enabled for 60 days, which means
                                             				that MediaSense deletes all video messages/greetings after 60 days and the
                                             				messages/greetings are not available any more. To avoid your video
                                             				messages/greetings from getting deleted, you must disable the MediaSense Prune
                                             				Policy setting

- In Cisco MediaSense
                                                				  Administration, select Prune Policy Configuration.

- On the MediaSense Prune
                                                				  Policy Configuration page, uncheck the Automatically prune recordings after
                                                				  they are more than 60 days old, and when disk space is needed for new
                                                				  recordings (1) check box and select Save.

- Restart all the Cisco
                                                				  MediaSense media services on all the nodes.

### Configuring Video
                           	 Services

Video services allow Unity Connection to integrate with video
                                 		  server to store and retrieve all the video messages and greetings recorded by
                                 		  the user. In addition, it allows Unity Connection to verify the state of video
                                 		  server, codecs, and user credentials used with video server.

Step 1

In Cisco Unity Connection Administration, expand Video and
                                          			 select Video
                                             				Services .

The Search Video Services page appears displaying the currently
                                             				configured video services.

Step 2

Configure video services (For more information on each field,
                                          			 see Help > This
                                             				Page ):

To add a new video service
                                                      						account:

- On the Search Video
                                                      						Services page, select Add
                                                         						  New .

- On the New Video Service
                                                      						page, enter the values of the required fields and select Save . You need to restart the Connection Conversation
                                                      						service on each server in a Unity Connection cluster.

- Select Test to display the task execution results window.

To edit an existing video
                                                      						service:

- On the Search Video
                                                      						Services page, select the video service that you want to edit.

- On the Edit Video Service
                                                      						page, enter the values of the required fields and select Save .

- Select Test to display the task execution results window.

To delete one or more video
                                                      						services:

- On the Search Video
                                                      						Services page, check the check boxes for the video services that you want to
                                                      						delete.

- Select Delete
                                                         						  Selected and OK to confirm.

### Configuring Video
                           	 Services Accounts

After configuring video services in Unity Connection, the
                                 		  administrator needs to configure video service accounts for each user.

You can also use the Bulk Administration Tool (BAT) to create,
                                             			 edit, and delete multiple video services accounts at the same time by importing
                                             			 information contained in a comma separated value (CSV) file.

Step 1

In Cisco Unity Connection Administration, expand Users and
                                          			 select Users .

The Search Users page appears displaying the currently
                                             				configured users.

Step 2

Configure video service accounts for the users (For more
                                          			 information on each field, see Help> This
                                             				Page ):

To add a video service
                                                      						account for a user:

- On the Search Users page,
                                                      						find the user for which you want to create a video service account.

- On the Edit Users Basics
                                                      						page, select Edit>
                                                         						  Video Services Accounts .

- On the Video Services
                                                      						Accounts page, select Add
                                                         						  New .

- For each user,
                                                                  						  you can add only one video service account.

- On the New Video
                                                                  						  Services Accounts page, enter the values of the required fields. Check the Map
                                                                  						  Video Service check box to configure the video service with video service
                                                                  						  account and select Save .

To edit an existing video
                                                      						service account for one or more users:

- On the Search Users page,
                                                      						find the user for which you want to edit the video service account. To edit the
                                                      						video service account of more than one user, check the check boxes for the
                                                      						users and select Bulk Edit.

- On the Edit User Basics
                                                      						page, select Edit>
                                                         						  Video Services Accounts .

- On the Video Services
                                                      						Accounts page, select the video service account that you want to edit.

- On the Edit Video Services
                                                      						Accounts page, enter the values of the required fields. Select the Map Video
                                                      						Service check box to configure the video service with video service account and
                                                      						select Save .

To delete a video service
                                                      						account for one or more users:

- On the Search Users page,
                                                      						find the user for which you want to delete the video service account.

- On the Edit User Basics
                                                      						page, select Edit>
                                                         						  Video Service Accounts .

- On the Video Service
                                                      						Accounts page, select the video service account that you want to delete.

- Select Delete
                                                         						  Selected and OK to confirm.

| Note | Cisco Media Sense is now end of life and end of support, hence Unity Connection will no longer provide the Video Messaging
                                       feature for users.For more information on Cisco Media Sense EOL, see https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/mediasense/eos-eol-notice-c51-738857.html . |
|---|---|

| Note | Make sure that the video server with which Unity Connection
                                                				integrates for the storage and retrieval of video messages and greetings is in
                                                				the active state. |
|---|---|

| Note | You can also use the Bulk Administration Tool (BAT) to configure
                                                				video service accounts. For more information on configuring video service
                                                				accounts using BAT tool, see the Bulk
                                                   				  Administration Tool section. |
|---|---|

| Note | You can also
                                       		configure the Differentiated Services Code Point (DSCP) value for the video
                                       		messaging on Telephony Configuration page of Cisco Unity Connection
                                       		Administration. However, it is recommended to set the value of this parameter
                                       		to the default unless a Cisco support engineer instructs otherwise. |
|---|---|

| Step 1 | Download and install Cisco MediaSense: For information, see the “Cisco MediaSense Installation” chapter
                                             				of Installation and Administration Guide for Cisco MediaSense Release 9.0(1),
                                             				available at http://www.cisco.com/en/US/docs/voice_ip_comm/cust_contact/contact_center/mediasense/901/inst_admin/CUMS_BK_IFE33F4B_00_mediasense-install-and-admin-guide_chapter_010.html . |
|---|---|
| Step 2 | Access Cisco MediaSense Administration: From a web browser on any computer in your Unified
                                                				  Communications network, go to http://servername/oraadmin. The servername is the IP address of the server where you have
                                                   					 installed Cisco MediaSense. A Security Alert message may appear, prompting you to accept the
                                                				  self-signed security certificate, if you have not already installed it. This
                                                				  security message may not appear if you have already installed a security
                                                				  certificate. The Cisco MediaSense Administration Authentication page appears. Enter the Application Administrator User ID and Password and
                                                				  select Log In. |
| Step 3 | Select the video file from Cisco MediaSense: In Cisco MediaSense Administration, select Media File
                                                   					 Management > Add . On the Add Media File page, enter a title for the video to be
                                                				  uploaded. Make sure that the title name of the image should be
                                                				  CiscoUnityConnectionLogo.mp4. (Optional) Enter a description of the file. Browse to select the Cisco logo in the File field and select Save . Note You can either select a customized logo from your system or can
                                                         				  select the standard Cisco logo. The customized logo must be in MP4 format and should meet the
                                             				following specifications: H.264 constrained baseline profile Resolution 1080p, 720p, 480p, or 360p Audio AAC-LC (MediaSense converts it to AAC-LD upon import) 48000 Hz sampling frequency Mono Maximum 2GB file size | Note | You can either select a customized logo from your system or can
                                                         				  select the standard Cisco logo. |
| Note | You can either select a customized logo from your system or can
                                                         				  select the standard Cisco logo. |
| Step 4 | Disable Cisco
                                          			 Media Sense Prune Policy: Cisco
                                             				MediaSense has a default setting of pruning enabled for 60 days, which means
                                             				that MediaSense deletes all video messages/greetings after 60 days and the
                                             				messages/greetings are not available any more. To avoid your video
                                             				messages/greetings from getting deleted, you must disable the MediaSense Prune
                                             				Policy setting In Cisco MediaSense
                                                				  Administration, select Prune Policy Configuration. On the MediaSense Prune
                                                				  Policy Configuration page, uncheck the Automatically prune recordings after
                                                				  they are more than 60 days old, and when disk space is needed for new
                                                				  recordings (1) check box and select Save. Restart all the Cisco
                                                				  MediaSense media services on all the nodes. |

| Note | You can either select a customized logo from your system or can
                                                         				  select the standard Cisco logo. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Video and
                                          			 select Video
                                             				Services . The Search Video Services page appears displaying the currently
                                             				configured video services. |
|---|---|
| Step 2 | Configure video services (For more information on each field,
                                          			 see Help > This
                                             				Page ): To add a new video service
                                                      						account: On the Search Video
                                                      						Services page, select Add
                                                         						  New . On the New Video Service
                                                      						page, enter the values of the required fields and select Save . You need to restart the Connection Conversation
                                                      						service on each server in a Unity Connection cluster. Select Test to display the task execution results window. To edit an existing video
                                                      						service: On the Search Video
                                                      						Services page, select the video service that you want to edit. On the Edit Video Service
                                                      						page, enter the values of the required fields and select Save . Select Test to display the task execution results window. To delete one or more video
                                                      						services: On the Search Video
                                                      						Services page, check the check boxes for the video services that you want to
                                                      						delete. Select Delete
                                                         						  Selected and OK to confirm. |

| Note | You can also use the Bulk Administration Tool (BAT) to create,
                                             			 edit, and delete multiple video services accounts at the same time by importing
                                             			 information contained in a comma separated value (CSV) file. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Users and
                                          			 select Users . The Search Users page appears displaying the currently
                                             				configured users. |
|---|---|
| Step 2 | Configure video service accounts for the users (For more
                                          			 information on each field, see Help> This
                                             				Page ): To add a video service
                                                      						account for a user: On the Search Users page,
                                                      						find the user for which you want to create a video service account. On the Edit Users Basics
                                                      						page, select Edit>
                                                         						  Video Services Accounts . On the Video Services
                                                      						Accounts page, select Add
                                                         						  New . Note For each user,
                                                                  						  you can add only one video service account. On the New Video
                                                                  						  Services Accounts page, enter the values of the required fields. Check the Map
                                                                  						  Video Service check box to configure the video service with video service
                                                                  						  account and select Save . To edit an existing video
                                                      						service account for one or more users: On the Search Users page,
                                                      						find the user for which you want to edit the video service account. To edit the
                                                      						video service account of more than one user, check the check boxes for the
                                                      						users and select Bulk Edit. On the Edit User Basics
                                                      						page, select Edit>
                                                         						  Video Services Accounts . On the Video Services
                                                      						Accounts page, select the video service account that you want to edit. On the Edit Video Services
                                                      						Accounts page, enter the values of the required fields. Select the Map Video
                                                      						Service check box to configure the video service with video service account and
                                                      						select Save . To delete a video service
                                                      						account for one or more users: On the Search Users page,
                                                      						find the user for which you want to delete the video service account. On the Edit User Basics
                                                      						page, select Edit>
                                                         						  Video Service Accounts . On the Video Service
                                                      						Accounts page, select the video service account that you want to delete. Select Delete
                                                         						  Selected and OK to confirm. | Note | For each user,
                                                                  						  you can add only one video service account. On the New Video
                                                                  						  Services Accounts page, enter the values of the required fields. Check the Map
                                                                  						  Video Service check box to configure the video service with video service
                                                                  						  account and select Save . |
| Note | For each user,
                                                                  						  you can add only one video service account. On the New Video
                                                                  						  Services Accounts page, enter the values of the required fields. Check the Map
                                                                  						  Video Service check box to configure the video service with video service
                                                                  						  account and select Save . |

| Note | For each user,
                                                                  						  you can add only one video service account. On the New Video
                                                                  						  Services Accounts page, enter the values of the required fields. Check the Map
                                                                  						  Video Service check box to configure the video service with video service
                                                                  						  account and select Save . |
|---|---|