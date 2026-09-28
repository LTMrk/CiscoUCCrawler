---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su6-cucm-b-feature-configuration-guide-for-cisco12su6-cucm--b9f82ca00e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU6/cucm_b_feature-configuration-guide-for-cisco12su6/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_011000.html
retrieved_at: 2026-08-16T16:36:45.606942+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: October 8, 2025

Chapter: Paging

## Chapter: Paging

# Paging

## Paging
                        	 Overview

Unified Communications Manager can be configured to integrate with Cisco Paging Server to provide basic paging services for Cisco Unified IP Phone and a variety of endpoints. The Cisco Paging Server product is offered through the InformaCast Virtual Appliance and offers
                           the following deployment options:

### InformaCast Basic Paging

InformaCast Basic Paging provides phone-to-phone live audio paging to individual Cisco IP phones or groups of up to 50 phones
                              simultaneously. InformaCast Basic Paging is free to all Unified Communications Manager customers and all Cisco Business Edition 6000 and Cisco Business Edition 7000 customers.

### InformaCast
                           	 Advanced Notification

InformaCast Advanced
                              		Notification is a full-featured emergency notification and paging solution that
                              		allows you to reach an unlimited number of Cisco IP phones and various devices
                              		and systems with text and audio messages.

To streamline the configuration process, Unified Communications Manager comes with a provisioning wizard that allows you to quickly configure advanced notifications services.

Some of the features
                              		include:

Text and audio
                                    			 (live or pre-recorded) to Cisco IP Phones and other endpoints

Analog and IP
                                    			 overhead paging systems integration

911 or emergency
                                    			 call monitoring or alerting or recording

Cisco Jabber
                                    			 integration

Cisco Spark
                                    			 integration

Automated
                                    			 weather notifications

Dynamically
                                    			 triggered emergency conference calls

Pre-recorded or
                                    			 scheduled broadcasts (school bells or shift changes)

Event
                                    			 accountability with message confirmation and reporting

Notification to
                                    			 computer desktops (Windows and Mac OS)

Facilities
                                    			 integration (control lighting, door locks)

Security
                                    			 integration (panic or duress buttons, motion detectors, fire)

Purchase a license
                              		key to access InformaCast Advanced Notification features.

### InformaCast
                           	 Mobile

InformaCast Mobile
                              		is a cloud-based service that allows users to send images, text, and
                              		pre-recorded audio to mobile devices running iOS or Android. It also has
                              		bi-directional integration with InformaCast Advanced Notification.

Some of the features
                              		include:

The ability to
                                    			 send and receive InformaCast messages via mobile devices running iOS or Android

Bi-directional
                                    			 integration with InformaCast Advanced Notification

Message
                                    			 confirmations and read receipts

No calling or
                                    			 SMS messaging fees

InformaCast Mobile
                              		must be purchased direct from Singlewire Software. Please refer to the
                              		Singlewire website for addtional details and downloads.

If you have already configured Unified Communications Manager to integrate with InformaCast Advanced Notification, no further configuration of Unified Communications Manager is required.

## Paging
                        	 Prerequisites

Cisco Paging
                              		  Server is designed to work in a multicast environment. You must configure your
                              		  network for multicast.

For a list of
                              		  Cisco Unified IP Phones that support paging, refer to the Cisco
                                 			 Unified IP Phones section of the Singlewire Compatibility Matrix
                              		  at:

## Cisco Unified Communications Manager Configuration for Basic Paging Task Flow

Perform the following tasks to configure Unified Communications Manager to integrate with Cisco Paging Server for an InformaCast Basic Paging deployment.

### Before you begin

Learn more about the feature by reviewing the following:

Paging Overview

InformaCast Basic Paging

Review Paging Prerequisites

The configuration in this section is automated when using the Emergency Notifications Paging wizard.

Step 1

Enable SNMP Service

Configure SNMP in Unified Communications Manager .

Step 2

Set Default Codec to G.711

Set the default codec to G.711.

Step 3

Configure a Device Pool for Paging

Configure a device pool.

Step 4

Configure Route Partition for InformaCast Paging

Configure a route partition for Basic Paging.

Step 5

Configure Calling Search Space for InformaCast Paging

Configure a calling search space for Basic Paging.

Step 6

Configure CTI Ports for Paging

Configure CTI ports.

Step 7

Configure Access Control Group with AXL Access

Configure an AXL access control group.

Step 8

Configure Application User for Paging

Configure an application user.

Step 9

Enable web access for the phone using one of the following
                                       			 procedures:

- Enable Web Access for a Phone

- Enable Web Access for Common Phone Profile

- Enable Web Access for Enterprise Phone Configuration

You can enable web access on all phones globally using Enterprise
                                          				Phone Configuration, a group of phones using a Common Phone Profile, or an
                                          				individual phone.

Step 10

Configure Authentication URL

Configure the Unified Communications Manager authentication URL to point to InformaCast so that when InformaCast pushes broadcasts to Cisco Unified IP Phone , the phones will authenticate with InformaCast.

For detailed procedures on how to configure Cisco Unified Communications Manager and Cisco Paging Server, refer to the InformaCast Virtual Appliance Basic Paging Installation and User Guide .

### Configure SNMP for
                           	 Paging

Perform the
                                 		  following tasks to configure SNMP services in the cluster.

Step 1

Enable SNMP Service

Enable the
                                             				SNMP and other services in the cluster.

Step 2

Create an InformaCast SNMP Community String

Configure an
                                             				SNMP community string.

#### Enable SNMP
                              	 Service

To configure
                                    		  paging,
                                    		  you must enable SNMP on every node in the cluster. In addition, you must enable
                                    		  the following services:

Cisco
                                          				CallManager SNMP Service—Enable on all nodes in the cluster.

Cisco CallManager—Enable on at least one node.

Cisco AXL Web
                                          				Services—Enable on at least one node.

Cisco
                                          				CTIManager—Enable on at least one node.

Step 1

From Cisco Unified Serviceability, choose Tools > Service Activation .

Step 2

From the Server drop-down list, choose the server on which you want to configure SNMP.

Step 3

Check the
                                             			 check boxes that correspond to the Cisco
                                                				CallManager SNMP Service .

Step 4

For at least one server in the cluster, check the check boxes that
                                             			 correspond to Cisco CallManager , Cisco CTIManager , and Cisco AXL Web Service services.

Step 5

Click Save .

Step 6

Click OK .

Step 7

Repeat the
                                             			 previous steps for all nodes in the cluster.

#### Create an
                              	 InformaCast SNMP Community String

Perform this
                                    		  procedure for Basic Paging 
                                    		  
                                    		  to set up an SNMP community string.

##### Before you begin

Enable SNMP Service

Step 1

From Cisco Unified Serviceability, choose SNMP > V1/V2c > Community String .

Step 2

From the Server drop-down list, choose a server and click Find .

Step 3

Click Add
                                                				New .

Step 4

In the Community String Name field, enter ICVA .

Step 5

From the Access Privileges drop-down list, select ReadOnly .

Step 6

Check the Apply
                                                				to All Nodes check box if the check box is active.

Step 7

Click Save .

Step 8

Click OK .

##### What to do next

Set Default Codec to G.711

### Configure Region
                           	 for Paging

For Basic Paging, you must
                                 		  set up a region for your paging deployment.

Step 1

Set Default Codec to G.711

Create a
                                             				region that uses the G.711 codec for calls to other regions.

Step 2

Configure a Device Pool for Paging

Set up a
                                             				device pool for paging and assign the region that you created to that device
                                             				pool.

#### Set Default Codec to G.711

You must create an InformaCast region that uses G.711 as the default codec for calls to other regions.

##### Before you begin

Configure SNMP for Paging

Step 1

From Cisco Unified CM Administration, choose System > Region Information > Region .

Step 2

Click Add New .

Step 3

In the Name field, enter ICVA .

Step 4

Click Save .

Step 5

In the Regions text box, select all regions by pressing the CTRL key and clicking all of the selected regions.

Step 6

From the Maximum Audio Bit Rate drop-down list, select 64 kbps (G.722, G.711) .

Step 7

From the Maximum Session Bit Rate for Video Calls column click the None radio button.

Step 8

Click Save .

#### Configure a Device
                              	 Pool for Paging

Perform this
                                    		  procedure to configure a device pool for your
                                    		  paging deployment.

##### Before you begin

Set Default Codec to G.711

Step 1

From Cisco Unified CM Administration, choose System > Device Pool .

Step 2

Click Add
                                                				New .

Step 3

In the Device
                                                				Pool Name field, enter ICVA .

Step 4

From the Cisco Unified Communications Manager Group drop-down list, select the group that contains the Cisco Unified Communications Manager cluster with which the InformaCast
                                             Virtual Appliance will communicate.

Step 5

From the Date/Time Group drop-down list, select a date/time group. Select CMLocal unless you are performing dialing restrictions by the time of day.

Step 6

From the Region drop-down list, choose ICVA .

Step 7

From the SRST Reference drop-down list, select Disable .

Step 8

Click Save .

### Configure
                           	 Partitions and Calling Search Spaces for Paging

Perform the
                                 		  following tasks to configure a partition and calling search space (CSS) for
                                 		  paging as follows:

For Basic
                                       				Paging deployments, create a single partition and CSS for InformaCast paging.

Step 1

Configure Route Partition for InformaCast Paging

Configure a
                                             				route partition for InformaCast paging.

Step 2

Configure Calling Search Space for InformaCast Paging

Configure a
                                             				calling search space for InformaCast paging.

#### Configure Route Partition for InformaCast Paging

Create a route partition for InformaCast paging.

##### Before you begin

Configure a Device Pool for Paging

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Route Partitions .

Step 2

Click Add New .

Step 3

In the Name field, enter the following name and description for the partition: ICVA-CTIOutbound,ICVA-Do not add to any phone CSS .

Step 4

Click Save .

#### Configure Calling
                              	 Search Space for InformaCast Paging

Perform this
                                    		  procedure to configure a calling search space for InformaCast paging.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Calling Search Space .

Step 2

Click Add
                                                				New .

Step 3

In the Name field, enter ICVA .

Step 4

In the Available Partitions list box, use the arrows to
                                             			 move the following partitions to the Selected Partitions list box.

- The partition that you
                                                				created for InformaCast paging

- The partitions that contain
                                                				your users' extensions and any analog paging extensions

Step 5

Click Save .

### Configure CTI
                           	 Ports for Paging

Perform this
                                 		  procedure to configure CTI ports for your paging deployment. The number of CTI
                                 		  ports that you need depends on your deployment type and your applications'
                                 		  usage:

For Basic
                                       				Paging deployments, you must create a minimum of two CTI ports for InformaCast
                                       				paging.

#### Before you begin

Configure Calling Search Space for InformaCast Paging

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Add
                                             				New .

Step 3

From the Phone Type drop-down list, choose CTI Port .

Step 4

In the Device
                                             				Name field, enter a name for the CTI Port. For example, ICVA-IC-001 for an InformaCast port.

Step 5

In the Description field, enter a description for the port.
                                          			 For example, InformaCast Recording Port for Call
                                             				Monitoring .

Step 6

From the Device Pool drop-down list, select ICVA .

Step 7

From the Calling Search Space drop-down list, select ICVA .

Step 8

From the Device Security Profile drop-down list, select Cisco CTI Port - Standard SCCP Non-Secure Profile .

Step 9

Click Save .

Step 10

Click OK .

Step 11

In the left
                                          			 association area, click Line
                                             				[1] - Add a new DN .

Step 12

In the Directory Number field, enter a directory number.
                                          			 This directory number should not be used for any purpose other than making
                                          			 paging calls. It should not be assigned to a phone and should not be within a
                                          			 direct-inward-dialing range.

Step 13

In the Route Partition drop-down list, select the following ports:

- For InformaCast ports, select ICVA-CTIOutbound .

Step 14

In the Display (Internal Caller ID) text box, enter InformaCast .

Step 15

In the ASCII
                                             				Display (Internal Caller ID) text box, enter InformaCast .

Step 16

Click Save .

Step 17

Repeat this
                                          			 procedure for each CTI port that you need.

#### What to do next

### Configure Access
                           	 Control Group with AXL Access

Perform this
                                 		  procedure 
                                 		  to create an access control group that includes AXL access.

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > Access Control Group .

Step 2

Click Add
                                             				New .

Step 3

In the Name text box, enter ICVA
                                             				User Group .

Step 4

Click Save .

Step 5

From the Related Links drop-down list, select Back to Find/List and click Go .

Step 6

In the Roles column, click the i icon that corresponds to the new access control group.

Step 7

Click Assign
                                             				Role to Group .

Step 8

Click Find .

Step 9

Select Standard AXL API Access check box, and click Add
                                             				Selected .

Step 10

Click Save .

### Configure
                           	 Application User for Paging

Perform this
                                 		  procedure to configure an application user:

For Basic
                                       				Paging, configure an InformaCast application user.

Step 1

From Cisco Unified CM Administration, choose User Management > Application User .

Step 2

Click Add
                                             				New .

Step 3

In the User
                                             				ID text box, enter a user ID for the application user. For
                                          			 example, ICVA
                                             				InformaCast .

Step 4

Enter a
                                          			 password in the Password and Confirm Password fields.

Step 5

In the Available Devices list box, click the CTI ports that
                                          			 you created for your deployment and use the arrows to move the devices to the Controlled Devices list box. For example, select ICVA-IC-001 for InformaCast and ICVA-CA-001 for CallAware.

Step 6

Click the Add to Access Control Group .

Step 7

Click Find .

Step 8

Check the
                                          			 following check boxes (unless otherwise indicated, select these permissions for
                                          			 all application users):

- ICVA User Group

- Standard CTI Allow Control
                                             				of All Devices

- Standard CTI Allow Control
                                             				of Phones supporting Connected Xfer and conf

- Standard CTI Allow Control
                                             				of Phones supporting Rollover Mode

- Standard CTI Enabled

Step 9

Click Add
                                             				Selected .

Step 10

Click Save .

### Enable Web Access
                           	 for a Phone

Perform this procedure in Basic Paging to enable web access for a Cisco Unified IP Phone . You can also use a Common Phone Profile to enable web access for a group of phones that use that profile. For details, see Enable Web Access for Common Phone Profile .

#### Before you begin

Configure Application User for Paging

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find and select the phone for which you want to
                                          			 enable web access.

Step 3

In the Product Specific Configuration Layout area, from the Web Access drop-down list, select Enabled .

Step 4

Click Save .

#### What to do next

Configure Authentication URL

### Enable Web Access
                           	 for Common Phone Profile

Perform this
                                 		  procedure in 
                                 		  Basic Paging to enable web access for a group of Cisco Unified IP Phones
                                 		  that use a Common Phone Profile. You can also enable web access on an
                                 		  individual phone. For details, see Enable Web Access for a Phone .

#### Before you begin

Configure Application User for Paging

Step 1

From Cisco Unified CM Administration, choose I Device > Device Settings > Common Phone Profile .

Step 2

Click Find and select the profile that applies to the
                                          			 group of phones for which you want to enable web access.

Step 3

In the Product Specific Configuration Layout area, from the Web
                                             				Access drop-down list, select Enable .

Step 4

Click Save .

Step 5

Click Apply
                                             				Config to reset the phones that use the Common Phone Profile.

Step 6

Click OK .

#### What to do next

Configure Authentication URL

### Enable Web Access
                           	 for Enterprise Phone Configuration

Perform this procedure in Unified Communications Manager to enable web access for a group of Cisco Unified IP Phone that use a Common Phone Profile. You can also enable web access on an individual phone. For more details, see Enable Web Access for a Phone .

#### Before you begin

Configure Application User for Paging .

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Phone Configuration .

Step 2

From the Web
                                             				Access drop-down list, select Enable .

Step 3

Click Save .

Step 4

Click Apply
                                             				Config to reset the phones that use the Common Phone Profile.

Step 5

Click OK .

### Configure
                           	 Authentication URL

Perform the following tasks to configure an authentication URL that points to InformaCast so that when InformaCast pushes
                                 broadcasts to Cisco Unified IP Phones, the phones authenticate with InformaCast instead of Unified Communications Manager .

Step 1

Set Authentication URL

Set the Unified Communications Manager authentication URL to point InformaCast.

Step 2

Reset Your Phones

Reset the phones in your deployment so that your phones use the new settings.

Step 3

Test Your Phones

Verify that
                                             				the phones in your deployment use the new authentication URL settings.

#### Set Authentication
                              	 URL

Perform this procedure to set the Unified Communications Manager authentication URL to point to the InformaCast Virtual Appliance.

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Parameters .

Step 2

Scroll to the Phone
                                                				URL Parameters area, and in the URL
                                                				Authentication field, enter http://<IP
                                                				Address>:8081/InformaCast/phone/auth where <IP Address> is
                                             			 the IP Address of the InformaCast Virtual Appliance.

Make a note
                                                            				  of the existing URL in the URL Authentication field. You may need this when you
                                                            				  configure InformaCast. See your InformaCast documentation for details.

Step 3

Scroll to the Secured Phone URL Parameters area, and in the Secured Authentication URL field, enter http://<IP
                                                				Address>:8081/InformaCast/phone/auth where <IP Address> is
                                             			 the IP Address of the InformaCast Virtual Appliance.

Step 4

Click Save .

#### Reset Your Phones

After you set the authentication URL to point to the InformaCast Virtual Applicance, you must reset your phones. This procedures
                                    describes how to manually reset the phones in device pools. There are many methods for resetting your phones. For example,
                                    you can also use Bulk Administration Tool to schedule the reset during off hours. See the Cisco Unified Communications Manager Bulk Administration Guide for information on the Bulk Administration Tool.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

In the From Phone Where box, select Device Pool .

Step 3

Set the other drop-down menus and field items to settings that will bring up the device pools that you contain your phones.

Step 4

Click Find .

Step 5

Select the device pools that you want to reset.

Step 6

Click Reset Selected .

Step 7

Click Reset .

#### Test Your
                              	 Phones

Verify that your
                                    		  phones are authenticating with the InformaCast Virtual Appliance.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Use the drop-down list and fields in the Find and List Phones window to filter your search for a phone that should be using
                                             the new authentication URL, and click Find .

Step 3

For the phone
                                             			 that should be using the new settings, click the IP Address link in the IPv4
                                                				Address column.

Step 4

Click Network
                                             			 Configuration.

Step 5

Verify that
                                             			 the Authentication URL field displays the InformaCast
                                             			 Virtual Appliance IP address that you entered for the URL
                                                				Authentication enterprise parameter. If the correct URL does not
                                             			 appear, you will need to set the authentication URL.

## Advanced
                        	 Notification Paging Configuration Task Flow

Perform the following tasks to integrate InformaCast Paging Server with Unified Communications Manager for IP paging and emergency call alerting. It includes the following features:

InformaCast
                                    				advanced notification

Panic button
                                    				configuration

Text and audio
                                    				notification to IP phones when a user dials an emergency services number
                                    				(CallAware)

Step 1

Install the InformaCast Virtual Appliance .

Download the
                                          				InformaCast OVA file from the Singlewire website and
                                          				upload it to vSphere.

Step 2

Configure Connection to InformaCast .

Configure Unified Communications Manager and InformaCast.

Step 3

Configure Panic Button .

Configure a
                                          				panic button to send a text and audio notification to IP phones.

Step 4

Configure CallAware Emergency Call Alerting .

Configure
                                          				emergency call text and audio notifications.

### Install the
                           	 InformaCast Virtual Appliance

Singlewire
                                 		  supports InformaCast Virtual Appliance on the VMware ESXi platform, which is
                                 		  managed through the vSphere client.

To view a list
                                             			 of Singlewire-supported VMware ESXi versions, go to this URL: https://www.singlewire.com/compatibility-matrix and click the Server
                                             			 Platforms link under InformaCast Platform section.

If you have
                                             			 purchased a license, refer to https://www.singlewire.com/icva-kb-activate to activate your license.
                                             			 This will ensure that Emergency Notifications stay active after the 90-day
                                             			 trial.

For more
                                             			 details on the installation, including InformaCast screen captures, go to this
                                             			 URL: https://www.singlewire.com/icva-kb-install .

#### Before you begin

Import InformaCast
                                 		  Virtual Appliance using the vSphere client. This can be downloaded from your
                                 		  VMware server.

Step 1

Download the
                                          			 OVA file from the Singlewire website and
                                          			 then log in to the vSphere client.

If you are
                                                         				  using InformaCast on the Communications Manager Business Edition 6000, you are
                                                         				  supplied with a DVD in a package with an OVA on it (physical media).

Step 2

From the vSphere
                                             				Client window, choose File > Deploy OVF
                                                				  Template .

Step 3

Click the Deploy
                                             				from File radio button and then click Browse to select the saved the OVA file (or to the
                                          			 OVA file on the supplied DVD). After you select the OVA file, click Open .

Step 4

Click Next to continue.

Step 5

Click Next to verify the Name
                                             				and Location , and then click Next to select the network to store the new virtual
                                          			 machine files.

Tip

It is good
                                                         				  practice to place the Virtual Appliance on the same VLAN as your Cisco Unified Communications Manager .

Step 6

Click Next to continue, and then click Finish .

Step 7

From the vSphere
                                             				Client window, click Hosts
                                             				and Clusters icon and then select your host server.

Step 8

Click the Configuration tab and select the Virtual Machine Startup/Shutdown link in the Software section.

Step 9

Click the Properties link.

Step 10

Check the Allow
                                             				virtual machines to start and stop automatically with the system check box under System
                                             				Settings .

Step 11

Under Startup Order , scroll to the Manual
                                             				Startup section and select your virtual machine (by default, this
                                          			 is Singlewire InformaCast VM), and then move it from the Manual
                                             				Startup section to the Automatic Startup section, by using the Move
                                             				Up button. After moving it, click OK .

Step 12

Choose View > Inventory > VMs and
                                                				  Templates and then select your virtual machine.

Step 13

Choose the Inventory > Virtual
                                                				  Machine > Open Console

Step 14

InformaCast
                                          			 configuration starts for the first time. During this configuration, perform the
                                          			 following tasks for the InformaCast Virtual Appliance:

Accept
                                                				  Cisco End User License Agreement (EULA)

Accept
                                                				  Singlewire EULA

Set up
                                                				  hostname

Set up
                                                				  IP address, subnet mask, and default gateway

Set up
                                                				  DNS server IP address and domain name

Set up
                                                				  NTP server IP address or hostname

Set up
                                                				  time zone

Set up
                                                				  Secure Socket Layer (SSL) certificate parameters

Set up
                                                				  SSL subject alternate names (optional)

Set up
                                                				  the OS admin password

Set up
                                                				  the InformaCast and PTT (PushToTalk) admin password. This password is required
                                                				  to connect the Cisco Unified Communications Manager and InformaCast
                                                				  in the Cisco Unified CM Administration, Advanced
                                                      						Features > Emergency Notifications Paging .

Set up
                                                				  security passphrase for backup and communication

Step 15

Click Continue to work with Singlewire InformaCast.

### Configure
                           	 Connection to InformaCast

Use this procedure to load the InformaCast certificate to the Unified Communications Manager Tomcat trust store.

#### Before you begin

Install the InformaCast Virtual Appliance .

Step 1

From Cisco Unified CM Administration, choose Advanced Features > Emergency Notifications Paging .

Step 2

In the Introduction to InformaCast Emergency Notifications page, click Next to continue.

Step 3

In the Installing the InformaCast Virtual Appliance page,
                                          			 click Next to continue.

You should have successfully installed InformaCast Virtual Appliance to configure with the Unified Communications Manager .

Step 4

In the IP
                                             				address of InformaCast VM field, enter either IP address or
                                          			 Hostname.

By default,
                                                         				  the username is stated as admin in the Username to use in InformaCast field, and it is not
                                                         				  editable.

Step 5

In the Password for admin app user field, enter the
                                          			 administrator password of the InformaCast application.

Step 6

Click OK to load the InformaCast certificate to the Unified Communications Manager Tomcat trust store.

Step 7

Click Next .

Activates SNMP service

Configures SNMP Service with locally generated random
                                                   					 credentials

Activates CTI Manager Service

Configures Unified Communications Manager for InformaCast

Creates new region (1 per cluster)

Creates new device pool (1 per cluster)

Creates SIP trunk (1 per cluster)

Creates route group (1 per cluster)

Creates route list

Creates role

Creates app user

Configures InformaCast for Unified Communications Manager

Creates a cluster

Refreshes recipient groups

Sets SIP access to deny

Creates SIP access

### Configure Panic
                           	 Button

Use this procedure
                                 		  to configure a panic button to send a text and audio notification to IP phones.
                                 		  This allows you to initiate a one click alarm if there is emergency.

#### Before you begin

Configure Connection to InformaCast .

Step 1

From Cisco Unified CM Administration, choose Advanced Features > Emergency Notifications Paging .

Step 2

In the Introduction to InformaCast Emergency Notifications page, click Next to continue.

Step 3

In the Installing the InformaCast Virtual Appliance page,
                                          			 click Next to continue.

Step 4

In the Connecting Cisco Unified Communications Manager and InformaCast page, click Next to continue.

Step 5

From the Choose
                                             				pre-recorded message by name drop-down list, select the
                                          			 pre-recorded message to be displayed on Cisco Unified IP phones and various
                                          			 devices and systems in emergency.

You can
                                                         				  change the pre-recorded message in InformaCast administration, as required.

Step 6

In the Enter
                                             				DN to trigger the panic button field, enter the Directory Number
                                          			 (DN), which includes the digits 0 to 9, asterisks (*), and pound signs (#).
                                          			 Default value is ***5.

Step 7

From the Route Partition drop-down list, select a partition to restrict access to the route pattern.

If you do not want to restrict access to the route pattern, select < None > for the partition.

Step 8

Click Choose
                                             				Phones to Send Notification button.

Step 9

From the Phones to Send Notification dialog box, select the
                                          			 Cisco Unified IP phones to send the pre-recorded message. The dial pattern
                                          			 entered by you (for example, ***5) is configured as speed dial on the selected
                                          			 phones.

Step 10

Click Add Rules , to create a new rule for the selected Cisco Unified IP Phone to receive notifications.

Select one of the parameters from the drop-down list. The available options are Device Pool, Description, and Directory Number.

In the second drop-down list, select a criteria from the following options:

Does

Does not

In the third drop-down list, select a criteria from the following options:

Begins with

Ends with

Contains

In the text box, enter the search criterion.

Minimum of one new rule and maximum of new five rules can be created. The Add Rules button gets disabled when five rules are created.

To delete a rule, click Delete Rules .

Click Test Rules , to validate the created rules. When the test rule is completed with more than zero phones, the Next button is enabled.

Phones added to Cisco Unified Communications Manager at a later date that match this rule will be included as recipients in notifications to this group.

Step 11

Click Next .

The wizard performs the following tasks:

Adds a speed dial for the entered DN to the selected phones. If the selected phones have unused speed dials assigned to existing
                                                   phone button templates, this speed dial appears directly on the selected phones. If the selected phones do not have unused
                                                   speed dial buttons, the panic button speed dial is created, but it does not appear on the phone.

Adds route pattern for entered DN in selected partition using created route list.

Creates an InformaCast DialCast entry for the entered DN to send the selected message to the phones matching the selected
                                                   rules.

### Configure
                           	 CallAware Emergency Call Alerting

Use this
                                 		  procedure to configure the CallAware emergency call alerting details. This
                                 		  sends a text and audio notification to IP phones when an emergency number is
                                 		  dialed. It can also detect calls to numbers other than 911.

#### Before you begin

Configure Panic Button .

Step 1

From Cisco Unified CM Administration, choose Advanced Features > Emergency Notifications Paging .

Step 2

In the Introduction to InformaCast Emergency Notifications page, click Next to continue.

Step 3

In the Installing the InformaCast Virtual Appliance page,
                                          			 click Next to continue.

Step 4

In the Connecting Cisco Unified Communications Manager and InformaCast page, click Next to continue.

Step 5

In the Configuring a Panic Button page, click Next to continue.

Step 6

From the Choose
                                             				pre-recorded message by name drop-down list, select the
                                          			 pre-recorded message to be displayed on Cisco Unified IP phones and various
                                          			 devices and systems in emergency.

You can
                                                         				  change the pre-recorded message in InformaCast administration, as required.

Step 7

Click Choose
                                             				Emergency Route Patterns button.

Step 8

From the Route
                                             				Patterns dialog box, select the route patterns by checking the box
                                          			 next to the desired patterns.

Click
                                                				  the Save Selected/Changes button.

Step 9

Click Add Rules , to create a new rule for the selected Cisco Unified IP Phone to receive notifications.

Select one of the parameters from the drop-down list. The available options are Device Pool, Description, and Directory Number.

In the second drop-down list, select a criteria from the following options:

Does

Does not

In the third drop-down list, select a criteria from the following options:

Begins with

Ends with

Contains

In the text box, enter the search criterion.

Minimum of one new rule and maximum of five new rules can be created. The Add Rules button gets disabled when five rules are created.

To delete a rule, click Delete Rules .

Click Test Rules , to validate the created rules. When the test rule is completed with more than zero phones, the Finish button is enabled.

Phones added to Unified Communications Manager at a later date that match this rule will be included as recipients in notifications to this group.

Step 10

Click Finish .

The wizard
                                             				performs the following tasks:

Adds
                                                   					 External Call Control profile for InformaCast

For each
                                                   					 selected route pattern, modify that route pattern to reference the External
                                                   					 Call Control profile

Creates
                                                   					 a recipient group with rules that match phones to receive the notification

Creates
                                                   					 an InformaCast routing request with the selected message and recipient group

The Summary page appears and confirms the successful configuration of InformaCast with Unified Communications Manager . For more information, see https://www.singlewire.com .

## Paging
                        	 Interactions

Advanced Notification Paging Interactions

### Advanced
                           	 Notification Paging Interactions

Feature

Interaction

Emergency Notifications Paging

You can configure the Emergency Notifications Paging wizard using InformaCast Release 11.5(1)SU3 and later versions in basic
                                             paging mode only.

You can configure call monitoring to route patterns that
                                             					 contain digits only in the Emergency Notifications Paging wizard. For route
                                             					 patterns that contain wildcard characters, configure in InformaCast.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable SNMP Service | Configure SNMP in Unified Communications Manager . |
| Step 2 | Set Default Codec to G.711 | Set the default codec to G.711. |
| Step 3 | Configure a Device Pool for Paging | Configure a device pool. |
| Step 4 | Configure Route Partition for InformaCast Paging | Configure a route partition for Basic Paging. |
| Step 5 | Configure Calling Search Space for InformaCast Paging | Configure a calling search space for Basic Paging. |
| Step 6 | Configure CTI Ports for Paging | Configure CTI ports. |
| Step 7 | Configure Access Control Group with AXL Access | Configure an AXL access control group. |
| Step 8 | Configure Application User for Paging | Configure an application user. |
| Step 9 | Enable web access for the phone using one of the following
                                       			 procedures: Enable Web Access for a Phone Enable Web Access for Common Phone Profile Enable Web Access for Enterprise Phone Configuration | You can enable web access on all phones globally using Enterprise
                                          				Phone Configuration, a group of phones using a Common Phone Profile, or an
                                          				individual phone. |
| Step 10 | Configure Authentication URL | Configure the Unified Communications Manager authentication URL to point to InformaCast so that when InformaCast pushes broadcasts to Cisco Unified IP Phone , the phones will authenticate with InformaCast. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable SNMP Service | Enable the
                                             				SNMP and other services in the cluster. |
| Step 2 | Create an InformaCast SNMP Community String | Configure an
                                             				SNMP community string. |

| Step 1 | From Cisco Unified Serviceability, choose Tools > Service Activation . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server on which you want to configure SNMP. |
| Step 3 | Check the
                                             			 check boxes that correspond to the Cisco
                                                				CallManager SNMP Service . |
| Step 4 | For at least one server in the cluster, check the check boxes that
                                             			 correspond to Cisco CallManager , Cisco CTIManager , and Cisco AXL Web Service services. |
| Step 5 | Click Save . |
| Step 6 | Click OK . |
| Step 7 | Repeat the
                                             			 previous steps for all nodes in the cluster. |

| Step 1 | From Cisco Unified Serviceability, choose SNMP > V1/V2c > Community String . |
|---|---|
| Step 2 | From the Server drop-down list, choose a server and click Find . |
| Step 3 | Click Add
                                                				New . |
| Step 4 | In the Community String Name field, enter ICVA . |
| Step 5 | From the Access Privileges drop-down list, select ReadOnly . |
| Step 6 | Check the Apply
                                                				to All Nodes check box if the check box is active. |
| Step 7 | Click Save . |
| Step 8 | Click OK . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Set Default Codec to G.711 | Create a
                                             				region that uses the G.711 codec for calls to other regions. |
| Step 2 | Configure a Device Pool for Paging | Set up a
                                             				device pool for paging and assign the region that you created to that device
                                             				pool. |

| Step 1 | From Cisco Unified CM Administration, choose System > Region Information > Region . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | In the Name field, enter ICVA . |
| Step 4 | Click Save . |
| Step 5 | In the Regions text box, select all regions by pressing the CTRL key and clicking all of the selected regions. |
| Step 6 | From the Maximum Audio Bit Rate drop-down list, select 64 kbps (G.722, G.711) . |
| Step 7 | From the Maximum Session Bit Rate for Video Calls column click the None radio button. |
| Step 8 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Device Pool . |
|---|---|
| Step 2 | Click Add
                                                				New . |
| Step 3 | In the Device
                                                				Pool Name field, enter ICVA . |
| Step 4 | From the Cisco Unified Communications Manager Group drop-down list, select the group that contains the Cisco Unified Communications Manager cluster with which the InformaCast
                                             Virtual Appliance will communicate. |
| Step 5 | From the Date/Time Group drop-down list, select a date/time group. Select CMLocal unless you are performing dialing restrictions by the time of day. |
| Step 6 | From the Region drop-down list, choose ICVA . |
| Step 7 | From the SRST Reference drop-down list, select Disable . |
| Step 8 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Route Partition for InformaCast Paging | Configure a
                                             				route partition for InformaCast paging. |
| Step 2 | Configure Calling Search Space for InformaCast Paging | Configure a
                                             				calling search space for InformaCast paging. |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Route Partitions . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | In the Name field, enter the following name and description for the partition: ICVA-CTIOutbound,ICVA-Do not add to any phone CSS . |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Calling Search Space . |
|---|---|
| Step 2 | Click Add
                                                				New . |
| Step 3 | In the Name field, enter ICVA . |
| Step 4 | In the Available Partitions list box, use the arrows to
                                             			 move the following partitions to the Selected Partitions list box. The partition that you
                                                				created for InformaCast paging The partitions that contain
                                                				your users' extensions and any analog paging extensions |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Add
                                             				New . |
| Step 3 | From the Phone Type drop-down list, choose CTI Port . |
| Step 4 | In the Device
                                             				Name field, enter a name for the CTI Port. For example, ICVA-IC-001 for an InformaCast port. |
| Step 5 | In the Description field, enter a description for the port.
                                          			 For example, InformaCast Recording Port for Call
                                             				Monitoring . |
| Step 6 | From the Device Pool drop-down list, select ICVA . |
| Step 7 | From the Calling Search Space drop-down list, select ICVA . |
| Step 8 | From the Device Security Profile drop-down list, select Cisco CTI Port - Standard SCCP Non-Secure Profile . |
| Step 9 | Click Save . |
| Step 10 | Click OK . |
| Step 11 | In the left
                                          			 association area, click Line
                                             				[1] - Add a new DN . |
| Step 12 | In the Directory Number field, enter a directory number.
                                          			 This directory number should not be used for any purpose other than making
                                          			 paging calls. It should not be assigned to a phone and should not be within a
                                          			 direct-inward-dialing range. |
| Step 13 | In the Route Partition drop-down list, select the following ports: For InformaCast ports, select ICVA-CTIOutbound . |
| Step 14 | In the Display (Internal Caller ID) text box, enter InformaCast . |
| Step 15 | In the ASCII
                                             				Display (Internal Caller ID) text box, enter InformaCast . |
| Step 16 | Click Save . |
| Step 17 | Repeat this
                                          			 procedure for each CTI port that you need. |

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > Access Control Group . |
|---|---|
| Step 2 | Click Add
                                             				New . |
| Step 3 | In the Name text box, enter ICVA
                                             				User Group . |
| Step 4 | Click Save . |
| Step 5 | From the Related Links drop-down list, select Back to Find/List and click Go . |
| Step 6 | In the Roles column, click the i icon that corresponds to the new access control group. |
| Step 7 | Click Assign
                                             				Role to Group . |
| Step 8 | Click Find . |
| Step 9 | Select Standard AXL API Access check box, and click Add
                                             				Selected . |
| Step 10 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose User Management > Application User . |
|---|---|
| Step 2 | Click Add
                                             				New . |
| Step 3 | In the User
                                             				ID text box, enter a user ID for the application user. For
                                          			 example, ICVA
                                             				InformaCast . |
| Step 4 | Enter a
                                          			 password in the Password and Confirm Password fields. |
| Step 5 | In the Available Devices list box, click the CTI ports that
                                          			 you created for your deployment and use the arrows to move the devices to the Controlled Devices list box. For example, select ICVA-IC-001 for InformaCast and ICVA-CA-001 for CallAware. |
| Step 6 | Click the Add to Access Control Group . |
| Step 7 | Click Find . |
| Step 8 | Check the
                                          			 following check boxes (unless otherwise indicated, select these permissions for
                                          			 all application users): ICVA User Group Standard CTI Allow Control
                                             				of All Devices Standard CTI Allow Control
                                             				of Phones supporting Connected Xfer and conf Standard CTI Allow Control
                                             				of Phones supporting Rollover Mode Standard CTI Enabled |
| Step 9 | Click Add
                                             				Selected . |
| Step 10 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select the phone for which you want to
                                          			 enable web access. |
| Step 3 | In the Product Specific Configuration Layout area, from the Web Access drop-down list, select Enabled . |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose I Device > Device Settings > Common Phone Profile . |
|---|---|
| Step 2 | Click Find and select the profile that applies to the
                                          			 group of phones for which you want to enable web access. |
| Step 3 | In the Product Specific Configuration Layout area, from the Web
                                             				Access drop-down list, select Enable . |
| Step 4 | Click Save . |
| Step 5 | Click Apply
                                             				Config to reset the phones that use the Common Phone Profile. |
| Step 6 | Click OK . |

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Phone Configuration . |
|---|---|
| Step 2 | From the Web
                                             				Access drop-down list, select Enable . |
| Step 3 | Click Save . |
| Step 4 | Click Apply
                                             				Config to reset the phones that use the Common Phone Profile. |
| Step 5 | Click OK . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Set Authentication URL | Set the Unified Communications Manager authentication URL to point InformaCast. |
| Step 2 | Reset Your Phones | Reset the phones in your deployment so that your phones use the new settings. |
| Step 3 | Test Your Phones | Verify that
                                             				the phones in your deployment use the new authentication URL settings. |

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Parameters . |
|---|---|
| Step 2 | Scroll to the Phone
                                                				URL Parameters area, and in the URL
                                                				Authentication field, enter http://<IP
                                                				Address>:8081/InformaCast/phone/auth where <IP Address> is
                                             			 the IP Address of the InformaCast Virtual Appliance. Note Make a note
                                                            				  of the existing URL in the URL Authentication field. You may need this when you
                                                            				  configure InformaCast. See your InformaCast documentation for details. | Note | Make a note
                                                            				  of the existing URL in the URL Authentication field. You may need this when you
                                                            				  configure InformaCast. See your InformaCast documentation for details. |
| Note | Make a note
                                                            				  of the existing URL in the URL Authentication field. You may need this when you
                                                            				  configure InformaCast. See your InformaCast documentation for details. |
| Step 3 | Scroll to the Secured Phone URL Parameters area, and in the Secured Authentication URL field, enter http://<IP
                                                				Address>:8081/InformaCast/phone/auth where <IP Address> is
                                             			 the IP Address of the InformaCast Virtual Appliance. |
| Step 4 | Click Save . |

| Note | Make a note
                                                            				  of the existing URL in the URL Authentication field. You may need this when you
                                                            				  configure InformaCast. See your InformaCast documentation for details. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | In the From Phone Where box, select Device Pool . |
| Step 3 | Set the other drop-down menus and field items to settings that will bring up the device pools that you contain your phones. |
| Step 4 | Click Find . |
| Step 5 | Select the device pools that you want to reset. |
| Step 6 | Click Reset Selected . |
| Step 7 | Click Reset . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Use the drop-down list and fields in the Find and List Phones window to filter your search for a phone that should be using
                                             the new authentication URL, and click Find . |
| Step 3 | For the phone
                                             			 that should be using the new settings, click the IP Address link in the IPv4
                                                				Address column. |
| Step 4 | Click Network
                                             			 Configuration. The
                                             			 Network Configuration page appears. |
| Step 5 | Verify that
                                             			 the Authentication URL field displays the InformaCast
                                             			 Virtual Appliance IP address that you entered for the URL
                                                				Authentication enterprise parameter. If the correct URL does not
                                             			 appear, you will need to set the authentication URL. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Install the InformaCast Virtual Appliance . | Download the
                                          				InformaCast OVA file from the Singlewire website and
                                          				upload it to vSphere. |
| Step 2 | Configure Connection to InformaCast . | Configure Unified Communications Manager and InformaCast. |
| Step 3 | Configure Panic Button . | Configure a
                                          				panic button to send a text and audio notification to IP phones. |
| Step 4 | Configure CallAware Emergency Call Alerting . | Configure
                                          				emergency call text and audio notifications. |

| Note | To view a list
                                             			 of Singlewire-supported VMware ESXi versions, go to this URL: https://www.singlewire.com/compatibility-matrix and click the Server
                                             			 Platforms link under InformaCast Platform section. |
|---|---|

| Note | If you have
                                             			 purchased a license, refer to https://www.singlewire.com/icva-kb-activate to activate your license.
                                             			 This will ensure that Emergency Notifications stay active after the 90-day
                                             			 trial. |
|---|---|

| Note | For more
                                             			 details on the installation, including InformaCast screen captures, go to this
                                             			 URL: https://www.singlewire.com/icva-kb-install . |
|---|---|

| Step 1 | Download the
                                          			 OVA file from the Singlewire website and
                                          			 then log in to the vSphere client. Note If you are
                                                         				  using InformaCast on the Communications Manager Business Edition 6000, you are
                                                         				  supplied with a DVD in a package with an OVA on it (physical media). The vSphere
                                             				Client window appears. | Note | If you are
                                                         				  using InformaCast on the Communications Manager Business Edition 6000, you are
                                                         				  supplied with a DVD in a package with an OVA on it (physical media). |
|---|---|---|---|
| Note | If you are
                                                         				  using InformaCast on the Communications Manager Business Edition 6000, you are
                                                         				  supplied with a DVD in a package with an OVA on it (physical media). |
| Step 2 | From the vSphere
                                             				Client window, choose File > Deploy OVF
                                                				  Template . The Deploy
                                             				OVF Template dialog box appears. |
| Step 3 | Click the Deploy
                                             				from File radio button and then click Browse to select the saved the OVA file (or to the
                                          			 OVA file on the supplied DVD). After you select the OVA file, click Open . The Source location is selected in the Deploy
                                             				OVF Template dialog box. |
| Step 4 | Click Next to continue. The Deploy
                                             				OVF Template dialog box refreshes and OVF
                                             				Template Details appears. |
| Step 5 | Click Next to verify the Name
                                             				and Location , and then click Next to select the network to store the new virtual
                                          			 machine files. Tip It is good
                                                         				  practice to place the Virtual Appliance on the same VLAN as your Cisco Unified Communications Manager . | Tip | It is good
                                                         				  practice to place the Virtual Appliance on the same VLAN as your Cisco Unified Communications Manager . |
| Tip | It is good
                                                         				  practice to place the Virtual Appliance on the same VLAN as your Cisco Unified Communications Manager . |
| Step 6 | Click Next to continue, and then click Finish . The
                                          			 InformaCast Virtual Appliance begins importing. |
| Step 7 | From the vSphere
                                             				Client window, click Hosts
                                             				and Clusters icon and then select your host server. The vSphere
                                             				Client window refreshes. |
| Step 8 | Click the Configuration tab and select the Virtual Machine Startup/Shutdown link in the Software section. |
| Step 9 | Click the Properties link. The Virtual
                                             				Machine Startup and Shutdown dialog box appears. |
| Step 10 | Check the Allow
                                             				virtual machines to start and stop automatically with the system check box under System
                                             				Settings . |
| Step 11 | Under Startup Order , scroll to the Manual
                                             				Startup section and select your virtual machine (by default, this
                                          			 is Singlewire InformaCast VM), and then move it from the Manual
                                             				Startup section to the Automatic Startup section, by using the Move
                                             				Up button. After moving it, click OK . The
                                          			 InformaCast Virtual Appliance starts and stops automatically with the server on
                                          			 which it is hosted. Now you can turn on InformaCast's virtual machine and set
                                          			 its network configuration. |
| Step 12 | Choose View > Inventory > VMs and
                                                				  Templates and then select your virtual machine. |
| Step 13 | Choose the Inventory > Virtual
                                                				  Machine > Open Console The
                                          			 Singlewire InformaCast VM console window appears. |
| Step 14 | InformaCast
                                          			 configuration starts for the first time. During this configuration, perform the
                                          			 following tasks for the InformaCast Virtual Appliance: Accept
                                                				  Cisco End User License Agreement (EULA) Accept
                                                				  Singlewire EULA Set up
                                                				  hostname Set up
                                                				  IP address, subnet mask, and default gateway Set up
                                                				  DNS server IP address and domain name Set up
                                                				  NTP server IP address or hostname Set up
                                                				  time zone Set up
                                                				  Secure Socket Layer (SSL) certificate parameters Set up
                                                				  SSL subject alternate names (optional) Set up
                                                				  the OS admin password Set up
                                                				  the InformaCast and PTT (PushToTalk) admin password. This password is required
                                                				  to connect the Cisco Unified Communications Manager and InformaCast
                                                				  in the Cisco Unified CM Administration, Advanced
                                                      						Features > Emergency Notifications Paging . Set up
                                                				  security passphrase for backup and communication When
                                          			 your configuration is successful, the "Welcome to
                                             				Singlewire InformaCast" message is displayed. |
| Step 15 | Click Continue to work with Singlewire InformaCast. |

| Note | If you are
                                                         				  using InformaCast on the Communications Manager Business Edition 6000, you are
                                                         				  supplied with a DVD in a package with an OVA on it (physical media). |
|---|---|

| Tip | It is good
                                                         				  practice to place the Virtual Appliance on the same VLAN as your Cisco Unified Communications Manager . |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Advanced Features > Emergency Notifications Paging . |
|---|---|
| Step 2 | In the Introduction to InformaCast Emergency Notifications page, click Next to continue. The Installing the InformaCast Virtual Appliance page
                                          			 appears. |
| Step 3 | In the Installing the InformaCast Virtual Appliance page,
                                          			 click Next to continue. Note You should have successfully installed InformaCast Virtual Appliance to configure with the Unified Communications Manager . The Connecting Cisco Unified Communications Manager and InformaCast page appears. | Note | You should have successfully installed InformaCast Virtual Appliance to configure with the Unified Communications Manager . |
| Note | You should have successfully installed InformaCast Virtual Appliance to configure with the Unified Communications Manager . |
| Step 4 | In the IP
                                             				address of InformaCast VM field, enter either IP address or
                                          			 Hostname. Note By default,
                                                         				  the username is stated as admin in the Username to use in InformaCast field, and it is not
                                                         				  editable. | Note | By default,
                                                         				  the username is stated as admin in the Username to use in InformaCast field, and it is not
                                                         				  editable. |
| Note | By default,
                                                         				  the username is stated as admin in the Username to use in InformaCast field, and it is not
                                                         				  editable. |
| Step 5 | In the Password for admin app user field, enter the
                                          			 administrator password of the InformaCast application. The dialog box displaying the thumbprint of the InformaCast certificate is displayed. |
| Step 6 | Click OK to load the InformaCast certificate to the Unified Communications Manager Tomcat trust store. The configuration process starts. Note When the configuration is successful, the Status field displays the completion status. | Note | When the configuration is successful, the Status field displays the completion status. |
| Note | When the configuration is successful, the Status field displays the completion status. |
| Step 7 | Click Next . The wizard performs the following tasks: Activates SNMP service Configures SNMP Service with locally generated random
                                                   					 credentials Activates CTI Manager Service Configures Unified Communications Manager for InformaCast Creates new region (1 per cluster) Creates new device pool (1 per cluster) Creates SIP trunk (1 per cluster) Creates route group (1 per cluster) Creates route list Creates role Creates app user Configures InformaCast for Unified Communications Manager Creates a cluster Refreshes recipient groups Sets SIP access to deny Creates SIP access |

| Note | You should have successfully installed InformaCast Virtual Appliance to configure with the Unified Communications Manager . |
|---|---|

| Note | By default,
                                                         				  the username is stated as admin in the Username to use in InformaCast field, and it is not
                                                         				  editable. |
|---|---|

| Note | When the configuration is successful, the Status field displays the completion status. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Advanced Features > Emergency Notifications Paging . |
|---|---|
| Step 2 | In the Introduction to InformaCast Emergency Notifications page, click Next to continue. |
| Step 3 | In the Installing the InformaCast Virtual Appliance page,
                                          			 click Next to continue. |
| Step 4 | In the Connecting Cisco Unified Communications Manager and InformaCast page, click Next to continue. The Configuring a Panic Button page appears. |
| Step 5 | From the Choose
                                             				pre-recorded message by name drop-down list, select the
                                          			 pre-recorded message to be displayed on Cisco Unified IP phones and various
                                          			 devices and systems in emergency. Note You can
                                                         				  change the pre-recorded message in InformaCast administration, as required. | Note | You can
                                                         				  change the pre-recorded message in InformaCast administration, as required. |
| Note | You can
                                                         				  change the pre-recorded message in InformaCast administration, as required. |
| Step 6 | In the Enter
                                             				DN to trigger the panic button field, enter the Directory Number
                                          			 (DN), which includes the digits 0 to 9, asterisks (*), and pound signs (#).
                                          			 Default value is ***5. |
| Step 7 | From the Route Partition drop-down list, select a partition to restrict access to the route pattern. Note If you do not want to restrict access to the route pattern, select < None > for the partition. | Note | If you do not want to restrict access to the route pattern, select < None > for the partition. |
| Note | If you do not want to restrict access to the route pattern, select < None > for the partition. |
| Step 8 | Click Choose
                                             				Phones to Send Notification button. The Phones to Send Notification dialog box appears. |
| Step 9 | From the Phones to Send Notification dialog box, select the
                                          			 Cisco Unified IP phones to send the pre-recorded message. The dial pattern
                                          			 entered by you (for example, ***5) is configured as speed dial on the selected
                                          			 phones. The selected Cisco Unified IP Phone are displayed in the Selected Phones to Send Notification list box. |
| Step 10 | Click Add Rules , to create a new rule for the selected Cisco Unified IP Phone to receive notifications. Select one of the parameters from the drop-down list. The available options are Device Pool, Description, and Directory Number. In the second drop-down list, select a criteria from the following options: Does Does not In the third drop-down list, select a criteria from the following options: Begins with Ends with Contains In the text box, enter the search criterion. Note Minimum of one new rule and maximum of new five rules can be created. The Add Rules button gets disabled when five rules are created. Note To delete a rule, click Delete Rules . Click Test Rules , to validate the created rules. When the test rule is completed with more than zero phones, the Next button is enabled. Note Phones added to Cisco Unified Communications Manager at a later date that match this rule will be included as recipients in notifications to this group. | Note | Minimum of one new rule and maximum of new five rules can be created. The Add Rules button gets disabled when five rules are created. | Note | To delete a rule, click Delete Rules . | Note | Phones added to Cisco Unified Communications Manager at a later date that match this rule will be included as recipients in notifications to this group. |
| Note | Minimum of one new rule and maximum of new five rules can be created. The Add Rules button gets disabled when five rules are created. |
| Note | To delete a rule, click Delete Rules . |
| Note | Phones added to Cisco Unified Communications Manager at a later date that match this rule will be included as recipients in notifications to this group. |
| Step 11 | Click Next . The wizard performs the following tasks: Adds a speed dial for the entered DN to the selected phones. If the selected phones have unused speed dials assigned to existing
                                                   phone button templates, this speed dial appears directly on the selected phones. If the selected phones do not have unused
                                                   speed dial buttons, the panic button speed dial is created, but it does not appear on the phone. Adds route pattern for entered DN in selected partition using created route list. Creates an InformaCast DialCast entry for the entered DN to send the selected message to the phones matching the selected
                                                   rules. |

| Note | You can
                                                         				  change the pre-recorded message in InformaCast administration, as required. |
|---|---|

| Note | If you do not want to restrict access to the route pattern, select < None > for the partition. |
|---|---|

| Note | Minimum of one new rule and maximum of new five rules can be created. The Add Rules button gets disabled when five rules are created. |
|---|---|

| Note | To delete a rule, click Delete Rules . |
|---|---|

| Note | Phones added to Cisco Unified Communications Manager at a later date that match this rule will be included as recipients in notifications to this group. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Advanced Features > Emergency Notifications Paging . |
|---|---|
| Step 2 | In the Introduction to InformaCast Emergency Notifications page, click Next to continue. |
| Step 3 | In the Installing the InformaCast Virtual Appliance page,
                                          			 click Next to continue. |
| Step 4 | In the Connecting Cisco Unified Communications Manager and InformaCast page, click Next to continue. |
| Step 5 | In the Configuring a Panic Button page, click Next to continue. The Configuring CallAware Emergency Call Alerting page
                                          			 appears. |
| Step 6 | From the Choose
                                             				pre-recorded message by name drop-down list, select the
                                          			 pre-recorded message to be displayed on Cisco Unified IP phones and various
                                          			 devices and systems in emergency. Note You can
                                                         				  change the pre-recorded message in InformaCast administration, as required. | Note | You can
                                                         				  change the pre-recorded message in InformaCast administration, as required. |
| Note | You can
                                                         				  change the pre-recorded message in InformaCast administration, as required. |
| Step 7 | Click Choose
                                             				Emergency Route Patterns button. The Route
                                             				Patterns dialog box appears. |
| Step 8 | From the Route
                                             				Patterns dialog box, select the route patterns by checking the box
                                          			 next to the desired patterns. Click
                                                				  the Save Selected/Changes button. The
                                          			 selected route patterns are displayed in the Selected Route Patterns list box. |
| Step 9 | Click Add Rules , to create a new rule for the selected Cisco Unified IP Phone to receive notifications. Select one of the parameters from the drop-down list. The available options are Device Pool, Description, and Directory Number. In the second drop-down list, select a criteria from the following options: Does Does not In the third drop-down list, select a criteria from the following options: Begins with Ends with Contains In the text box, enter the search criterion. Note Minimum of one new rule and maximum of five new rules can be created. The Add Rules button gets disabled when five rules are created. Note To delete a rule, click Delete Rules . Click Test Rules , to validate the created rules. When the test rule is completed with more than zero phones, the Finish button is enabled. Note Phones added to Unified Communications Manager at a later date that match this rule will be included as recipients in notifications to this group. | Note | Minimum of one new rule and maximum of five new rules can be created. The Add Rules button gets disabled when five rules are created. | Note | To delete a rule, click Delete Rules . | Note | Phones added to Unified Communications Manager at a later date that match this rule will be included as recipients in notifications to this group. |
| Note | Minimum of one new rule and maximum of five new rules can be created. The Add Rules button gets disabled when five rules are created. |
| Note | To delete a rule, click Delete Rules . |
| Note | Phones added to Unified Communications Manager at a later date that match this rule will be included as recipients in notifications to this group. |
| Step 10 | Click Finish . The wizard
                                             				performs the following tasks: Adds
                                                   					 External Call Control profile for InformaCast For each
                                                   					 selected route pattern, modify that route pattern to reference the External
                                                   					 Call Control profile Creates
                                                   					 a recipient group with rules that match phones to receive the notification Creates
                                                   					 an InformaCast routing request with the selected message and recipient group The Summary page appears and confirms the successful configuration of InformaCast with Unified Communications Manager . For more information, see https://www.singlewire.com . |

| Note | You can
                                                         				  change the pre-recorded message in InformaCast administration, as required. |
|---|---|

| Note | Minimum of one new rule and maximum of five new rules can be created. The Add Rules button gets disabled when five rules are created. |
|---|---|

| Note | To delete a rule, click Delete Rules . |
|---|---|

| Note | Phones added to Unified Communications Manager at a later date that match this rule will be included as recipients in notifications to this group. |
|---|---|

| Feature | Interaction |
|---|---|
| Emergency Notifications Paging | You can configure the Emergency Notifications Paging wizard using InformaCast Release 11.5(1)SU3 and later versions in basic
                                             paging mode only. You can configure call monitoring to route patterns that
                                             					 contain digits only in the Emergency Notifications Paging wizard. For route
                                             					 patterns that contain wildcard characters, configure in InformaCast. |