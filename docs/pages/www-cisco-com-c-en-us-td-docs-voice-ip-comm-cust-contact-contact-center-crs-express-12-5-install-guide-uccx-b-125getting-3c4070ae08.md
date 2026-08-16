---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-install-guide-uccx-b-125getting-3c4070ae08
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/install/guide/uccx_b_125getting-started-ip-ivr/uccx_b_125getting-started-ip-ivr_chapter_01100.html
retrieved_at: 2026-08-16T21:15:04.965853+00:00
---

Getting Started with IP IVR Guide, Release 12.5(1)

# Getting Started with IP IVR Guide, Release 12.5(1)

Updated: February 10, 2020

Chapter: Install and Configure Unified CM for Unified IP IVR

## Chapter: Install and Configure Unified CM for Unified IP IVR

# Install and Configure Unified CM for Unified IP IVR

## About Unified CM

Unified CM:

Provide features for which organizations have traditionally used
                                    				PBX systems. Unified CM uses open standards, such as TCP/IP, H.323 standards
                                    				for packet-based multimedia communications systems, and Media Gateway Control
                                    				Protocol (MGCP).

Allow deployment of voice applications and the integration of
                                    				telephony systems with Intranet applications.

## Unified CM
                        	 Install

Follow the
                           		step-by-step installation instructions for Unified CM included in the Installing Cisco
                              		  Unified Communications Manager Guide . See Cisco Unified Communications Manager Install and Upgrade
                                 			 Guides .

There are no
                           		Unified CCE specific installation prerequisites or instructions for Unified CM.
                           		You can find the guide and the other guides mentioned at the Cisco Unified Communications Manager Install and
                                 			 Upgrade website.

Once Unified
                           		CM installation is complete, configure Unified CM as described in the next
                           		section.

Prior to
                           		proceeding with configuration, ensure that:

By using the
                                 			 System option in the Cisco Unified CM menu selection from the Unified CCX
                                 			 Administration web page, verify that Unified CM has been created on a Unified
                                 			 CM server.

By using Unified
                                 			 CM Administration and the Cisco Unified Serviceability Administration, verify
                                 			 that all the services required by Unified CM are running.

If you are
                                 			 planning on using the Unified CM BAT (Bulk Administration Tool), you can run it
                                 			 by choosing Bulk Administration from the Unified CM Administration menu.

By using the
                                 			 Unified CM User Management web page, identify the users in the Unified CM
                                 			 directory that will be assigned administration privileges in Unified CCX. If
                                 			 these users do not exist in the Unified CM directory, then you must create
                                 			 those users in Unified CM.

Write down in a
                                             				notebook the Unified CM directory information since you will need it for the
                                             				Unified IP IVR installation. If you keep configuration information that is used
                                             				more than once in a check list notebook, then it will be easier to enter the
                                             				correct configuration information when it is needed.

### Related
                              		  Documentation

Installing Cisco Unified
                                 			 Communications Manager

Cisco Unified Communications
                                 			 Manager Bulk Administration Guide

Cisco Unified Communications
                                 			 Manager Administration Guide

Cisco Unified Communications
                                 			 Manager Features and Service Guide

Cisco Unified Communications
                                 			 Manager System Guide

Cisco Unified Contact Center
                                 			 Express Operations Guide

## Configure Unified
                        	 CM

For
                              		  instructions on configuring Unified CM, see the configuration instructions in
                              		  the Cisco Unified
                                       				  Communications Manager Administration Guide .

Most of the
                              		  Unified CM configuration tasks are done by using Cisco Unified Communications
                              		  Manager Administration. The administration program is accessed from a PC by
                              		  using a web browser.

Enter: https://<Communications
                                             				  Manager_servername>/ccmadmin

## Unified CM
                        	 Configuration Checklist

When
                              		  configuring Unified CM, complete the tasks described in the following table to
                              		  configure Unified CM for use with Unified IP IVR.

Task

Purpose

1.Create
                                                   					 Unified CM users that will later be assigned administrative privileges in the
                                                   					 Unified CCX Administration software.

Provides a
                                                   					 user account for Unified IP IVR to connect with Unified CM.

You will
                                                   					 need to remember the user IDs and passwords for when you install and configure
                                                   					 Unified IP IVR.

The user ID
                                                   					 should not be longer than 31 alphanumeric characters. Although a user ID in
                                                   					 Unified CM can contain up to 128 alphanumeric characters, in a Unified CCX
                                                   					 system, a user ID can be no longer than 31 alphanumeric characters.

User Configuration window

See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "End
                                                      						User Configuration " chapter.

From the
                                                   					 Unified CM Administration page menu bar, select User > Management > End
                                                         						  User .

2. Configure
                                                   					 the Unified CM Group for the devices or use the default.

Specifies
                                                   					 the Unified CM group to provide redundancy and to assign to devices in this
                                                   					 device pool.

Unified CM Group
                                                      						Configuration window

See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "Cisco
                                                      						Unified Communication Manager Group Configuration" chapter.

3. Configure
                                                   					 the appropriate Regions for the sites.

Specifies
                                                   					 the codecs to be used by calls between devices in that region and other
                                                   					 regions.

Region
                                                      						Configuration window

See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "Region Configuration" chapter.

From the
                                                   					 Unified CM Administration page menu bar, select System > Region and then click the Add New link.

4. Configure
                                                   					 the Locations for the sites.

Implements
                                                   					 Call Admission Control which regulates voice quality by limiting the available
                                                   					 bandwidth for calls.

Location
                                                      						Configuration window

See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , " Location
                                                      						Configuration" chapter.

5. Configure
                                                   					 the device pool with the previously configured Regions.

Specifies
                                                   					 the voice codec to be used for calls in the regions with the devices.

Device Pool
                                                      						Configuration window

See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , Device
                                                      						Pool Configuration chapter.

From the
                                                   					 Unified CM Administration page menu bar, select Device > Phone and then either find a
                                                   					 configured phone or click the Add New link.

Choose the
                                                   					 device pool from the Phone Configuration web page.

6. Configure
                                                   					 the phones individually in Unified CM with the correct directory numbers or
                                                   					 configure them with the Unified CM BAT tool. For Bulk Configuration, associate
                                                   					 the Device Pool with the Phone Configuration.

Specifies a
                                                   					 unique dialable phone number for each phone.

Also,
                                                   					 defines characteristics for devices, such as region, date/time group, failover
                                                   					 behavior, and others.

You must set
                                                   					 the configuration on each IP phone so that it can locate and connect to Unified
                                                   					 CM. This procedure varies by site according to the customer's network
                                                   					 configuration.

Phone
                                                      						Configuration window or BAT

See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "Cisco
                                                      						Unified IP Phone Configuration" section.

From the
                                                   					 Unified CM Administration page menu bar, select Device > Phone and then click the Add New link.
                                                   					 Next select your phone type and click Next and continue to follow the instructions,
                                                   					 filling in the required information in the Phone Configuration window.

Add the
                                                   					 phone number and a directory number to the phone number, and then configure the
                                                   					 DN (Dialed Number).

### Check Phone Configuration in Unified CM

Using a Web browser, open Unified CM Administration .

From the Device menu, select Phone.

In the Find and List Phones page, make sure the last text box is
                                          			 blank and click Find .

This will list all the IP phones connected to your system plus the
                                             				CTI ports and Call Control groups automatically created in Unified CM when you
                                             				configured the Unified CCX Application.

| Note | Write down in a
                                             				notebook the Unified CM directory information since you will need it for the
                                             				Unified IP IVR installation. If you keep configuration information that is used
                                             				more than once in a check list notebook, then it will be easier to enter the
                                             				correct configuration information when it is needed. |
|---|---|

| Enter: https://<Communications
                                             				  Manager_servername>/ccmadmin |
|---|

| Task Purpose 1.Create
                                                   					 Unified CM users that will later be assigned administrative privileges in the
                                                   					 Unified CCX Administration software. Provides a
                                                   					 user account for Unified IP IVR to connect with Unified CM. You will
                                                   					 need to remember the user IDs and passwords for when you install and configure
                                                   					 Unified IP IVR. The user ID
                                                   					 should not be longer than 31 alphanumeric characters. Although a user ID in
                                                   					 Unified CM can contain up to 128 alphanumeric characters, in a Unified CCX
                                                   					 system, a user ID can be no longer than 31 alphanumeric characters. User Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "End
                                                      						User Configuration " chapter. From the
                                                   					 Unified CM Administration page menu bar, select User > Management > End
                                                         						  User . 2. Configure
                                                   					 the Unified CM Group for the devices or use the default. Specifies
                                                   					 the Unified CM group to provide redundancy and to assign to devices in this
                                                   					 device pool. Unified CM Group
                                                      						Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "Cisco
                                                      						Unified Communication Manager Group Configuration" chapter. 3. Configure
                                                   					 the appropriate Regions for the sites. Specifies
                                                   					 the codecs to be used by calls between devices in that region and other
                                                   					 regions. Region
                                                      						Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "Region Configuration" chapter. From the
                                                   					 Unified CM Administration page menu bar, select System > Region and then click the Add New link. 4. Configure
                                                   					 the Locations for the sites. Implements
                                                   					 Call Admission Control which regulates voice quality by limiting the available
                                                   					 bandwidth for calls. Location
                                                      						Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , " Location
                                                      						Configuration" chapter. 5. Configure
                                                   					 the device pool with the previously configured Regions. Specifies
                                                   					 the voice codec to be used for calls in the regions with the devices. Device Pool
                                                      						Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , Device
                                                      						Pool Configuration chapter. From the
                                                   					 Unified CM Administration page menu bar, select Device > Phone and then either find a
                                                   					 configured phone or click the Add New link. Choose the
                                                   					 device pool from the Phone Configuration web page. 6. Configure
                                                   					 the phones individually in Unified CM with the correct directory numbers or
                                                   					 configure them with the Unified CM BAT tool. For Bulk Configuration, associate
                                                   					 the Device Pool with the Phone Configuration. Specifies a
                                                   					 unique dialable phone number for each phone. Also,
                                                   					 defines characteristics for devices, such as region, date/time group, failover
                                                   					 behavior, and others. You must set
                                                   					 the configuration on each IP phone so that it can locate and connect to Unified
                                                   					 CM. This procedure varies by site according to the customer's network
                                                   					 configuration. Phone
                                                      						Configuration window or BAT See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "Cisco
                                                      						Unified IP Phone Configuration" section. From the
                                                   					 Unified CM Administration page menu bar, select Device > Phone and then click the Add New link.
                                                   					 Next select your phone type and click Next and continue to follow the instructions,
                                                   					 filling in the required information in the Phone Configuration window. Add the
                                                   					 phone number and a directory number to the phone number, and then configure the
                                                   					 DN (Dialed Number). | Task | Purpose | 1.Create
                                                   					 Unified CM users that will later be assigned administrative privileges in the
                                                   					 Unified CCX Administration software. | Provides a
                                                   					 user account for Unified IP IVR to connect with Unified CM. You will
                                                   					 need to remember the user IDs and passwords for when you install and configure
                                                   					 Unified IP IVR. The user ID
                                                   					 should not be longer than 31 alphanumeric characters. Although a user ID in
                                                   					 Unified CM can contain up to 128 alphanumeric characters, in a Unified CCX
                                                   					 system, a user ID can be no longer than 31 alphanumeric characters. User Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "End
                                                      						User Configuration " chapter. From the
                                                   					 Unified CM Administration page menu bar, select User > Management > End
                                                         						  User . | 2. Configure
                                                   					 the Unified CM Group for the devices or use the default. | Specifies
                                                   					 the Unified CM group to provide redundancy and to assign to devices in this
                                                   					 device pool. Unified CM Group
                                                      						Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "Cisco
                                                      						Unified Communication Manager Group Configuration" chapter. | 3. Configure
                                                   					 the appropriate Regions for the sites. | Specifies
                                                   					 the codecs to be used by calls between devices in that region and other
                                                   					 regions. Region
                                                      						Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "Region Configuration" chapter. From the
                                                   					 Unified CM Administration page menu bar, select System > Region and then click the Add New link. | 4. Configure
                                                   					 the Locations for the sites. | Implements
                                                   					 Call Admission Control which regulates voice quality by limiting the available
                                                   					 bandwidth for calls. Location
                                                      						Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , " Location
                                                      						Configuration" chapter. | 5. Configure
                                                   					 the device pool with the previously configured Regions. | Specifies
                                                   					 the voice codec to be used for calls in the regions with the devices. Device Pool
                                                      						Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , Device
                                                      						Pool Configuration chapter. From the
                                                   					 Unified CM Administration page menu bar, select Device > Phone and then either find a
                                                   					 configured phone or click the Add New link. Choose the
                                                   					 device pool from the Phone Configuration web page. | 6. Configure
                                                   					 the phones individually in Unified CM with the correct directory numbers or
                                                   					 configure them with the Unified CM BAT tool. For Bulk Configuration, associate
                                                   					 the Device Pool with the Phone Configuration. | Specifies a
                                                   					 unique dialable phone number for each phone. Also,
                                                   					 defines characteristics for devices, such as region, date/time group, failover
                                                   					 behavior, and others. You must set
                                                   					 the configuration on each IP phone so that it can locate and connect to Unified
                                                   					 CM. This procedure varies by site according to the customer's network
                                                   					 configuration. Phone
                                                      						Configuration window or BAT See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "Cisco
                                                      						Unified IP Phone Configuration" section. From the
                                                   					 Unified CM Administration page menu bar, select Device > Phone and then click the Add New link.
                                                   					 Next select your phone type and click Next and continue to follow the instructions,
                                                   					 filling in the required information in the Phone Configuration window. Add the
                                                   					 phone number and a directory number to the phone number, and then configure the
                                                   					 DN (Dialed Number). |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Task | Purpose |
| 1.Create
                                                   					 Unified CM users that will later be assigned administrative privileges in the
                                                   					 Unified CCX Administration software. | Provides a
                                                   					 user account for Unified IP IVR to connect with Unified CM. You will
                                                   					 need to remember the user IDs and passwords for when you install and configure
                                                   					 Unified IP IVR. The user ID
                                                   					 should not be longer than 31 alphanumeric characters. Although a user ID in
                                                   					 Unified CM can contain up to 128 alphanumeric characters, in a Unified CCX
                                                   					 system, a user ID can be no longer than 31 alphanumeric characters. User Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "End
                                                      						User Configuration " chapter. From the
                                                   					 Unified CM Administration page menu bar, select User > Management > End
                                                         						  User . |
| 2. Configure
                                                   					 the Unified CM Group for the devices or use the default. | Specifies
                                                   					 the Unified CM group to provide redundancy and to assign to devices in this
                                                   					 device pool. Unified CM Group
                                                      						Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "Cisco
                                                      						Unified Communication Manager Group Configuration" chapter. |
| 3. Configure
                                                   					 the appropriate Regions for the sites. | Specifies
                                                   					 the codecs to be used by calls between devices in that region and other
                                                   					 regions. Region
                                                      						Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "Region Configuration" chapter. From the
                                                   					 Unified CM Administration page menu bar, select System > Region and then click the Add New link. |
| 4. Configure
                                                   					 the Locations for the sites. | Implements
                                                   					 Call Admission Control which regulates voice quality by limiting the available
                                                   					 bandwidth for calls. Location
                                                      						Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , " Location
                                                      						Configuration" chapter. |
| 5. Configure
                                                   					 the device pool with the previously configured Regions. | Specifies
                                                   					 the voice codec to be used for calls in the regions with the devices. Device Pool
                                                      						Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , Device
                                                      						Pool Configuration chapter. From the
                                                   					 Unified CM Administration page menu bar, select Device > Phone and then either find a
                                                   					 configured phone or click the Add New link. Choose the
                                                   					 device pool from the Phone Configuration web page. |
| 6. Configure
                                                   					 the phones individually in Unified CM with the correct directory numbers or
                                                   					 configure them with the Unified CM BAT tool. For Bulk Configuration, associate
                                                   					 the Device Pool with the Phone Configuration. | Specifies a
                                                   					 unique dialable phone number for each phone. Also,
                                                   					 defines characteristics for devices, such as region, date/time group, failover
                                                   					 behavior, and others. You must set
                                                   					 the configuration on each IP phone so that it can locate and connect to Unified
                                                   					 CM. This procedure varies by site according to the customer's network
                                                   					 configuration. Phone
                                                      						Configuration window or BAT See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "Cisco
                                                      						Unified IP Phone Configuration" section. From the
                                                   					 Unified CM Administration page menu bar, select Device > Phone and then click the Add New link.
                                                   					 Next select your phone type and click Next and continue to follow the instructions,
                                                   					 filling in the required information in the Phone Configuration window. Add the
                                                   					 phone number and a directory number to the phone number, and then configure the
                                                   					 DN (Dialed Number). |

| Task | Purpose |
|---|---|
| 1.Create
                                                   					 Unified CM users that will later be assigned administrative privileges in the
                                                   					 Unified CCX Administration software. | Provides a
                                                   					 user account for Unified IP IVR to connect with Unified CM. You will
                                                   					 need to remember the user IDs and passwords for when you install and configure
                                                   					 Unified IP IVR. The user ID
                                                   					 should not be longer than 31 alphanumeric characters. Although a user ID in
                                                   					 Unified CM can contain up to 128 alphanumeric characters, in a Unified CCX
                                                   					 system, a user ID can be no longer than 31 alphanumeric characters. User Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "End
                                                      						User Configuration " chapter. From the
                                                   					 Unified CM Administration page menu bar, select User > Management > End
                                                         						  User . |
| 2. Configure
                                                   					 the Unified CM Group for the devices or use the default. | Specifies
                                                   					 the Unified CM group to provide redundancy and to assign to devices in this
                                                   					 device pool. Unified CM Group
                                                      						Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "Cisco
                                                      						Unified Communication Manager Group Configuration" chapter. |
| 3. Configure
                                                   					 the appropriate Regions for the sites. | Specifies
                                                   					 the codecs to be used by calls between devices in that region and other
                                                   					 regions. Region
                                                      						Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "Region Configuration" chapter. From the
                                                   					 Unified CM Administration page menu bar, select System > Region and then click the Add New link. |
| 4. Configure
                                                   					 the Locations for the sites. | Implements
                                                   					 Call Admission Control which regulates voice quality by limiting the available
                                                   					 bandwidth for calls. Location
                                                      						Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , " Location
                                                      						Configuration" chapter. |
| 5. Configure
                                                   					 the device pool with the previously configured Regions. | Specifies
                                                   					 the voice codec to be used for calls in the regions with the devices. Device Pool
                                                      						Configuration window See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , Device
                                                      						Pool Configuration chapter. From the
                                                   					 Unified CM Administration page menu bar, select Device > Phone and then either find a
                                                   					 configured phone or click the Add New link. Choose the
                                                   					 device pool from the Phone Configuration web page. |
| 6. Configure
                                                   					 the phones individually in Unified CM with the correct directory numbers or
                                                   					 configure them with the Unified CM BAT tool. For Bulk Configuration, associate
                                                   					 the Device Pool with the Phone Configuration. | Specifies a
                                                   					 unique dialable phone number for each phone. Also,
                                                   					 defines characteristics for devices, such as region, date/time group, failover
                                                   					 behavior, and others. You must set
                                                   					 the configuration on each IP phone so that it can locate and connect to Unified
                                                   					 CM. This procedure varies by site according to the customer's network
                                                   					 configuration. Phone
                                                      						Configuration window or BAT See also the Cisco Unified
                                                            				  Communications Manager Administration Guide , "Cisco
                                                      						Unified IP Phone Configuration" section. From the
                                                   					 Unified CM Administration page menu bar, select Device > Phone and then click the Add New link.
                                                   					 Next select your phone type and click Next and continue to follow the instructions,
                                                   					 filling in the required information in the Phone Configuration window. Add the
                                                   					 phone number and a directory number to the phone number, and then configure the
                                                   					 DN (Dialed Number). |

| Step 1 | Using a Web browser, open Unified CM Administration . This URL is commonly: https://<Communications
                                             				Manager_servername>/ccmadmin |
|---|---|
| Step 2 | From the Device menu, select Phone. |
| Step 3 | In the Find and List Phones page, make sure the last text box is
                                          			 blank and click Find . This will list all the IP phones connected to your system plus the
                                             				CTI ports and Call Control groups automatically created in Unified CM when you
                                             				configured the Unified CCX Application. |