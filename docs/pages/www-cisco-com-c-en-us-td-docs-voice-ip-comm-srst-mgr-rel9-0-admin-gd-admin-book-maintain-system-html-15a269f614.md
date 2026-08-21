---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-maintain-system-html-15a269f614
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/maintain_system.html
retrieved_at: 2026-08-21T23:39:33.828373+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 5, 2014

Chapter: Maintaining the Cisco Unified SRST Manager System

## Chapter: Maintaining the Cisco Unified SRST Manager System

## Copying Configurations

Use Cisco Unified SRST Manager EXEC commands to copy the startup configuration and running configuration to and from the hard disk on the Cisco Unified SRST Manager VM, the network FTP server, and the network TFTP server.

Note Depending on the specific TFTP server you are using, you might need to create a file with the same name on the TFTP server and verify that the file has the correct permissions before transferring the running configuration to the TFTP server.

### Copying the Startup Configuration from the Hard Disk to Another Location

Starting in Cisco Unified SRST Manager EXEC mode, use the following command to copy the startup configuration on the hard disk to another location:

copy startup-config { ftp: user-id : password @ ftp-server-url | tftp: tftp-server-url }

### Syntax Description

ftp: user-id : password @

Username and password for the FTP server. Include the colon (:) and the “at” sign (@) in your entry.

ftp-server-url

URL of the FTP server including directory and filename (for example, ftps://server/dir/filename)

tftp: tftp-server-url

URL of the TFTP server including directory and filename (for example, tftps://server/dir/filename)

This command is interactive and prompts for the required information. You cannot enter the parameters in one line. The following examples illustrate this process.

In this example, the startup configuration is copied to the FTP server, which requires a username and password to transfer files. The startup configuration file is saved on the FTP server with the filename start .

The following example shows the startup configuration copied to the TFTP server, which does not require a username and password. The startup configuration is saved in the TFTP directory configs as filename temp_start .

Note Depending on the specific TFTP server, you might need to create a file with the same name on the TFTP server and verify that the file has the correct permissions before transferring the running configuration to the TFTP server.

### Copying the Startup Configuration from the Network FTP Server to Another Location

Starting in Cisco Unified SRST Manager EXEC mode, use the following command to copy the startup configuration on the network FTP server to another location:

copy ftp: { running-config | startup-config } user-id:password @ftps:// server/dir/filename

### Syntax Description

running-config

Active configuration on hard disk.

startup-config

Startup configuration on hard disk.

user-id : password @

Username and password for the FTP server. Include the colon (:) and the at sign (@) in your entry.

ftp-server-url

URL of the FTP server.

This command is interactive and prompts you for the information. You cannot enter the parameters in one line. The following example illustrates this process.

### Examples

In this example, the FTP server requires a username and password. The file start in the FTP server configs directory is copied to the startup configuration.

Note Depending on the specific TFTP server, you might need to create a file with the same name on the TFTP server and verify that the file has the correct permissions before transferring the running configuration to the TFTP server.

### Copying the Running Configuration from the Hard Disk to Another Location

Starting in Cisco Unified SRST Manager EXEC mode, use the following command to copy the running configuration on the hard disk to another location:

copy running-config {ftp: user-id:password @ftps:// server/dir/filename | startup-config | tftp:tftps:// server/dir/filename }

### Syntax Description

ftp: user-id : password @

Username and password for the FTP server. Include the colon (:) and the at sign (@) in your entry.

ftp-server-url

URL of the FTP server including directory and filename..

startup-config

Startup configuration on hard disk.

tftp-server-url

URL of the TFTP server including directory and filename.

When you copy the running configuration to the startup configuration, enter the command on one line.

When you copy to the FTP or TFTP server, this command becomes interactive and prompts you for the information. You cannot enter the parameters in one line. The following example illustrates this process.

### Examples

In the following example, the running configuration is copied to the FTP server, which requires a username and password. The running configuration is copied to the configs directory as file saved_start.

In the following example, the running configuration is copied to the startup configuration. In this instance, enter the command on a single line.

Note Depending on the specific TFTP server, you might need to create a file with the same name on the TFTP server and verify that the file has the correct permissions before transferring the running configuration to the TFTP server.

### Copying the Running Configuration from the Network TFTP Server to Another Location

Starting in Cisco Unified SRST Manager EXEC mode, use the following command to copy the running configuration from the network TFTP server to another location:

copy t ftp: { running-config | startup-config } tftps: //server/dir/filename

### Syntax Description

running-config

Active configuration on hard disk.

startup-config

Startup configuration on hard disk.

tftp-server-url

URL of the TFTP server.

This command is interactive and prompts you for the information. You cannot enter the parameters in one line. The following example illustrates this process.

### Examples

In this example, the file start in directory configs on the TFTP server is copied to the startup configuration.

Note Depending on the specific TFTP server, you might need to create a file with the same name on the TFTP server and verify that the file has the correct permissions before transferring the running configuration to the TFTP server.

## Restoring Factory Default Values

Cisco Unified SRST Manager provides a command to restore the factory default values for the entire system. Restoring the system to the factory defaults erases the current configuration. This function is available in offline mode. When the system is clean, a message appears indicating that the system will reload, and the system begins to reload. When the reload is complete, the system prompts you to start the post-installation process.

Step 1 Enter the following to put the system into offline mode:

Step 2 Enter the following:

The system displays a message stating that this will cause all the configuration and data on the system to be erased and this is not reversible, and asks if you want to continue.

Step 3 Do one of the following:

- Enter n to retain the system configuration and data.

The operation is cancelled, but the system remains in offline mode. To return to online mode, enter continue .

- Enter y to erase the system configuration and data.

When the system is clean, a message appears indicating that the system will start to reload. When the reload is complete, a prompt appears to start the post-installation process.

## Going Offline, Reloading, Rebooting, Shutting Down, and Going Back Online

You must take the Cisco Unified SRST Manager system offline before you can back up, reload, or restore the system; however, you do not need to take the system offline to shut down the system.

Shut down Cisco Unified SRST Manager from the console or CLI interface before powering off the virtual machine from the vSphere client/vCenter application.

### Taking the Cisco Unified SRST Manager System Offline

Using the offline command in Cisco Unified SRST Manager EXEC mode takes the system into offline/administration mode. When you use the offline command, the system prompts you for confirmation. The default is “no,” so to confirm, you must enter y for “yes.”

Step 1 Enter the following command:

offline

Step 2 Enter y to confirm.

### Example

### Restarting the Cisco Unified SRST Manager System

To restart the system using the starting configuration, use the reload command in Cisco Unified SRST Manager offline/administration mode. Restarting the system will terminate all end-user sessions and cause any unsaved configuration data to be lost.

Step 1 Enter the following command:

reload

### Example

### Shutting Down the Cisco Unified SRST Manager System

To halt the system, use the shutdown command in Cisco Unified SRST Manager EXEC mode.

### Shutting Down the Software

Step 1 Enter the following command:

shutdown

### Shutting Down the VM

Power off the VM using the VMware management application.

| ftp: user-id : password @ | Username and password for the FTP server. Include the colon (:) and the “at” sign (@) in your entry. |
|---|---|
| ftp-server-url | URL of the FTP server including directory and filename (for example, ftps://server/dir/filename) |
| tftp: tftp-server-url | URL of the TFTP server including directory and filename (for example, tftps://server/dir/filename) |

| running-config | Active configuration on hard disk. |
|---|---|
| startup-config | Startup configuration on hard disk. |
| user-id : password @ | Username and password for the FTP server. Include the colon (:) and the at sign (@) in your entry. |
| ftp-server-url | URL of the FTP server. |

| ftp: user-id : password @ | Username and password for the FTP server. Include the colon (:) and the at sign (@) in your entry. |
|---|---|
| ftp-server-url | URL of the FTP server including directory and filename.. |
| startup-config | Startup configuration on hard disk. |
| tftp-server-url | URL of the TFTP server including directory and filename. |

| running-config | Active configuration on hard disk. |
|---|---|
| startup-config | Startup configuration on hard disk. |
| tftp-server-url | URL of the TFTP server. |