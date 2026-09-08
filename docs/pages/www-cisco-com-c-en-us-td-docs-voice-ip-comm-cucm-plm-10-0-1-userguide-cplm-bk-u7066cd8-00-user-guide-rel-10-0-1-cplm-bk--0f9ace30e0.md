---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-10-0-1-userguide-cplm-bk-u7066cd8-00-user-guide-rel-10-0-1-cplm-bk--0f9ace30e0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/10_0_1/userguide/CPLM_BK_U7066CD8_00_user-guide-rel-10-0-1/CPLM_BK_U7066CD8_00_user-guide-rel-10-0-1_chapter_01000.html
retrieved_at: 2026-09-08T05:03:52.925973+00:00
---

Cisco Prime License Manager User Guide, Release 10.0(1)

# Cisco Prime License Manager User Guide, Release 10.0(1)

Updated: July 29, 2014

Chapter: Administration

## Chapter: Administration

# Administration

The following sections provide information on using the Cisco Prime License Manager administrative tools.

## Backup/Restore

Use the following
		  procedure to perform a backup and restore of Cisco Prime License Manager.

- IP Address/Hostname

- Username

- Password

- Directory

## License
	 Definitions

License
		  definitions contain information about the license types managed by Cisco Prime
		  License Manager. This file should be updated prior to upgrading any of your
		  product instances to a new version or before adding a product instance of a new
		  type. The Administration > License Definitions page provides the following
		  information for the currently installed file:

- File name

- Version

- Date Installed

You can click the Check for Latest
			 Version link to access the Download Software site. From this site, you can
		  locate the latest release and download it.

Once downloaded, a
		  new license definition file can be installed using the following procedure:

## Security
	 Updates

Security updates
		  may be required at Cisco Prime License Manager periodically to permit
		  electronic operations with the Cisco License Office.

Security updates
		  will be available at the Cisco Software Download Center: http:/​/​software.cisco.com .

Use the following
		  procedure to perform security updates through CLI:

Directory:
				/users/bsmith/security_update/update

Server:
				se032c-94-61

User Name:
				bsmith

Password:
				********

Available
				options for security update in
				"se032c-94-61:/users/bsmith/security_update/update":

1)
				SecUpd_v1.upd

q) quit

Installing
				security update...

Continue
				(y/n)?

When the
				update is complete, the following message appears:

Security
				update installed.

## License
	 Rehost

Licenses are
		  fulfilled to a specific Cisco Prime License Manger. If you require licenses to
		  be moved to a new Cisco Prime License Manager, they will be need to be
		  rehosted.

A rehost may be
		  required if:

- A hardware failure occurred
			 and new hardware is required for Cisco Prime License Manager

- Multiple Cisco Prime
			 License Managers are desired and a subset of fulfillment licenses need to be
			 moved to a new Cisco Prime License Manager

License rehosts
		  or transfers can be requested at www.cisco.com/​go/​license and do not require Global
		  Licensing Operations (GLO) support.

To perform a
		  rehost, the license registration from the source machine as well as license
		  request or license registration from the target machine is required.

Use the following
		  procedure to perform a license rehost.

## Accessing
	 Diagnostic Logs

Use the following
		  procedure to run diagnostic logs in Cisco Prime License Manager.

## Reset OS
	 Administrator and Security Passwords

To reset a password, you must connect to the system through the system
		  console. You cannot reset a password when you connect to the system through a
		  secure shell session.

During this
			 procedure, you must remove and then insert a valid CD or DVD in the disk drive
			 to prove that you have physical access to the system.

- Username: pwrecovery

The Welcome
				  to platform password reset window appears.

The system
				tests to ensure that you removed the CD or DVD from the disk drive.

For this
				  test, you must use a data CD, not a music CD. The system tests to ensure that
				  you have inserted the disk.

- Enter a to reset the Administrator password.

- Enter s to reset the security password.

- Enter q to quit.

The password
				must contain at least six characters. The system checks the new password for
				strength. If the password does not pass the strength check, you are prompted to
				enter a new password.

| Step 1 | From the main
			 menu, select Administration
				> Backup/Restore . |
|---|---|
| Step 2 | The
			 Backup/Restore page opens. Enter the following information: IP Address/Hostname Username Password Directory Note At this
				point, you can click the Test
				  Connection button to test your connection. | Note | At this
				point, you can click the Test
				  Connection button to test your connection. |
| Note | At this
				point, you can click the Test
				  Connection button to test your connection. |
| Step 3 | To perform a
			 backup, click the Run Backup button. Note A maximum of two backups are stored. Creating a third backup
				will overwrite the oldest backup. | Note | A maximum of two backups are stored. Creating a third backup
				will overwrite the oldest backup. |
| Note | A maximum of two backups are stored. Creating a third backup
				will overwrite the oldest backup. |
| Step 4 | To restore,
			 select the file you wish to restore and click the Run
				Restore button. |

| Note | At this
				point, you can click the Test
				  Connection button to test your connection. |
|---|---|

| Note | A maximum of two backups are stored. Creating a third backup
				will overwrite the oldest backup. |
|---|---|

| Step 1 | Access the
			 License Definitions page from the main menu by selecting Administration
				> License Definitions . |
|---|---|
| Step 2 | Click the Check for
				Latest Version link to access the Download Software site. Download the
			 desired license definition file to your computer. |
| Step 3 | Click the Install New
				License Definition File button. The Install License Definitions window
			 appears. |
| Step 4 | Click the Browse button to select the license definition file you just downloaded, then click Install . |

| Step 1 | Enter the license
				management security update command. |
|---|---|
| Step 2 | Enter Directory , Server , User Name ,
			 and Password information when prompted, as shown in the following example: Example: Directory:
				/users/bsmith/security_update/update Server:
				se032c-94-61 User Name:
				bsmith Password:
				******** |
| Step 3 | You are then
			 asked to select the security update, as shown in the following example: Example: Available
				options for security update in
				"se032c-94-61:/users/bsmith/security_update/update": 1)
				SecUpd_v1.upd q) quit |
| Step 4 | Select option 1 to
			 download the security update. The following messages appear: Example: Installing
				security update... Continue
				(y/n)? |
| Step 5 | Select y to
			 continue the security update. When the
				update is complete, the following message appears: Security
				update installed. |

| Note | In order to use the rehost portal, you must use the same Cisco.com
		  user ID that initially ordered or fulfilled the licenses. |
|---|---|

| Step 1 | From Product License Registration ( https:/​/​tools.cisco.com/​SWIFT/​LicensingUI/​Quickstart ), choose Licenses . |
|---|---|
| Step 2 | Under the License ID tab of a particular device, choose the license(s) that you want to rehost. |
| Step 3 | In the pop-up that appears, choose Rehost/Transfer . |
| Step 4 | In the Quantity to Assign field, enter the
			 number of licenses you want to transfer. |
| Step 5 | In the License Request field, enter the License Request from the Cisco Prime License Manager of the target device. |
| Step 6 | Click Next . |
| Step 7 | In the Review screen, review your selections. |
| Step 8 | Enter your email address, choose your name
			 from the drop-down list next to End User , and indicate that you agree with the Terms of the License. |
| Step 9 | Click Submit . |
| Step 10 | The rehosted
			 license is emailed to you. It must then be manually installed on
			 Cisco Prime License Manager. Note The license
				can also be downloaded to your machine by clicking Download
				  Target on the License Request Status window and choosing the download location. | Note | The license
				can also be downloaded to your machine by clicking Download
				  Target on the License Request Status window and choosing the download location. |
| Note | The license
				can also be downloaded to your machine by clicking Download
				  Target on the License Request Status window and choosing the download location. |

| Note | The license
				can also be downloaded to your machine by clicking Download
				  Target on the License Request Status window and choosing the download location. |
|---|---|

| Step 1 | From the main
			 menu in Cisco Prime License Manager, select Administration
				> Diagnostic Logs . |
|---|---|
| Step 2 | The Diagnostic
			 Logs screen appears. Under the Log Settings tab, set the log level to Debug for
			 both "Cisco Prime License Manager core services: and "Communication with
			 product instances". Click Save to
			 save your changes. |
| Step 3 | Select the Download
				Logs tab and select the date and time range to include in your log file
			 (the time period during which the issue occurred). Click the Generate Log
				File button. |
| Step 4 | The link to
			 the log file appears below the Generate Log File button. Click the link to
			 download the log file to your PC and then send the log file to Cisco: licensing@cisco.com |

| Note | During this
			 procedure, you must remove and then insert a valid CD or DVD in the disk drive
			 to prove that you have physical access to the system. |
|---|---|

| Step 1 | Log in to the
			 system with the following username and password: Username: pwrecovery Password: pwreset The Welcome
				  to platform password reset window appears. |
|---|---|
| Step 2 | Press any key
			 to continue. |
| Step 3 | If you have a
			 CD or DVD in the disk drive, remove it now. |
| Step 4 | Press any key
			 to continue. The system
				tests to ensure that you removed the CD or DVD from the disk drive. |
| Step 5 | Insert a valid
			 CD or DVD into the disk drive. Note For this
				  test, you must use a data CD, not a music CD. The system tests to ensure that
				  you have inserted the disk. | Note | For this
				  test, you must use a data CD, not a music CD. The system tests to ensure that
				  you have inserted the disk. |
| Note | For this
				  test, you must use a data CD, not a music CD. The system tests to ensure that
				  you have inserted the disk. |
| Step 6 | After the
			 system verifies that you have inserted the disk, you are prompted to enter one
			 of the following options to continue: Enter a to reset the Administrator password. Enter s to reset the security password. Enter q to quit. |
| Step 7 | Enter a new
			 password of the type that you chose. |
| Step 8 | Reenter the
			 new password. The password
				must contain at least six characters. The system checks the new password for
				strength. If the password does not pass the strength check, you are prompted to
				enter a new password. |
| Step 9 | After the
			 system verifies the strength of the new password, the password is reset. You
			 are prompted to press any key to exit the password reset utility. |

| Note | For this
				  test, you must use a data CD, not a music CD. The system tests to ensure that
				  you have inserted the disk. |
|---|---|