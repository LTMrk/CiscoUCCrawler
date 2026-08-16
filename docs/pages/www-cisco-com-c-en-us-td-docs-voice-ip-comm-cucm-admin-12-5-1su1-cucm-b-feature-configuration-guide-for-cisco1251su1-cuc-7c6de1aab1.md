---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su1-cucm-b-feature-configuration-guide-for-cisco1251su1-cuc-7c6de1aab1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU1/cucm_b_feature-configuration-guide-for-cisco1251SU1/cucm_b_feature-configuration-guide-for-cisco1251SU2_chapter_0101.html
retrieved_at: 2026-08-16T17:17:06.891425+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

Updated: July 31, 2025

Chapter: Remote Worker Emergency Calling

## Chapter: Remote Worker Emergency Calling

# Remote Worker Emergency Calling

## Remote Worker
                        	 Emergency Calling Overview

The Remote Worker
                           		Emergency Calling feature enables customers to provide reliable emergency
                           		calling support to remote workers by using remote Virtual Private Network (VPN)
                           		connections. Emergency calls from off-premises users are routed to the Public
                           		Safety Answering Point (PSAP), and user-provided location information is
                           		delivered with each call.

To use this feature,
                           		remote workers must confirm or update their location whenever their device
                           		registration is interrupted. A customizable disclaimer notice is first
                           		displayed on the devices that are designated for off-premises (connected
                           		remotely to the customer network), which advises the users to provide correct
                           		location information. After the location information is provided, the
                           		off-premises location that is currently associated with the designated device
                           		is displayed. Users can confirm their current location or select another
                           		previously stored location from their device display; if their location is new,
                           		they are directed to the Cisco Emergency Responder Off-Premises User web page
                           		to create a new location.

Before completing
                           		this process, the administrator may restrict the device to calling a single
                           		configured destination. This action ensures that the device user has
                           		acknowledged the disclaimer and provided current location information before
                           		the device is enabled for normal use.

## Remote Worker
                        	 Emergency Calling Prerequisites

## Remote Worker
                        	 Emergency Calling Configuration Task Flow

### Before you begin

Step 1

Configure User As a Remote Worker

Step 2

Specify Alternate Routing for Emergency Calling

Step 3

Configure the Application Server

Step 4

Configure E911 Messages

### Configure User As
                           	 a Remote Worker

#### Before you begin

Ensure that you have configured Intrado on the Cisco Emergency Responder . For more information about configuring Intrado on the Cisco Emergency Responder , see Cisco Emergency Responder Administration Guide .

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Enter the
                                          			 appropriate search criteria to find the phone and click Find .

Step 3

Choose the
                                          			 phone for which you want to configure Remote Worker Emergency Calling.

Step 4

From the Device Information section, select the appropriate user ID from the Owner User ID drop-down list and check the Require off-premise location check box.

Step 5

Click Save .

### Specify
                           	 Alternate Routing for Emergency Calling

Perform the
                                 		  following steps to configure calling search space and destination number. These
                                 		  parameters are used to restrict the routing of any call made from a registered
                                 		  off-premises device where the user has not set a location. If you do not
                                 		  configure these parameters, the calls are routed normally.

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose a server.

Step 3

From the Service drop-down list, choose Cisco CallManager .

Step 4

In the Clusterwide Parameters (Emergency Calling for Required Off-premise Location) section, specify Alternate Destination for
                                             				  Emergency Call .

Step 5

Specify Alternate Calling Search
                                             				  Space for Emergency Call .

Step 6

Click Save .

### Configure
                           	 the Application Server

You must configure the application server to enable the E911 Proxy to communicate with the Cisco Emergency Responder . E911 proxy is used to direct the users to the application server where they enter the location of the device.

Step 1

From Cisco Unified CM Administration, choose System > Application Server .

Step 2

Click Add
                                             				New .

Step 3

From the Application Server Type drop-down list, select CER
                                             				Location Management .

Step 4

Click Next .

Step 5

In the Name field, specify a name to identify the
                                          			 application server that you are configuring.

Step 6

In the IP
                                             				address field, specify the IP address of the server that you are
                                          			 configuring.

Step 7

From the list
                                          			 of Available Application Users , select the application
                                          			 user and click the Down arrow.

Step 8

In the End
                                             				User URL field, enter a URL for the end users that are associated
                                          			 with this application server.

Step 9

Click Save .

### Configure E911
                           	 Messages

Use the following
                                 		  procedure to select and edit E911 messages for off-premises devices.

Step 1

From Cisco Unified CM Administration, choose System > E911 Messages .

Step 2

Select the
                                          			 required language link of the E911 messages.

The E911 Messages
                                                				  Configuration page displays the Agreement, Disclaimer, and Error
                                             				messages.

Step 3

(Optional) Edit the E911 messages to be displayed on off-premises devices.

Step 4

Click Save .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure User As a Remote Worker | Associate the
                                       			 off-premises device with the owner of the device. |
| Step 2 | Specify Alternate Routing for Emergency Calling | These parameters specify the calling search space and destination number that are used to restrict the routing of any call
                                       that is made from a registered off-premises device where the user chose not to set a location. If these parameters are not
                                       configured, calls are routed normally. |
| Step 3 | Configure the Application Server | Direct end
                                       			 users to the application server where they enter the location of the device. |
| Step 4 | Configure E911 Messages | Configure the
                                       			 E911 messages that appear on an off-premises end-user phone. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Enter the
                                          			 appropriate search criteria to find the phone and click Find . A list
                                          			 of phones that match the search criteria is displayed. |
| Step 3 | Choose the
                                          			 phone for which you want to configure Remote Worker Emergency Calling. The Phone
                                             				Configuration window is displayed. |
| Step 4 | From the Device Information section, select the appropriate user ID from the Owner User ID drop-down list and check the Require off-premise location check box. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose a server. |
| Step 3 | From the Service drop-down list, choose Cisco CallManager . The Service Parameter Configuration window appeares. |
| Step 4 | In the Clusterwide Parameters (Emergency Calling for Required Off-premise Location) section, specify Alternate Destination for
                                             				  Emergency Call . |
| Step 5 | Specify Alternate Calling Search
                                             				  Space for Emergency Call . |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Application Server . |
|---|---|
| Step 2 | Click Add
                                             				New . The Application Server window appears. |
| Step 3 | From the Application Server Type drop-down list, select CER
                                             				Location Management . |
| Step 4 | Click Next . |
| Step 5 | In the Name field, specify a name to identify the
                                          			 application server that you are configuring. |
| Step 6 | In the IP
                                             				address field, specify the IP address of the server that you are
                                          			 configuring. |
| Step 7 | From the list
                                          			 of Available Application Users , select the application
                                          			 user and click the Down arrow. |
| Step 8 | In the End
                                             				User URL field, enter a URL for the end users that are associated
                                          			 with this application server. |
| Step 9 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > E911 Messages . |
|---|---|
| Step 2 | Select the
                                          			 required language link of the E911 messages. The E911 Messages
                                                				  Configuration page displays the Agreement, Disclaimer, and Error
                                             				messages. |
| Step 3 | (Optional) Edit the E911 messages to be displayed on off-premises devices. |
| Step 4 | Click Save . |