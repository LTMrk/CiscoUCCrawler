---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-maintain-and-operate-guide-uccx-3dc8c7ea45
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/maintain_and_operate/guide/uccx_b_unified-ccx-operating-system-125/uccx_b_unified-ccx-operating-system-125_chapter_0111.html
retrieved_at: 2026-08-16T21:42:01.942731+00:00
---

Cisco Unified Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR, Release 12.5(1)

# Cisco Unified Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR, Release 12.5(1)

Updated: February 6, 2020

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

You can upload a text file that contains a customized logon message that appears in Cisco Unified Operating System Administration,
                              Disaster Recovery System, and the command-line interface.

To upload a customized logon message, follow this
                              		  procedure:

From the Cisco Unified Operating System Administration window, navigate to Software Upgrades > Customized Logon Message .

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

| Step 1 | From the Cisco Unified Operating System Administration window, navigate to Software Upgrades > Customized Logon Message . The Customized Logon Message window appears. |
|---|---|
| Step 2 | To choose the text file that you want to upload, click Browse . |
| Step 3 | Click Upload File . 
                                       		   You cannot upload a file that is larger than 10kB. The customized logon message appears. |
| Step 4 | To revert to the default log-on message, click Delete . Your customized logon message is deleted, and the system
                                       			 displays the default logon message. |