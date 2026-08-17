---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-os-administration-guide-b-15cucosagx-b-15cucosagx-chapter-01-h-408c4201bd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/os_administration/guide/b_15cucosagx/b_15cucosagx_chapter_01.html
retrieved_at: 2026-08-17T03:43:06.646590+00:00
---

Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 15

# Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 15

Updated: October 1, 2024

Chapter: Log in to Cisco
	 Unified Communications Operating System Administration

## Chapter: Log in to Cisco
	 Unified Communications Operating System Administration

- Log in to Cisco                              	 Unified Communications Operating System Administration

- Logging in to                              	 Cisco Unified Communications Operating System Administration

- Resetting OS                              	 Administrator and Security Passwords

# Log in to Cisco
                     	 Unified Communications Operating System Administration

This chapter describes the procedure for accessing the Cisco Unified
                        		Communications Operating System Administration and also provides procedures for
                        		resetting a lost password.

## Logging in to
                        	 Cisco Unified Communications Operating System Administration

To access Cisco Unified Communications Operating System
                              		  Administration and log in, follow this procedure.

Do not use the browser controls (for example, the Back button)
                                          			 while you are using Cisco Unified Communications Operating System
                                          			 Administration.

Step 1

Browse to the URL for Cisco Unity Connection Administration.

Step 2

From the Navigation menu in the upper, right corner of the
                                       			 Cisco Unity Connection Administration window, select Cisco Unified OS Administration and click Go .

The Cisco Unified Communications Operating System Administration
                                          				Logon window displays.

You can also access Cisco Unified Communications Operating
                                                      				  System Administration directly by entering the following URL: http:// server-name /cmplatform

Step 3

Enter your Administrator username and password.

The Administrator username and password get established during
                                                      				  installation or created with the command line interface.

Step 4

Click Submit.

The Cisco Unified Communications Operating System Administration
                                          				window displays.

## Resetting OS
                        	 Administrator and Security Passwords

If you lose the Administrator password or security password, use
                              		  the following procedure to reset these passwords.

To perform the password reset process, you must be connected to
                              		  the system through the system console, that is, you must have a keyboard and
                              		  monitor connected to the server. You cannot reset a password when connected to
                              		  the system through a secure shell session.

Caution

The security password on all nodes in a cluster must match.
                                          			 Change the security password on all machines, otherwise the cluster nodes does
                                          			 not communicate.

Caution

You must reset each server in a cluster after you change its
                                          			 security password. Failure to reboot the servers (nodes) causes system service
                                          			 problems and problems with the Cisco Unified Communications Manager
                                          			 Administration windows on the subscriber servers.

During this procedure, you must remove and then insert a valid
                                          			 CD or DVD in the disk drive to prove that you have physical access to the
                                          			 system.

Step 1

Log in to the system with the following username and password:

Username: pwrecovery

Password: pwreset

The Welcome to platform password reset window displays.

Step 2

Press any key to continue.

Step 3

If you have a CD or DVD in the disk drive, remove it now.

Step 4

Press any key to continue.

The system tests to ensure that you have removed the CD or DVD
                                          				from the disk drive.

Step 5

Insert a valid CD or DVD into the disk drive.

For this test, you must use a data CD, not a music CD.

The system tests to ensure that you have inserted the disk.

Step 6

After the system verifies that you have inserted the disk, you
                                       			 get prompted to enter one of the following options to continue:

Enter a to reset the administrator password.

Enter s to reset the security password.

Enter q to quit.

Step 7

Enter a new password of the type that you created.

Step 8

Reenter the new password.

The password must contain at least 6 characters. The system
                                          				checks the new password for strength. If the password does not pass the
                                          				strength check, you get prompted to enter a new password.

Step 9

After the system verifies the strength of the new password, the
                                       			 password gets reset, and you get prompted to press any key to exit the password
                                       			 reset utility.

| Note | Do not use the browser controls (for example, the Back button)
                                          			 while you are using Cisco Unified Communications Operating System
                                          			 Administration. |
|---|---|

| Step 1 | Browse to the URL for Cisco Unity Connection Administration. |
|---|---|
| Step 2 | From the Navigation menu in the upper, right corner of the
                                       			 Cisco Unity Connection Administration window, select Cisco Unified OS Administration and click Go . The Cisco Unified Communications Operating System Administration
                                          				Logon window displays. Note You can also access Cisco Unified Communications Operating
                                                      				  System Administration directly by entering the following URL: http:// server-name /cmplatform | Note | You can also access Cisco Unified Communications Operating
                                                      				  System Administration directly by entering the following URL: http:// server-name /cmplatform |
| Note | You can also access Cisco Unified Communications Operating
                                                      				  System Administration directly by entering the following URL: http:// server-name /cmplatform |
| Step 3 | Enter your Administrator username and password. Note The Administrator username and password get established during
                                                      				  installation or created with the command line interface. | Note | The Administrator username and password get established during
                                                      				  installation or created with the command line interface. |
| Note | The Administrator username and password get established during
                                                      				  installation or created with the command line interface. |
| Step 4 | Click Submit. The Cisco Unified Communications Operating System Administration
                                          				window displays. |

| Note | You can also access Cisco Unified Communications Operating
                                                      				  System Administration directly by entering the following URL: http:// server-name /cmplatform |
|---|---|

| Note | The Administrator username and password get established during
                                                      				  installation or created with the command line interface. |
|---|---|

| Caution | The security password on all nodes in a cluster must match.
                                          			 Change the security password on all machines, otherwise the cluster nodes does
                                          			 not communicate. |
|---|---|

| Caution | You must reset each server in a cluster after you change its
                                          			 security password. Failure to reboot the servers (nodes) causes system service
                                          			 problems and problems with the Cisco Unified Communications Manager
                                          			 Administration windows on the subscriber servers. |
|---|---|

| Note | During this procedure, you must remove and then insert a valid
                                          			 CD or DVD in the disk drive to prove that you have physical access to the
                                          			 system. |
|---|---|

| Step 1 | Log in to the system with the following username and password: Username: pwrecovery Password: pwreset The Welcome to platform password reset window displays. |
|---|---|
| Step 2 | Press any key to continue. |
| Step 3 | If you have a CD or DVD in the disk drive, remove it now. |
| Step 4 | Press any key to continue. The system tests to ensure that you have removed the CD or DVD
                                          				from the disk drive. |
| Step 5 | Insert a valid CD or DVD into the disk drive. Note For this test, you must use a data CD, not a music CD. The system tests to ensure that you have inserted the disk. | Note | For this test, you must use a data CD, not a music CD. The system tests to ensure that you have inserted the disk. |
| Note | For this test, you must use a data CD, not a music CD. The system tests to ensure that you have inserted the disk. |
| Step 6 | After the system verifies that you have inserted the disk, you
                                       			 get prompted to enter one of the following options to continue: Enter a to reset the administrator password. Enter s to reset the security password. Enter q to quit. |
| Step 7 | Enter a new password of the type that you created. |
| Step 8 | Reenter the new password. The password must contain at least 6 characters. The system
                                          				checks the new password for strength. If the password does not pass the
                                          				strength check, you get prompted to enter a new password. |
| Step 9 | After the system verifies the strength of the new password, the
                                       			 password gets reset, and you get prompted to press any key to exit the password
                                       			 reset utility. |

| Note | For this test, you must use a data CD, not a music CD. The system tests to ensure that you have inserted the disk. |
|---|---|