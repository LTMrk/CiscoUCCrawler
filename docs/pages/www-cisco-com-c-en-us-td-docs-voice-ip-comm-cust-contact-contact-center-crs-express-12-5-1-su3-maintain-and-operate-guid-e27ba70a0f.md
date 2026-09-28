---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su3-maintain-and-operate-guid-e27ba70a0f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su3/maintain_and_operate/guide/uccx_b_unified-ccx-operating-system-1251su3/uccx_m_1251su3_software-upgrades.html
retrieved_at: 2026-08-16T21:30:02.447070+00:00
---

Cisco Unified Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR, Release 12.5(1) SU3

# Cisco Unified Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR, Release 12.5(1) SU3

Updated: July 18, 2023

Chapter: Software
	 Upgrades

## Chapter: Software
	 Upgrades

# Software
                     	 Upgrades

You can use
                           		  the Install/Upgrade option to upgrade the Unified CCX software and
                           		  install Unified CCX COP patch
                           		  files.

For more
                                       			 information regarding the supported versions of Unified CCX and Unified CM, see Cisco Unified Contact Center
                                             				  Express (Unified CCX) Compatibility Matrix .

Caution

When you upgrade from an earlier version of
                                          				Unified CCX to the latest version the system
                                       			 restarts as part of the upgrade process. Therefore, you may want to perform the
                                       			 upgrade during maintenance window to avoid service interruptions.

## Unified CCX Upgrade and
                        	 Roll Back

For Upgrade and
                              		  Rollback instructions, see Cisco Unified Contact Center
                                 			 Express Installation and Upgrade Guide available here:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-guides-list.html

## TFTP File
                        	 Management

The Software
                                             				Upgrades > TFTP File Management menu option is
                                       		  not applicable for Unified CCX .

## Set Up Customized Logon Message

You can upload a text file that contains a
                              				customized logon message that appears when users log on to Unified CCX applications.
                              				In the applications, the message appears in one of the following ways as:

A pop-up window, as soon as the authentication page is loaded.

Cisco Unified CCX Administration

Cisco Unified CCX Serviceability

A pop-up window, after entering username and password.

Cisco Identity Service Management

Cisco Finesse Administration

Cisco Unified Intelligence Center

Finesse Desktop

A text in the authentication page.

Disaster Recovery System

Cisco Unified Serviceability

Cisco Unified OS Administration

If the message appears in a pop-up window, you must acknowledge the message to
                                          					log in.

In CLI, the message is displayed after you enter the username and again after you
                                          					enter the password.

To upload a customized logon message, the procedure is as follows:

Step 1

From the Cisco Unified Operating System Administration window, navigate to Software Upgrades > Customized Logon Message .

Step 2

Click Browse . Choose the text file that you want to
                                       					upload.

Step 3

Select the required file and click Upload File .

You cannot upload a file that is larger than 10kB.

Step 4

To revert to the default logon message, click Delete .

By default, there is no custom message configured for Cisco Finesse.

| Note | For more
                                       			 information regarding the supported versions of Unified CCX and Unified CM, see Cisco Unified Contact Center
                                             				  Express (Unified CCX) Compatibility Matrix . |
|---|---|

| Caution | When you upgrade from an earlier version of
                                          				Unified CCX to the latest version the system
                                       			 restarts as part of the upgrade process. Therefore, you may want to perform the
                                       			 upgrade during maintenance window to avoid service interruptions. |
|---|---|

| Note | The Software
                                             				Upgrades > TFTP File Management menu option is
                                       		  not applicable for Unified CCX . |
|---|---|

| Note | If the message appears in a pop-up window, you must acknowledge the message to
                                          					log in. In CLI, the message is displayed after you enter the username and again after you
                                          					enter the password. |
|---|---|

| Step 1 | From the Cisco Unified Operating System Administration window, navigate to Software Upgrades > Customized Logon Message . The Customized Logon Message window appears. |
|---|---|
| Step 2 | Click Browse . Choose the text file that you want to
                                       					upload. |
| Step 3 | Select the required file and click Upload File . Note You cannot upload a file that is larger than 10kB. The customized logon message appears. | Note | You cannot upload a file that is larger than 10kB. |
| Note | You cannot upload a file that is larger than 10kB. |
| Step 4 | To revert to the default logon message, click Delete . Note By default, there is no custom message configured for Cisco Finesse. Your customized logon message is deleted, and the system displays the
                                       					default logon message. | Note | By default, there is no custom message configured for Cisco Finesse. |
| Note | By default, there is no custom message configured for Cisco Finesse. |

| Note | You cannot upload a file that is larger than 10kB. |
|---|---|

| Note | By default, there is no custom message configured for Cisco Finesse. |
|---|---|