---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb12-6-cucosadmin-ccvp-b-1261-cvvb-cu-4bdc62dd5f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/vvb12_6/cucosadmin/ccvp_b_1261-cvvb-cuc-os-administration-guide/ccvp_b_1251-cvvb-cuc-os-administration-guide_chapter_0110.html
retrieved_at: 2026-08-21T16:31:35.665055+00:00
---

Cisco Unified Communications Operating System Administration Guide for Cisco Virtualized Voice Browser, Release 12.6(1)

# Cisco Unified Communications Operating System Administration Guide for Cisco Virtualized Voice Browser, Release 12.6(1)

Updated: May 21, 2021

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

You can upload a text
                              				file that contains a customized logon message that appears in Cisco Unified
                              				Operating System Administration, Disaster Recovery System, and the command-line
                              				interface.

To upload a customized logon message, the procedure is as follows:

From the Cisco Unified Operating System Administration window, navigate to Software Upgrades > Customized Logon Message .

Click Browse . Choose the text file that you want to
                                       					upload.

Select the required file and click Upload File .

You cannot upload a file that is larger than 10kB.

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