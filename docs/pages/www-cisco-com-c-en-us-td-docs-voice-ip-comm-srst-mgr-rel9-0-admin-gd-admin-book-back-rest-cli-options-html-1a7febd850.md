---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-back-rest-cli-options-html-1a7febd850
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/back_rest_cli_options.html
retrieved_at: 2026-08-21T23:39:50.850868+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 11, 2014

Chapter: Backing Up and Restoring Data Using the CLI

## Chapter: Backing Up and Restoring Data Using the CLI

## Backup and Restore Using SFTP

### Overview

You can transfer files from any Cisco Unified SRST Manager application to and from the backup server using Secure File Transfer Protocol (SFTP). SFTP provides data integrity and confidentiality that is not provided by FTP.

Because SFTP is based on Secure Shell tunnel version 2 (SSHv2), only SSHv2 servers are supported for this feature.

To run backup and restore over SFTP, you must configure the URL of the backup server in the form of sftp:// hostname / dir , in addition to the username and password to log in to the server. The backup server must have an SSH daemon running with the SFTP subsystem enabled. The SSH protocol allows various user authentication schemes.

### Performing Backup and Restore Using SFTP

### Prerequisites

Cisco Unified SRST Manager 9.0 or a later version.

### Required Data for This Procedure

There is no data required.

### SUMMARY STEPS

1. config t

2. backup { revisions number | server url sftp-url username sftp-username password sftp-password }

3. end

### DETAILED STEPS

Step 1

config t

srstmgr-1# config t

Enters configuration mode.

Step 2

backup { revisions number | server url sftp-url username sftp-username password sftp-password }

Performs a backup to the specified SFTP or FTP server. To use SFTP, the URL must be of the form sftp:// hostname / directory .

Step 3

end

srstmgr-1(config)# end

Returns to EXEC mode.

## Backup Server Authentication Using a SSH Host Key

### Overview

You can authenticate the backup server using the SSH protocol before starting a backup/restore operation. The SSH protocol uses public key cryptography for server authentication.

This feature provides two methods of authenticating a server:

- Establishing a secure connection based only on the URL of a trusted backup server.

- Obtaining the fingerprint of the backup server and using it to establish a secure connection. This fingerprint is also known as the host key or private key.

The first method is easier than the second method, but it is less secure because it does not depend on knowledge of the backup server’s private host key. However, if you know the URL of a trusted backup server, it is generally safe. In this case, the backup server securely provides the client with its private host key.

In both cases, when server authentication is enabled, the system validates the SSH server’s private host key by comparing the fingerprint of the key received from the server with a preconfigured string. If the two fingerprints do not match, the SSH handshake fails, and the backup/restore operation does not occur.

You cannot use the GUI to configure this feature; you must use the CLI.

Both methods are explained in the following sections.

### Configuring Backup Server Authentication Without Using the SSH Host Key

### Prerequisites

Cisco Unified SRST Manager 9.0 or a later version

### Required Data for This Procedure

To enable SSH authentication of a backup server without knowing the server’s fingerprint (private host key), you must know the URL of a trusted backup server.

### SUMMARY STEPS

1. config t

2. backup server url sftp:// url

3. backup server authenticate

4. end

5. show security ssh knownhost

### DETAILED STEPS

Step 1

config t

srstmgr-1# config t

Enters configuration mode.

Step 2

backup server url sftp:// url

Establishes an initial connection with the backup server.

Step 3

backup server authenticate

Retrieves the fingerprint of the backup server’s host key and establishes a secure SSH connection.

Step 4

end

srstmgr-1(config)# end

Returns to EXEC mode.

Step 5

show security ssh knownhost

Displays a list of configured SSH servers and their fingerprints.

### Configuring Backup Server Authentication Using the SSH Host Key

### Prerequisites

Cisco Unified SRST Manager 9.0 or a later version

### Required Data for This Procedure

To use a backup server’s fingerprint (private host key) to enable SSH authentication, you must first retrieve the fingerprint “out-of-band” by running the ssh-keygen routine on the backup server. This routine is included in the OpenSSH package. The following example shows the command and its output:

ssh-keygen -l -f /etc/ssh/ssh_host_dsa_key.pub

1024 4d:5c:be:1d:93:7b:7c:da:56:83:e0:02:ba:ee:37:c1 /etc/ssh/ssh_host_dsa_key.pub

### SUMMARY STEPS

1. config t

2. security ssh knownhost host {ssh-rsa | ssh-dsa} fingerprint-string

3. end

4. show security ssh knowhost

### DETAILED STEPS

Step 1

config t

srstmgr-1# config t

Enters configuration mode.

Step 2

security ssh knownhost host {ssh-rsa | ssh-dsa} fingerprint-string

Configures the MD5 fingerprint of the SSH server’s host key using the following arguments and keywords:

host — Fully qualified hostname or IP address of the SSH server.

ssh-rsa — RSA algorithm was used to create this fingerprint for a SSH server’s host key.

ssh-dsa — DSA algorithm was used to create this fingerprint for a SSH server’s host key.

fingerprint-string — MD5 fingerprint string.

Step 3

end

srstmgr-1(config)# end

Returns to EXEC mode.

Step 4

show security ssh knownhost

Displays a list of configured SSH servers and their fingerprints.

## Encrypting and Signing of Backup Content on the Server

### Overview

You can protect backed up configuration and data files using signing and encryption before the files are transferred to the backup server.

To enable this feature, you must configure a master key from which the encryption and signing key (known as the session key) are derived. The backup files are encrypted and signed before they are sent to the backup server. When restoring the files, the master key is used to validate the integrity of the files and decrypt them accordingly. You can also restore the backup files to any other machine running Cisco Unified SRST Manager 9.0 or later versions, if you configure the same master key before you begin the restore process. To make it easier to automate a scheduled backup, the master key is stored securely on the hosting device. It is not included in the backup content.

During the restore process, if the system detects that backup content has been tampered with, the restore process aborts. The system also halts and waits for the administrator to take some action, such as restoring using a different revision.

For backward compatibility, you can allow unsigned backup files to be restored if the risk is acceptable.

### Configuring the Encryption and Signing of Backup Content on the Server

### Prerequisites

Cisco Unified SRST Manager 9.0 or a later version

### Required Data for This Procedure

There is no data required.

### SUMMARY STEPS

1. config t

2. backup security key generate

3. backup security protected

4. backup security enforced

5. end

### DETAILED STEPS

Step 1

config t

srstmgr-1# config t

Enters configuration mode.

Step 2

backup security key generate

Creates the master key used for encrypting and signing the backup files.

Step 3

backup security protected

Enables secure mode for backups. In secure mode, all backup files are protected using encryption and a signature.

Step 4

backup security enforced

Specifies that only protected and untampered backup files are restored.

Step 5

end

srstmgr-1(config)# end

Returns to EXEC mode.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | config t srstmgr-1# config t | Enters configuration mode. |
| Step 2 | backup { revisions number \| server url sftp-url username sftp-username password sftp-password } srstmgr-1(config)# backup server url sftp://branch/vmbackups username admin password mainserver | Performs a backup to the specified SFTP or FTP server. To use SFTP, the URL must be of the form sftp:// hostname / directory . |
| Step 3 | end srstmgr-1(config)# end | Returns to EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | config t srstmgr-1# config t | Enters configuration mode. |
| Step 2 | backup server url sftp:// url srstmgr-1(config)# backup server url sftp://company.com/server22 | Establishes an initial connection with the backup server. |
| Step 3 | backup server authenticate srstmgr-1(config)# backup server authenticate | Retrieves the fingerprint of the backup server’s host key and establishes a secure SSH connection. |
| Step 4 | end srstmgr-1(config)# end | Returns to EXEC mode. |
| Step 5 | show security ssh knownhost srstmgr-1(config)# show security ssh knownhost | Displays a list of configured SSH servers and their fingerprints. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | config t srstmgr-1# config t | Enters configuration mode. |
| Step 2 | security ssh knownhost host {ssh-rsa \| ssh-dsa} fingerprint-string srstmgr-1(config)# security ssh knownhost server.cisco.com ssh-rsa a5:3a:12:6d:e9:48:a3:34:be:8f:ee:50:30:e5:e6:c3 | Configures the MD5 fingerprint of the SSH server’s host key using the following arguments and keywords: host — Fully qualified hostname or IP address of the SSH server. ssh-rsa — RSA algorithm was used to create this fingerprint for a SSH server’s host key. ssh-dsa — DSA algorithm was used to create this fingerprint for a SSH server’s host key. fingerprint-string — MD5 fingerprint string. |
| Step 3 | end srstmgr-1(config)# end | Returns to EXEC mode. |
| Step 4 | show security ssh knownhost srstmgr-1(config)# show security ssh knownhost | Displays a list of configured SSH servers and their fingerprints. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | config t srstmgr-1# config t | Enters configuration mode. |
| Step 2 | backup security key generate srstmgr-1(config)# backup security key generate | Creates the master key used for encrypting and signing the backup files. |
| Step 3 | backup security protected srstmgr-1(config)# backup security protected | Enables secure mode for backups. In secure mode, all backup files are protected using encryption and a signature. |
| Step 4 | backup security enforced srstmgr-1(config)# backup security enforced | Specifies that only protected and untampered backup files are restored. |
| Step 5 | end srstmgr-1(config)# end | Returns to EXEC mode. |