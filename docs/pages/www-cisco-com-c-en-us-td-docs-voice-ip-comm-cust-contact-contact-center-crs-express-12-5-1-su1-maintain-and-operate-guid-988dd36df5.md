---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-maintain-and-operate-guid-988dd36df5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/maintain_and_operate/guide/uccx_b_1251su1unified-ccx-operating-system/uccx_b_1261unified-ccx-operating-system_chapter_010.html
retrieved_at: 2026-08-16T21:40:41.700031+00:00
---

Cisco Unified Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR, Release 12.5(1) SU1

# Cisco Unified Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR, Release 12.5(1) SU1

Updated: February 1, 2021

Chapter: Cisco Unified Operating System Administration

## Chapter: Cisco Unified Operating System Administration

- Cisco Unified Operating System Administration

- Login to Cisco Unified Operating System

- Reset Administrator                              	 or Security Password

# Cisco Unified Operating System Administration

## Login to Cisco Unified Operating System

To access and login to Cisco Unified Operating System from Unified CCX , follow this procedure:

Do not use the browser controls (for example, the Back button) while you are using Cisco Unified Operating System Administration.

Log in to Unified CCX Application
                                       			 Administration web interface.

From the
                                       			 Navigation menu in the upper-right corner of the Unified CCX Application Administration web interface, choose Cisco
                                          				Unified OS Administration and click Go .

The Cisco Unified Operating System Administration Logon web page appears.

You can also access Cisco Unified Operating System Administration directly by entering the following URL:

https://<serverIP>/cmplatform

Enter your
                                       			 platform user credentials as configured during installation of Unified CCX .

The platform
                                                      				  username and password get established during installation or created by using
                                                      				  the command line interface.

Click Submit .

## Reset Administrator
                        	 or Security Password

If you lose
                              		  the administrator password or security password, use the following procedure to
                              		  reset the passwords.

The security
                                          			 password on all nodes in a cluster must match. Change the security password on
                                          			 all machines, or the cluster nodes cannot communicate.

During this
                                          			 procedure, you must remove and then insert a valid CD or DVD in the disk drive
                                          			 to prove that you have physical access to the system.

### Before you begin

To perform
                              		  the password reset process, you must be connected to the system through the
                              		  system console, that is, you must have a keyboard and monitor connected to the
                              		  server. You cannot reset a password when connected to the system through a
                              		  secure shell session.

Log in to the
                                       			 system with the following username and password:

Username: pwrecovery

Password: pwreset

The Welcome to platform password reset window appears.

Press any key to
                                       			 continue.

If you have a CD
                                       			 or DVD in the disk drive, remove it now.

Press any key to
                                       			 continue.

The system tests
                                          				to ensure that you have removed the CD or DVD from the disk drive.

Insert a valid
                                       			 CD or DVD into the disk drive. For this test, you must use a data CD, not a
                                       			 music CD. The system tests to ensure that you inserted the disk.

After the system
                                       			 verifies that you have inserted the disk, you are prompted to enter one of the
                                       			 following options to continue:

- Enter a to reset the administrator password.

- Enter s to reset the security password.

- Enter q to quit.

Enter a new
                                       			 password of the type that you chose.

Reenter the new
                                       			 password.

After the system verifies the strength of the new password, the password is reset, and you are prompted to press any key to
                                       exit the password reset utility.

Restart the system for the changes to take effect.

| Note | Do not use the browser controls (for example, the Back button) while you are using Cisco Unified Operating System Administration. |
|---|---|

| Step 1 | Log in to Unified CCX Application
                                       			 Administration web interface. |
|---|---|
| Step 2 | From the
                                       			 Navigation menu in the upper-right corner of the Unified CCX Application Administration web interface, choose Cisco
                                          				Unified OS Administration and click Go . The Cisco Unified Operating System Administration Logon web page appears. Note You can also access Cisco Unified Operating System Administration directly by entering the following URL: https://<serverIP>/cmplatform | Note | You can also access Cisco Unified Operating System Administration directly by entering the following URL: https://<serverIP>/cmplatform |
| Note | You can also access Cisco Unified Operating System Administration directly by entering the following URL: https://<serverIP>/cmplatform |
| Step 3 | Enter your
                                       			 platform user credentials as configured during installation of Unified CCX . Note The platform
                                                      				  username and password get established during installation or created by using
                                                      				  the command line interface. | Note | The platform
                                                      				  username and password get established during installation or created by using
                                                      				  the command line interface. |
| Note | The platform
                                                      				  username and password get established during installation or created by using
                                                      				  the command line interface. |
| Step 4 | Click Submit . The Cisco Unified Operating System Administration window appears. |

| Note | You can also access Cisco Unified Operating System Administration directly by entering the following URL: https://<serverIP>/cmplatform |
|---|---|

| Note | The platform
                                                      				  username and password get established during installation or created by using
                                                      				  the command line interface. |
|---|---|

| Caution | The security
                                          			 password on all nodes in a cluster must match. Change the security password on
                                          			 all machines, or the cluster nodes cannot communicate. |
|---|---|

| Note | During this
                                          			 procedure, you must remove and then insert a valid CD or DVD in the disk drive
                                          			 to prove that you have physical access to the system. |
|---|---|

| Step 1 | Log in to the
                                       			 system with the following username and password: Username: pwrecovery Password: pwreset The Welcome to platform password reset window appears. |
|---|---|
| Step 2 | Press any key to
                                       			 continue. |
| Step 3 | If you have a CD
                                       			 or DVD in the disk drive, remove it now. |
| Step 4 | Press any key to
                                       			 continue. The system tests
                                          				to ensure that you have removed the CD or DVD from the disk drive. |
| Step 5 | Insert a valid
                                       			 CD or DVD into the disk drive. For this test, you must use a data CD, not a
                                       			 music CD. The system tests to ensure that you inserted the disk. |
| Step 6 | After the system
                                       			 verifies that you have inserted the disk, you are prompted to enter one of the
                                       			 following options to continue: Enter a to reset the administrator password. Enter s to reset the security password. Enter q to quit. |
| Step 7 | Enter a new
                                       			 password of the type that you chose. |
| Step 8 | Reenter the new
                                       			 password. The
                                       			 password must contain at least 6 characters. The system checks the new password
                                       			 for strength. If the password does not pass the strength check, you are
                                       			 prompted to enter a new password. |
| Step 9 | After the system verifies the strength of the new password, the password is reset, and you are prompted to press any key to
                                       exit the password reset utility. Note Restart the system for the changes to take effect. | Note | Restart the system for the changes to take effect. |
| Note | Restart the system for the changes to take effect. |

| Note | Restart the system for the changes to take effect. |
|---|---|