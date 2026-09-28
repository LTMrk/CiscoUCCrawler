---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1262-insta-a8e8dcf46b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1262/install/guide/cuic_b_install-and-upgrade-guide-1262/cuic_m_administration-console-sign-in-1261.html
retrieved_at: 2026-08-21T16:14:33.343265+00:00
---

Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 12.6(2)

# Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 12.6(2)

Updated: April 28, 2023

Chapter: Administration
	 Console Sign-In

## Chapter: Administration
	 Console Sign-In

- Administration                              	 Console Sign-In

- Define Member Node in Administration Console

- Verify Controller Is                              	 Synchronized with NTP Server

# Administration
                     	 Console Sign-In

After you install
                        		the Controller, you must sign in to the Administration Console to perform tasks
                        		as explained in this chapter.

The tasks below
                                    		  are not applicable for a Live Data and IdS deployment.

To sign in, open a browser and enter the URL for your Controller ( https://<HostAddress>/oamp ), where HostAddress is the host name or IP Address of the Controller . This opens the Administration Console.

Sign in using the
                        		System Application credentials.

## Define Member Node in Administration Console

If you intend to add a Member node, you must define the Member in the
                              		  Administration console before you run the installation for the Member.

Step 1

To access the Administration console, direct a browser to the URL http s ://<HOST ADDRESS>/oamp where HOST ADDRESS is the IP Address or Hostname of your server.

Step 2

Sign in using the system application user ID and password that you defined during installation. For more information, see Configuration Worksheet .

Step 3

From left panel, select Device Configuration .

The Device Configuration page shows the Controller that you have installed. Note that the hostname defaults to the alias CUIC1. (You can change it.)

Step 4

On the Device Configuration page, click New .

Step 5

On the Device Configuration fields for the new Member, enter a
                                       			 name by which you can identify the Member, the hostname or IP address, and a
                                       			 description for the device.

Step 6

Click OK .

The Member appears on the Device Configuration list.

## Verify Controller Is
                        	 Synchronized with NTP Server

To do this:

Step 1

Access the
                                       			 Command Line Interface on the Controller node directly, by using the monitor
                                       			 and keyboard at the server console. At the login prompt:

Enter the ID
                                             				  for the System Administrator user (created during Basic Install configuration).

When
                                             				  prompted, enter the password for the System Administration user.

Step 2

Enter this
                                       			 command: utils ntp
                                          				status .

| Note | The tasks below
                                    		  are not applicable for a Live Data and IdS deployment. |
|---|---|

| Step 1 | To access the Administration console, direct a browser to the URL http s ://<HOST ADDRESS>/oamp where HOST ADDRESS is the IP Address or Hostname of your server. |
|---|---|
| Step 2 | Sign in using the system application user ID and password that you defined during installation. For more information, see Configuration Worksheet . |
| Step 3 | From left panel, select Device Configuration . The Device Configuration page shows the Controller that you have installed. Note that the hostname defaults to the alias CUIC1. (You can change it.) |
| Step 4 | On the Device Configuration page, click New . |
| Step 5 | On the Device Configuration fields for the new Member, enter a
                                       			 name by which you can identify the Member, the hostname or IP address, and a
                                       			 description for the device. |
| Step 6 | Click OK . The Member appears on the Device Configuration list. |

| Step 1 | Access the
                                       			 Command Line Interface on the Controller node directly, by using the monitor
                                       			 and keyboard at the server console. At the login prompt: Enter the ID
                                             				  for the System Administrator user (created during Basic Install configuration). When
                                             				  prompted, enter the password for the System Administration user. |
|---|---|
| Step 2 | Enter this
                                       			 command: utils ntp
                                          				status . The output
                                       			 must indicate that the node is synchronized with an NTP server. If the
                                       			 Controller node is not synchronized with an NTP server, the installation of the
                                       			 Member node will fail. |