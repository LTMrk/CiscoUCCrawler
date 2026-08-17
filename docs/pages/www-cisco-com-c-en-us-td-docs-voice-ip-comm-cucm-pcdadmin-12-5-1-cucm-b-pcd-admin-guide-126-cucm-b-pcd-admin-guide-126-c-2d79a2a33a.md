---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-pcdadmin-12-5-1-cucm-b-pcd-admin-guide-126-cucm-b-pcd-admin-guide-126-c-2d79a2a33a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/pcdadmin/12_5_1/cucm_b_pcd-admin-guide_126/cucm_b_pcd-admin-guide_126_chapter_010.html
retrieved_at: 2026-08-17T00:33:45.382974+00:00
---

Prime Collaboration Deployment Administration Guide, Release 12.6(1)

# Prime Collaboration Deployment Administration Guide, Release 12.6(1)

Updated: November 27, 2025

Chapter: Upgrade Cisco Prime Collaboration Deployment

## Chapter: Upgrade Cisco Prime Collaboration Deployment

- Upgrade Cisco Prime Collaboration Deployment

- Upgrade Cisco                              	 Prime Collaboration Deployment Using CLI

# Upgrade Cisco Prime Collaboration Deployment

## Upgrade Cisco
                        	 Prime Collaboration Deployment Using CLI

To upgrade the software version of Cisco Prime Collaboration Deployment, use the utils system upgrade initiate CLI command. There are four options, depending on where you have placed the new ISO file on an external filesystem or on
                              Cisco Prime Collaboration Deployment itself.

### Before you begin

You must place the non-bootable ISO file on a network location or
                              		  remote drive that is accessible from Cisco Prime Collaboration Deployment.

Step 1

If you want to place the ISO on Cisco Prime Collaboration Deployment, upload it to the Cisco Prime Collaboration Deployment
                                       server /upgrade folder by performing the following steps:

sftp adminsftp@<Cisco Prime Collaboration Deployment IP>

cd upgrade

put <name of iso file>

Step 2

Log on to the CLI interface of the Cisco Prime Collaboration
                                       			 Deployment server, and use the utils system upgrade initiate CLI command.

```
Warning: Do not close this window without first canceling the upgrade.

1) Remote Filesystem via SFTP
2) Remote Filesystem via FTP
3) Local DVD/CD
4) Local Upload Directory
q) quit

Please select an option (1-4 or "q" ):
```

Step 3

Perform one of the following steps:

- If the ISO file is in the /upgrade folder of Cisco Prime Collaboration Deployment, choose option 4 .

- If the ISO file is on a remote file system, choose option 1 or 2 , depending on whether you wish to use SFTP or FTP.

Step 4

The system searches the directory for files to upgrade to and
                                       			 displays those filenames. Select the file that you wish to upgrade the Cisco
                                       			 Prime Collaboration Deployment system to by choosing the number of that file.

Step 5

Indicate whether you want the system to automatically switch to
                                       			 the upgraded version if the upgrade is successful.

### Example:

```
Automatically switch
				versions if the upgrade is successful (yes/no): yes
```

Step 6

Start the installation:

```
Start installation (yes/no): yes
The upgrade log is install_log_2013-10-07.20.57.17.log
Upgrading the system. Please wait...
10/07/2013 20:57:18 file_list.sh|Starting file_list.sh|<LVL::Info>
10/07/2013 20:57:18 file_list.sh|Parse argument method=local_upload_dir|<LVL::Debug>
10/07/2013 20:57:18 file_list.sh|Parse argument source_dir=|<LVL::Debug>
10/07/2013 20:57:18 file_list.sh|Parse argument dest_file=/var/log/install/downloaded_versions|<LVL::Debug>
```

The installation begins.

Step 7

After the installation is complete, use the show version active CLI command to see the current
                                       			 version of your Cisco Prime Collaboration Deployment software.

### Example:

```
Active Master Version: 11.0.x.xxxxx-xxxx
Active Version Installed Software Options:
No Installed Software Options Found.
```

| Step 1 | If you want to place the ISO on Cisco Prime Collaboration Deployment, upload it to the Cisco Prime Collaboration Deployment
                                       server /upgrade folder by performing the following steps: sftp adminsftp@<Cisco Prime Collaboration Deployment IP> cd upgrade put <name of iso file> Note If you are using a remote file system, place the ISO file there. Be sure that it can be accessed through SFTP or FTP. | Note | If you are using a remote file system, place the ISO file there. Be sure that it can be accessed through SFTP or FTP. |
|---|---|---|---|
| Note | If you are using a remote file system, place the ISO file there. Be sure that it can be accessed through SFTP or FTP. |
| Step 2 | Log on to the CLI interface of the Cisco Prime Collaboration
                                       			 Deployment server, and use the utils system upgrade initiate CLI command. You will be asked to choose an option, based on where your ISO is located. Warning: Do not close this window without first canceling the upgrade.

1) Remote Filesystem via SFTP
2) Remote Filesystem via FTP
3) Local DVD/CD
4) Local Upload Directory
q) quit

Please select an option (1-4 or "q" ): |
| Step 3 | Perform one of the following steps: If the ISO file is in the /upgrade folder of Cisco Prime Collaboration Deployment, choose option 4 . If the ISO file is on a remote file system, choose option 1 or 2 , depending on whether you wish to use SFTP or FTP. |
| Step 4 | The system searches the directory for files to upgrade to and
                                       			 displays those filenames. Select the file that you wish to upgrade the Cisco
                                       			 Prime Collaboration Deployment system to by choosing the number of that file. |
| Step 5 | Indicate whether you want the system to automatically switch to
                                       			 the upgraded version if the upgrade is successful. Example: Automatically switch
				versions if the upgrade is successful (yes/no): yes |
| Step 6 | Start the installation: Start installation (yes/no): yes
The upgrade log is install_log_2013-10-07.20.57.17.log
Upgrading the system. Please wait...
10/07/2013 20:57:18 file_list.sh\|Starting file_list.sh\|<LVL::Info>
10/07/2013 20:57:18 file_list.sh\|Parse argument method=local_upload_dir\|<LVL::Debug>
10/07/2013 20:57:18 file_list.sh\|Parse argument source_dir=\|<LVL::Debug>
10/07/2013 20:57:18 file_list.sh\|Parse argument dest_file=/var/log/install/downloaded_versions\|<LVL::Debug> The installation begins. |
| Step 7 | After the installation is complete, use the show version active CLI command to see the current
                                       			 version of your Cisco Prime Collaboration Deployment software. Example: Active Master Version: 11.0.x.xxxxx-xxxx
Active Version Installed Software Options:
No Installed Software Options Found. |

| Note | If you are using a remote file system, place the ISO file there. Be sure that it can be accessed through SFTP or FTP. |
|---|---|