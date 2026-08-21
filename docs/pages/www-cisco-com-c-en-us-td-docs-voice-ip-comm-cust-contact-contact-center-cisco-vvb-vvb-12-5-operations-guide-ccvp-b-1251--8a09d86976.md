---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb-12-5-operations-guide-ccvp-b-1251--8a09d86976
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/VVB_12_5/operations/guide/ccvp_b_1251-cvvb-cuc-os-administration-guide/ccvp_b_1251-cvvb-cuc-os-administration-guide_chapter_0110.html
retrieved_at: 2026-08-21T16:34:16.185087+00:00
---

Cisco Unified Communications Operating System Administration Guide for Cisco Virtualized Voice Browser, Release 12.5(1)

# Cisco Unified Communications Operating System Administration Guide for Cisco Virtualized Voice Browser, Release 12.5(1)

Updated: February 2, 2020

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

You can upload a text file that contains a customized logon
                              		  message that appears in Cisco Unified Communications Operating System
                              		  Administration, Disaster Recovery System, and the command-line interface.

To upload a customized logon message, follow this
                              		  procedure:

From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Software
                                             				  Upgrades > Customized Logon
                                             				  Message .

To choose the text file that you want to upload, click Browse .

Click Upload File . 
                                       		   You cannot upload a file that is larger than 10kB.

To revert to the default log-on message, click Delete .

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

| Step 1 | From the Cisco Unified Communications Operating System
                                       			 Administration window, navigate to Software
                                             				  Upgrades > Customized Logon
                                             				  Message . The Customized Logon Message window appears. |
|---|---|
| Step 2 | To choose the text file that you want to upload, click Browse . |
| Step 3 | Click Upload File . 
                                       		   You cannot upload a file that is larger than 10kB. The customized logon message appears. |
| Step 4 | To revert to the default log-on message, click Delete . Your customized logon message is deleted, and the system
                                       			 displays the default logon message. |