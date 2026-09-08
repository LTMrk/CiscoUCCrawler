---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-11-0-1-userguide-cplm-bk-u2c0c808-00-user-guide-rel-1101-cplm-bk-u2-67cde74a16
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/11_0_1/userguide/CPLM_BK_U2C0C808_00_user-guide-rel-1101/CPLM_BK_U2C0C808_00_user-guide-rel-1101_chapter_010.html
retrieved_at: 2026-09-08T05:00:49.120808+00:00
---

Cisco Prime License Manager User Guide, Release 11.0(1)

# Cisco Prime License Manager User Guide, Release 11.0(1)

Updated: September 12, 2017

Chapter: Upgrade

## Chapter: Upgrade

# Upgrade

## Upgrade Software
	 Using the Cisco Prime License Manager GUI

You can upgrade software or apply a patch using a COP file. Use one of
		  the following options to upgrade software using the Cisco Prime License Manager
		  GUI:

Upgrade from a
				remote file system

Upgrade from a
				local source

- Upgrade from
	 a Remote File System

- Upgrade from a Local
	 Source

### Upgrade from
	 a Remote File System

To upgrade the
		  software from an FTP or SFTP server, use the following procedure.

Copy the application ISO file to an FTP server that is accessible from Cisco
		  Prime License Manager.

The
				Install/Upgrade Software dialog box opens.

Enter
				following information:

- IP Address/Hostname

- Username

- Password

- Directory (the path to the
				location where you placed the ISO)

- Transfer Protocol (select either FTP or SFTP from the drop-down menu)

### Upgrade from a Local
	 Source

Define the media source of the virtual machine. For example, is it an ISO file in the datastore or a physical optical drive on the client or host. Check the Connected checkbox for the VM CD/DVD drive.

## Upgrade Software
	 Using the Cisco Prime License Manager CLI

You can upgrade software or apply a patch using a COP file. To initiate an
		  upgrade from a local or remote source using CLI commands, use the following
		  procedures.

### Upgrade from
	 Remote Source

To upgrade the software from an FTP server, use the following procedure. Keep in mind that this procedure uses example software versions. For the latest software version, see the appropriate Release Notes for Cisco Prime License Manager .

You need to place
		  the ISO on a network location or remote drive that is accessible from Cisco
		  Prime License Manager prior to starting this procedure.

```
admin:utils system upgrade initiate
```

Warning: Do not close this window without first canceling the upgrade.

Source:

1) Remote Filesystem via SFTP

2) Remote Filesystem via FTP

3) Local DVD/CD

q) quit

Please select an option (1 - 3 or "q" ):

Directory: /software/PLM/10.0.0.98030-1

Server: ftp.mycompany.com

User Name: bsmith

Password: ********

Checking for valid upgrades. Please wait...

Available options and upgrades in
				  "se032c-94-61:/software/PLM/10.0.0.98030-1":

1) CiscoPrimeLM_64bitLnx_10.0.0.98030-1.sgn.iso

q) quit

Accessing the file. Please wait...

Validating the file...

Downloaded 935 MB.

Checksumming the file...

A system reboot is required when the upgrade process completes or is canceled. This will ensure services affected by the upgrade process are functioning properly.

Downloaded: CiscoPrimeLM_64bitLnx_10.0.0.98030-1.sgn.iso

File version: 10.0.0.98030-1

File checksum: c4:13:ad:95:7b:c8:c1:01:1b:91:bb:da:8d:84:09:ea

Automatically switch
				versions if the upgrade is successful (yes/no): yes

Start
				installation (yes/no): yes

### Upgrade from Local
	 Source

To upgrade the software from an FTP server, use the following procedure. Keep in mind that this procedure uses example software versions. For the latest software version, see the appropriate Release Notes for Cisco Prime License Manager .

Define the media source of the virtual machine. For example, is it an ISO file in the datastore or a physical optical drive on the client or host. Check the Connected checkbox for the VM CD/DVD drive.

```
admin:utils system upgrade initiate
```

Warning: Do not close this window without first canceling the upgrade.

Source:

1) Remote Filesystem via SFTP

2) Remote Filesystem via FTP

3) Local DVD/CD

q) quit

Please select an option (1 - 3 or "q" ):

Accessing the file. Please wait...

Validating the file...

Downloaded 935 MB.

Checksumming the file...

A system reboot is required when the upgrade process completes or is canceled. This will ensure services affected by the upgrade process are functioning properly.

Downloaded: CiscoPrimeLM_64bitLnx_10.0.0.98030-1.sgn.iso

File version: 10.0.0.98030-1

File checksum: c4:13:ad:95:7b:c8:c1:01:1b:91:bb:da:8d:84:09:ea

Automatically switch versions if the upgrade is successful (yes/no): yes

```
Start installation (yes/no): yes
```

## Post-Upgrade
	 Tasks

After the upgrade,
		  perform the following tasks:

Check the
			 version number in the About box to verify that it is the expected upgraded
			 version.

Perform a
			 synchronization by selecting Product
				Instances > Synchronize Now .

Check the
			 Dashboard to verify that there are no alerts and then run a backup by selecting Administration > Backup/Restore .

| Step 1 | From the Cisco
			 Prime License Manager main menu, select Administration > Install/Upgrade . The
			 Install/Upgrade page opens. |
|---|---|
| Step 2 | Click Install/Upgrade
				Software . The
				Install/Upgrade Software dialog box opens. |
| Step 3 | Click Install/Upgrade from Network (this option
			 should be selected by default). Enter
				following information: IP Address/Hostname Username Password Directory (the path to the
				location where you placed the ISO) Transfer Protocol (select either FTP or SFTP from the drop-down menu) |
| Step 4 | Click Next . |
| Step 5 | All valid
			 upgrades are listed in the table. Select the required upgrade file
			 from the list. Note There
				can be multiple options listed. | Note | There
				can be multiple options listed. |
| Note | There
				can be multiple options listed. |
| Step 6 | Click Start
				Installation/Upgrade . A message appears asking you to confirm the
			 upgrade. Click Continue to begin the upgrade. Note You can leave
				  the screen up while the upgrade is in progress, as it provides feedback on the
				  progress of the upgrade, or close the browser. The upgrade proceeds even if you close the browser. The upgrade may take 45 minutes to an hour to
				  complete. | Note | You can leave
				  the screen up while the upgrade is in progress, as it provides feedback on the
				  progress of the upgrade, or close the browser. The upgrade proceeds even if you close the browser. The upgrade may take 45 minutes to an hour to
				  complete. |
| Note | You can leave
				  the screen up while the upgrade is in progress, as it provides feedback on the
				  progress of the upgrade, or close the browser. The upgrade proceeds even if you close the browser. The upgrade may take 45 minutes to an hour to
				  complete. |

| Note | There
				can be multiple options listed. |
|---|---|

| Note | You can leave
				  the screen up while the upgrade is in progress, as it provides feedback on the
				  progress of the upgrade, or close the browser. The upgrade proceeds even if you close the browser. The upgrade may take 45 minutes to an hour to
				  complete. |
|---|---|

| Step 1 | From the Cisco
			 Prime License Manager main menu, select Administration > Install/Upgrade . |
|---|---|
| Step 2 | Click Install/Upgrade
				Software . |
| Step 3 | Click Install/Upgrade from DVD/CD drive on Cisco Prime License Manager
				server . |
| Step 4 | All valid
			 upgrades are listed in the table. Select the appropriate (valid) upgrade file
			 from the list. |
| Step 5 | Click Start
				Installation/Upgrade . |
| Step 6 | Click Continue to begin the upgrade. Note You can either leave the
				  screen up while the upgrade is in progress or close your browser. Closing your browser does not impact the upgrade process. The upgrade may take 45 minutes to an hour to
				  complete. | Note | You can either leave the
				  screen up while the upgrade is in progress or close your browser. Closing your browser does not impact the upgrade process. The upgrade may take 45 minutes to an hour to
				  complete. |
| Note | You can either leave the
				  screen up while the upgrade is in progress or close your browser. Closing your browser does not impact the upgrade process. The upgrade may take 45 minutes to an hour to
				  complete. |

| Note | You can either leave the
				  screen up while the upgrade is in progress or close your browser. Closing your browser does not impact the upgrade process. The upgrade may take 45 minutes to an hour to
				  complete. |
|---|---|

| Step 1 | Enter the utils system
				upgrade initiate command, as shown in the following example. Example: admin:utils system upgrade initiate The
			 following options appear: Warning: Do not close this window without first canceling the upgrade. Source: 1) Remote Filesystem via SFTP 2) Remote Filesystem via FTP 3) Local DVD/CD q) quit Please select an option (1 - 3 or "q" ): |
|---|---|
| Step 2 | Select either option
			 1 or 2. |
| Step 3 | Enter
			 Directory, Server, User Name, and Password information when prompted. Directory: /software/PLM/10.0.0.98030-1 Server: ftp.mycompany.com User Name: bsmith Password: ******** Checking for valid upgrades. Please wait... |
| Step 4 | Enter SMTP
				Host Server (optional) to receive email notification once upgrade
			 is complete. The
			 following options appear: Available options and upgrades in
				  "se032c-94-61:/software/PLM/10.0.0.98030-1": 1) CiscoPrimeLM_64bitLnx_10.0.0.98030-1.sgn.iso q) quit |
| Step 5 | Select option 1 to download upgrade file. Accessing the file. Please wait... Validating the file... Downloaded 935 MB. Checksumming the file... A system reboot is required when the upgrade process completes or is canceled. This will ensure services affected by the upgrade process are functioning properly. Downloaded: CiscoPrimeLM_64bitLnx_10.0.0.98030-1.sgn.iso File version: 10.0.0.98030-1 File checksum: c4:13:ad:95:7b:c8:c1:01:1b:91:bb:da:8d:84:09:ea |
| Step 6 | When
			 asked to automatically switch versions if the upgrade is successful, enter yes. Automatically switch
				versions if the upgrade is successful (yes/no): yes |
| Step 7 | Enter yes to
			 start installation. Start
				installation (yes/no): yes |

| Step 1 | Insert the new
			 DVD into the disc drive on the local server that is to be upgraded. |
|---|---|
| Step 2 | Enter the utils system
				upgrade initiate command, as shown in the following example. Example: admin:utils system upgrade initiate The
			 following options appear: Warning: Do not close this window without first canceling the upgrade. Source: 1) Remote Filesystem via SFTP 2) Remote Filesystem via FTP 3) Local DVD/CD q) quit Please select an option (1 - 3 or "q" ): |
| Step 3 | Select option
			 3. |
| Step 4 | Select option 1 to download upgrade file. Accessing the file. Please wait... Validating the file... Downloaded 935 MB. Checksumming the file... A system reboot is required when the upgrade process completes or is canceled. This will ensure services affected by the upgrade process are functioning properly. Downloaded: CiscoPrimeLM_64bitLnx_10.0.0.98030-1.sgn.iso File version: 10.0.0.98030-1 File checksum: c4:13:ad:95:7b:c8:c1:01:1b:91:bb:da:8d:84:09:ea |
| Step 5 | When
			 asked to automatically switch versions if the upgrade is successful, enter yes. Automatically switch versions if the upgrade is successful (yes/no): yes |
| Step 6 | Enter yes to start installation. Start installation (yes/no): yes |