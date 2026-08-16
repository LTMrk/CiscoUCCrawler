---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su4-cucm-b-feature-configuration-guide-cisco1251su4-cucm-b--6a082463b7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU4/cucm_b_feature-configuration-guide-cisco1251su4/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_0111100.html
retrieved_at: 2026-08-16T17:01:48.909227+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: July 31, 2025

Chapter: Configure Location Awareness

## Chapter: Configure Location Awareness

# Configure Location Awareness

## Location Awareness Overview

Important

Meraki Access Points support for Location Awareness is applicable only from Release 12.5(1)SU6 onwards and Release 14SU1 onwards.

Location Awareness allows administrators to determine the physical location from which a phone connects to the company network.
                              For wireless networks, you can view the wireless access point infrastructure, and which mobile devices currently associate
                              to those access points. For wired networks, you can view the Ethernet switch infrastructure and see which devices are currently
                              connected to those switches. This allows you to determine the building, floor, and cube from which a call was placed.

Currently, wired phones do not support Location Awareness.

You can view your network infrastructure from Cisco Unified CM Administration > Advanced Features > Device Location Tracking Services > Switches and Access Points > Find and List Switches and Access Points window.

This feature updates the Unified Communications Manager database dynamically with the following information:

Network infrastructure devices such as switches and wireless access points, including IP addresses, hostnames, and BSSID info
                                    (where applicable) for each infrastructure device.

Associated endpoints for each infrastructure device, including:

For wireless networks, the list of devices that are currently associated to a wireless access point.

For wired networks, the list of devices and device types that are currently connected to an ethernet switch.

### Cisco Emergency Responder Integration

Location Awareness helps integrated applications such as Cisco Emergency Responder to determine the physical location of a
                              user who places an emergency call. When Location Awareness is enabled, Cisco Emergency Responder learns of a new device to
                              infrastructure association within minutes of a mobile device associating with a new wireless access point, or a desk phone
                              being connected to a new ethernet switch.

When Cisco Emergency Responder first starts up, it queries the Unified Communications Manager Database for the current device to network infrastructure associations. Every two minutes following, the Cisco Emergency
                              Responder checks for updates to the existing associations. As a result, even if a mobile caller places an emergency call while
                              in a roaming situation, Cisco Emergency Responder can quickly determine the physical location of the caller and send emergency
                              services to the appropriate building, floor, or cube.

### Wireless Network Updates

To enable Location Awareness for your wireless infrastructure, you can configure Unified Communications Manager to synchronize
                                 with a Cisco Wireless LAN Controller. You can synchronize Unified Communications Manager with up to fifty controllers. During
                                 the synchronization process, Unified Communications Manager updates its database with the access point infrastructure that
                                 the controller manages. In Cisco Unified CM Administration, you can view the status for your wireless access points, including
                                 the list of mobile clients that are associated to each access point.

As mobile clients roam between access points, SIP and SCCP signaling from the endpoint communicates the new device to access
                                 point association to Unified Communications Manager, which updates its database. Cisco Emergency Responder also learns of
                                 the new association by querying the Unified Communications Manager database every few minutes for new endpoints that have
                                 changed their association. As a result, if a mobile client places an emergency call, Cisco Emergency Responder has accurate
                                 information on the physical location of the user whom placed the call.

If you have a regular synchronization schedule for your Wireless Access Point controllers, Unified Communications Manager
                                 adds and updates access points from the database dynamically following each synchronization.

#### Using Bulk Administration to insert Access Points

If you are using a third-party wireless access point controller, or if you want to export your access points from Cisco Prime
                                 Infrastructure, you can use the Bulk Administration Tool to bulk insert your wireless access point infrastructure from a CSV
                                 file into the Unified Communications Manager database. Following the bulk insert, the next location update from the mobile
                                 device updates the database with the current access point association.

However, Bulk Administration does not allow you to update your access point infrastructure dynamically as new access points
                                 get added to your wireless network. If a mobile call gets placed through an access point that was added after the bulk insert,
                                 that access point will not have a record in the database, Unified Communications Manager will not be able to match the BSSID
                                 of the new access point, and will mark the infrastructure for the wireless device as UNIDENTIFIED AP.

For detailed information on the Bulk Administration Tool, refer to the "Manage Infrastructure Devices" chapter of the Bulk Administration Guide for Cisco Unified Communications Manager .

### Supported Endpoints for Location Awareness

The following endpoints support tracking via Location Awareness:

Cisco Uniifed Wireless IP Phone 7925G

Cisco Unified Wireless IP Phone 7925G-EX

Cisco Unified Wireless IP Phone 7926G

Cisco Jabber clients—supported as of 12.5(1)SU1

Cisco Wireless IP Phone 8821—supported as of 12.5(1)SU1

Webex App—supported as of 12.5(1)SU1

These endpoints provide upstream infrastructure information, such as BSSID, through Station Info messages to Cisco Unified
                                 Communications Manager. Cisco Emergency Responder uses AXL Change Notifications to track these devices through the associated
                                 access point.

For device tracking to work, wireless access points must be defined in Cisco Unified Communications Manager. You can do this
                                 by syncing a wireless access point controller or using Bulk Administration to import wireless access point infrastructure.

## Location Awareness Prerequisites

This feature allows you to synchronize the Cisco Unified Communications Manager database with multiple Cisco Wireless LAN
                              Controllers. You must also set up your Cisco Wireless LAN Controller hardware and  your infrastructure of access points. For
                              details, see your controller documentation.

## Location Awareness Configuration Task Flow

Complete the following tasks to set up Location Awareness in Cisco Unified Communications Manager.

### Before you begin

Step 1

Start Services for Wireless Infrastructure Synchronization

In Cisco Unified Serviceability, start services that support the Location Awareness feature.

Step 2

Configure Wireless Access Point Controller

Synchronize the database with a Cisco wireless access point controller. The sync imports the wireless infrastructure into
                                          the database.

Tip

Set up a sync schedule for automatic updates.

Step 3

Insert Infrastructure Devices

Optional. If you want to add your wireless infrastructure from Cisco Prime Infrastructure, or if you are using a third-party
                                          wireless LAN controller, use Bulk Administration to update the database from a CSV file.

Step 4

Deactivate Infrastructure Device from Tracking

Optional. If your synchronization includes access points that you do not want to track (for example, if the synchronization
                                          pulls in access points from  a lab), you can deactivate the access point and Cisco Unified Communications Manager will not
                                          track updates to the access point.

### Start Services for Wireless Infrastructure Synchronization

Use this procedure to start services that support synchronization with a Cisco Wireless LAN Controller in support of the Location
                                 Awareness feature.

Step 1

Log in to Cisco Unified Serviceability and choose Tools > Service Activation .

Step 2

From the Server drop-down list, select the publisher node.

Step 3

Make sure that the following services are checked:

- Cisco CallManager

- Cisco AXL Web Service

- Cisco Wireless Controller Synchronization Service

Step 4

Optional. If you want to use Bulk Administration to import your network infrastructure from a CSV file, make sure that Bulk Provisioning Service is checked.

Step 5

Click Save .

### Configure Wireless Access Point Controller

Use this procedure to synchronize the database with a Cisco wireless access point controller. During the sync, Unified Communications Manager updates its database with the wireless access point infrastructure that the controller manages. You can add up to fifty wireless
                                 access point controllers.

Step 1

From Cisco Unified CM Administration, choose Advanced Features > Device Location Tracking Services > Wireless Access Point Controllers .

Step 2

Select the controller that you want to configure:

- Click Find and select the controller to edit an existing controller.

- Click Add New to add a new controller.

Step 3

In the Name field, enter the IP address or hostname for the controller.

Step 4

Enter a Description for the controller.

Step 5

Complete the SNMP settings that will be used for SNMP messaging to the controller:

From the SNMP Version drop-down list, select the SNMP version protocol that the controller uses.

Complete the remaining SNMP authentication fields. For more information on the fields and their configuration options, see Online Help.

Click the Test SNMP Settings to confirm that you entered valid SNMP settings.

Step 6

If you want to configure scheduled syncs to regularly update the database:

Check the Enable scheduled synchronization to discover Infrastructure Devices check box.

In the Perform a Re-sync Every fields, create the synchronization schedule.

Step 7

Click Save .

Step 8

(Optional) To update the database immediately, click Synchronize .

Optional . If the synchronization pulls in access points that you do not want to track (for example, lab equipment or access points
                                 that are not in use) you can remove the access point from tracking.

### Insert Infrastructure Devices

Use this procedure to complete a bulk import of your wireless Access Point infrastructure from a CSV file into the Unified Communications Manager database. You can use this procedure to import a CSV file that was exported from Cisco Prime Infrastructure or if you want
                                 to import access points from a third-party wireless Access Point controller.

#### Before you begin

You must have a data file
                                 			 in comma separated value (CSV) format with the following delineated columns:

AccessPoint or Switch Name

IPv4 Address

IPv6 Address

BSSID—Required for Wireless Access Protocol (WAP) infrastructure devices

Description—A location identifier, a combination of switch type and location, or another meaningful identifier

You can define both an IPv4 and IPv6 address, or you can define an IPv4 or an IPv6 address.

For the BSSID value, enter the BSSID mask, ending in 0, that uniquely identifies the access point as opposed to the BSSIDs
                                             for the individual channels on the access point.

Step 1

Choose Bulk
                                                				  Administration > Infrastructure Device > Insert Infrastructure
                                                				  Device .

Step 2

In the File
                                             				Name field, choose the CSV data file that you created for this
                                          			 transaction.

Step 3

In the Job
                                             			 Information area, enter the Job description.

The default
                                             				description is Insert Infrastructure Device .

Step 4

Select when you want to run the job:

- Select the Run Immediately radio button, if you want to run the job immediately.

- Select the Run Later radio button, if you want to schedule the job for later.

Step 5

Click Submit .

Step 6

If you chose to run the job later, schedule when the job runs:

Choose Bulk Administration > Job Scheduler .

Click Find and select the job that you just created.

In the Job Scheduler window, schedule when you want to run the job.

Click Save .

### Deactivate Infrastructure Device from Tracking

If the synchronization includes access points or switches that you do not want to track (for example, if the sync pulls in
                                 lab equipment or access points that are not in use), you can deactivate the access point or switch from tracking. Unified
                                 Communications Manager will not update the status for the access point or switch.

Step 1

In Cisco Unified CM Administration, choose Advanced Features > Device Location Tracking Services > Switches and Access Points .

Step 2

Click Find and select the switch or access point that you want to stop tracking.

Step 3

Click Deactivate Selected .

### Related Documentation

After you complete your system configuration, and your system is up and running, you can use tasks in the following chapter
                                 to manage your infrastructure on an ongoing basis:

"Manage Infrastructure", Administration Guide for Cisco Unified Communications Manager and IM and Presence Service

## Location Awareness Restrictions

Feature

Interactions and Restrictions

Meraki Access Points

The Location Awareness feature does not support Meraki access points.

| Important | Meraki Access Points support for Location Awareness is applicable only from Release 12.5(1)SU6 onwards and Release 14SU1 onwards. |
|---|---|

| Note | Currently, wired phones do not support Location Awareness. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Start Services for Wireless Infrastructure Synchronization | In Cisco Unified Serviceability, start services that support the Location Awareness feature. |
| Step 2 | Configure Wireless Access Point Controller | Synchronize the database with a Cisco wireless access point controller. The sync imports the wireless infrastructure into
                                          the database. Tip Set up a sync schedule for automatic updates. | Tip | Set up a sync schedule for automatic updates. |
| Tip | Set up a sync schedule for automatic updates. |
| Step 3 | Insert Infrastructure Devices | Optional. If you want to add your wireless infrastructure from Cisco Prime Infrastructure, or if you are using a third-party
                                          wireless LAN controller, use Bulk Administration to update the database from a CSV file. Note This method does not allow you to set up automatic updates. | Note | This method does not allow you to set up automatic updates. |
| Note | This method does not allow you to set up automatic updates. |
| Step 4 | Deactivate Infrastructure Device from Tracking | Optional. If your synchronization includes access points that you do not want to track (for example, if the synchronization
                                          pulls in access points from  a lab), you can deactivate the access point and Cisco Unified Communications Manager will not
                                          track updates to the access point. |

| Tip | Set up a sync schedule for automatic updates. |
|---|---|

| Note | This method does not allow you to set up automatic updates. |
|---|---|

| Step 1 | Log in to Cisco Unified Serviceability and choose Tools > Service Activation . |
|---|---|
| Step 2 | From the Server drop-down list, select the publisher node. |
| Step 3 | Make sure that the following services are checked: Cisco CallManager Cisco AXL Web Service Cisco Wireless Controller Synchronization Service |
| Step 4 | Optional. If you want to use Bulk Administration to import your network infrastructure from a CSV file, make sure that Bulk Provisioning Service is checked. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Advanced Features > Device Location Tracking Services > Wireless Access Point Controllers . |
|---|---|
| Step 2 | Select the controller that you want to configure: Click Find and select the controller to edit an existing controller. Click Add New to add a new controller. |
| Step 3 | In the Name field, enter the IP address or hostname for the controller. |
| Step 4 | Enter a Description for the controller. |
| Step 5 | Complete the SNMP settings that will be used for SNMP messaging to the controller: From the SNMP Version drop-down list, select the SNMP version protocol that the controller uses. Complete the remaining SNMP authentication fields. For more information on the fields and their configuration options, see Online Help. Click the Test SNMP Settings to confirm that you entered valid SNMP settings. |
| Step 6 | If you want to configure scheduled syncs to regularly update the database: Check the Enable scheduled synchronization to discover Infrastructure Devices check box. In the Perform a Re-sync Every fields, create the synchronization schedule. |
| Step 7 | Click Save . |
| Step 8 | (Optional) To update the database immediately, click Synchronize . |

| Note | You can define both an IPv4 and IPv6 address, or you can define an IPv4 or an IPv6 address. |
|---|---|

| Note | For the BSSID value, enter the BSSID mask, ending in 0, that uniquely identifies the access point as opposed to the BSSIDs
                                             for the individual channels on the access point. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > Infrastructure Device > Insert Infrastructure
                                                				  Device . The Insert
                                             				Infrastructure Device Configuration window displays. |
|---|---|
| Step 2 | In the File
                                             				Name field, choose the CSV data file that you created for this
                                          			 transaction. |
| Step 3 | In the Job
                                             			 Information area, enter the Job description. The default
                                             				description is Insert Infrastructure Device . |
| Step 4 | Select when you want to run the job: Select the Run Immediately radio button, if you want to run the job immediately. Select the Run Later radio button, if you want to schedule the job for later. |
| Step 5 | Click Submit . If you chose to run the job immediately, the job runs. |
| Step 6 | If you chose to run the job later, schedule when the job runs: Choose Bulk Administration > Job Scheduler . Click Find and select the job that you just created. In the Job Scheduler window, schedule when you want to run the job. Click Save . At the scheduled time, the job runs. |

| Step 1 | In Cisco Unified CM Administration, choose Advanced Features > Device Location Tracking Services > Switches and Access Points . |
|---|---|
| Step 2 | Click Find and select the switch or access point that you want to stop tracking. |
| Step 3 | Click Deactivate Selected . |

| Feature | Interactions and Restrictions |
|---|---|
| Meraki Access Points | The Location Awareness feature does not support Meraki access points. |