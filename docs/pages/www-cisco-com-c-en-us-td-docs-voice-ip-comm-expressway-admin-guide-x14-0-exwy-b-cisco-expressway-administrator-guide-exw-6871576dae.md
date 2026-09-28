---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-admin-guide-x14-0-exwy-b-cisco-expressway-administrator-guide-exw-6871576dae
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/X14-0/exwy_b_cisco-expressway-administrator-guide/exwy_m_maintenance.html
retrieved_at: 2026-08-16T22:44:39.120744+00:00
---

Cisco Expressway Administrator Guide (X14.0)

# Cisco Expressway Administrator Guide (X14.0)

Updated: April 14, 2021

Chapter: Maintenance

## Chapter: Maintenance

# Maintenance

This section describes the options on the Configuration > Maintenance menu.

## Enable Maintenance Mode

Maintenance mode is typically used when you need to upgrade or take out of service an Expressway peer that is part of a cluster.
                              It allows the other cluster peers to continue to operate normally while the peer that is in maintenance mode is upgraded or
                              serviced. Putting a peer into maintenance mode provides a controlled method of stopping any further registrations or calls
                              from being managed by that peer.

An alarm is raised while the peer is in maintenance mode. You can monitor the Resource usage page ( Status > System > Resource usage ) to check how many registrations and calls are currently being handled by that peer.

When a peer is in maintenance mode, its workload is handled by the other cluster nodes. For large multitenant deployments
                              or MRA deployments therefore, we recommend that you only enable maintenance mode on one peer at a time, to avoid overloading
                              the other nodes.

### Impact on Active Calls and Registrations

#### Standard Expressway sessions (not MRA)

New calls and registrations will be handled by another peer in the cluster.

Existing registrations are allowed to expire and then should reregister to another peer (see Expressway Cluster Creation and Maintenance Deployment Guide for more information about endpoint configuration and setting up DNS SRV records).

Existing calls continue until the call is terminated.

#### Unified CM MRA sessions

Expressway stops accepting new calls or proxy (MRA) traffic. Existing calls and chat sessions are not affected.

As users end their sessions normally, the system comes to a point when it is not processing any traffic of a certain type,
                                 and then it shuts that service down.

If users try to make new calls or start new chat sessions while the Expressway is in maintenance mode, the clients will receive
                                 a service unavailable response, and they might then choose to use another peer (if they are capable). This fail-over behavior
                                 depends on the client, but restarting the client should resolve any connection issues if there are active peers in the cluster.

The Unified Communications status pages also show ( Maintenance Mode ) in any places where MRA services are affected.

### Process to Enable Maintenance Mode

Log to in the relevant peer.

Go to the Maintenance mode page Maintenance > Maintenance mode .

Set Maintenance mode to On .

Click Save and Click Ok on the confirmation dialog.

Maintenance mode is automatically disabled if the peer is restarted.

#### How to Manually Remove Calls or Registrations

To manually remove any calls or registrations that don't clear automatically:

Go to Status > Calls , click Select all and then click Disconnect (SIP calls may not disconnect immediately).

Go to Status > Registrations > By device , click Select all and then click Unregister .

You can leave the Conference Factory registration. This will not be the source of calls, and even if deleted will not roll
                                 over to another peer, as other peers have their own Conference Factory registration (if enabled).

## Enabling SSH Access to Expressway

You will use root access to authorize your public key. Take care not to increase your security exposure or cause any unsupported
                                          configuration. We strongly discourage using root .

Use SSH to log in as root .

Enter mkdir /tandberg/.ssh to create .ssh directory if it is not already present.

Copy your public key to /tandberg/.ssh .

Append your public key to the authorized_keys file with cat /tandberg/.ssh/ id_rsa.pub >> /tandberg/.ssh/authorized_keys .

Where id_rsa.pub is substituted with the name of your public key. Do not place your key anywhere else because the key could be lost on upgrade
                                          ( authorized_keys file does persist)

Log off and test SSH access using your own key

If you cannot access the Expressway with your key, you may need to connect as root and restart the SSH daemon with /etc/init.d/sshd restart .

## Upgrading Expressway Software

This section describes how to install new releases of Expressway software components onto an existing system. Component upgrades
                              can be performed in one of two ways:

Using the web interface - recommended approach using the Maintenance > Upgrade page. Full instructions are in the relevant release notes for the software.

Using secure copy (SCP/PSCP) - alternative approach. This method may be useful in specific cases such as with a slow or unstable network connection.

### No downgrading support

Downgrading to an older version is not supported.

### Upgrading Using Secure Copy (SCP/PSCP)

Before you begin

The process requires the software image file to be manually renamed to the filename expected by the system. We recommend that
                                    you upload the file with its default name (similar to s42700xXX_XX_XX.tar.gz ) and rename it only when you are ready to start (install) the upgrade. This provides better control of the process and also
                                    lets you check the file size before you proceed.

Depending on the software version, you may also need to install the release-key file.

Upload the software image file.

For the System platform component, upload to the /tmp folder on the system. For example: scp s42700x12_5_7.tar.gz root@10.0.0.1:/tmp/s42700x12_5_7.tar.gz

For other components, upload to the /tmp/pkgs/new/ folder on the system, keeping the file name and extension unchanged. For example: scp root@10.0.0.1:/tmp/pkgs/new/vcs-lang-es-es_8.1_amd64.tlp

Wait for the file upload to complete and then check the file size. Note that the default /tmp/tandberg-image.tar.gz file entry in /tmp will be 0 bytes.

When you are ready to start the upgrade, rename (or move) the file to the required filename of /tmp/tandberg-image.tar.gz (this will start the upgrade process).

For example: mv /tmp/s42700x12_5_7.tar.gz /tmp/tandberg-image.tar.gz

Enter the root password when prompted. The software installation begins automatically and you see " Software upgrade in progress " on the SSH/console.

Wait until the software has installed completely and you see " Upgrade complete! The new software will be used on the next reboot " .

We recommend that you reboot the system immediately, because any further configuration changes made before the reboot will be lost when the system restarts .

### Upgrading Firmware (Physical Appliances Only)

This section applies if Expressway is deployed on a physical appliance, and you need to upgrade the firmware for some reason.

Use the Cisco Host Upgrade Utility (HUU) to perform the upgrade. This is Cisco's dedicated tool for upgrading firmware components
                                 on a UCS C-Series server. Detailed instructions about  using the HUU are available in the latest Cisco Host Upgrade Utility User Guide on the Cisco UCS C-Series Rack Servers documentation page.

## Configuring Language Settings

The Language page ( Maintenance > Language ) controls which language is used for text displayed in the web user interface.

You can also get to the Language page by clicking on the Language link at the bottom of every page.

### Changing the Language

You can configure both the default language and the language to use on an individual browser:

Field

Description

Usage tips

System default language

The default language used on the web interface.

This applies to administrator and user (FindMe) sessions. You can select from the set of installed language packs.

This browser

The language used by the current browser on the current client computer. It can be set to use either the system default language
                                             or a specific alternative language.

This setting applies to the browser currently in use on the client computer. If you access the Expressway user interface using
                                             a different browser or a different computer, a different language setting may be in place.

### Installing Language Packs

You can install new language packs or install an updated version of an existing language pack.

Language packs are downloaded from the same area on cisco.com from where you obtain your Expressway software files. All available
                                 languages are contained in one language pack zip file. Download the appropriate language pack version that matches your software
                                 release.

After downloading the language pack, unzip the file to extract a set of .tlp files, one per supported language.

For the list of available languages, see the relevant release notes for your software version.

English (en_us) is installed by default and is always available.

You cannot create your own language packs. Language packs can be obtained only from Cisco.

If you upgrade to a later version of Expressway software you will see a "Language pack mismatch" alarm. You may need to install a later version of the associated language pack to ensure that all text is available in the
                                                   chosen language.

To install a .tlp language pack file:

Go to Maintenance > Language .

Click Browse and select the .tlp language pack you want to upload.

Click Install .

The selected language pack is then verified and uploaded. This may take several seconds.

Repeat steps 2 and 3 for any other languages you want to install.

### Removing Language Packs

Go to the Language page ( Maintenance > Language ).

From the list of installed language packs, select the language packs you want to remove.

Click Remove .

Click Yes when asked to confirm.

The selected language packs are then removed. This may take several seconds.

## Backing Up and Restoring Expressway Data

Use the Backup and restore page ( Maintenance > Backup and restore ) to create backup files of Expressway data and to restore the Expressway to a previous, saved configuration.

### When to Create a Backup

We recommend creating regular backups, and always in the following situations:

Before performing an upgrade.

Before performing a system restore.

In demonstration and test environments, if you want to be able to restore the Expressway to a known configuration.

### What Gets Backed Up

The data saved to a backup file includes:

Bootstrap key (from X8.11)

System configuration settings

Clustering configuration

Local authentication data (but not Active Directory credentials for remotely managed accounts):

User account and password details

Server security certificate and private key

Call detail records (if the CDR service on Expressway is enabled)

Log files are not included in backup files.

For detailed backup and restore procedures, see Creating a System Backup , and Restoring a Previous Backup .

### Clustered Systems

For more details about backing up and restoring peers in a cluster, see

Cluster Upgrades, Backup, and Restore .

## Creating a System Backup

### Before you Begin

Backup files are always encrypted (from X8.11). In particular because they include the bootstrap key, and authentication data
                                       and other sensitive information.

Backups can only be restored to a system that is running the same version of software from which the backup was made .

You can create a backup on one Expressway and restore it to a different Expressway. For example if the original system has
                                       failed. Before the restore, you must install the same option keys on the new system that were present on the old one.

If you try to restore a backup made on a different Expressway, you receive a warning message, but you will be allowed to continue.

(If you use FIPS140-2 cryptographic mode) You can't restore a backup made on a non-FIPS system, onto a system that's running
                                       in FIPS mode. You can restore a backup from a FIPS-enabled system onto a non-FIPS system.

Do not use backups to copy data between Expressways. If you do so, system-specific information will be duplicated (like IP
                                       addresses).

Because backup files contain sensitive information, you should not send them to Cisco in relation to technical support cases.
                                       Use snapshot and diagnostic files instead.

### Passwords

All backups must be password protected.

If you restore to a previous backup, and the administrator account password has changed since the backup was done, you must
                                       also provide the old account password when you first log in after the restore.

Active Directory credentials are not included in system backup files. If you use NTLM device authentication, you must provide the Active Directory password to
                                       rejoin the Active Directory domain after any restore.

For backup and restore purposes, emergency account passwords are handled the same as standard administrator account passwords.

### Process

Go to Maintenance > Backup and restore .

Enter an Encryption password to encrypt the backup file.

The password will be required in future if you ever want to restore the backup file.

Click Create system backup file .

Wait for the backup file to be created. This may take several minutes. Do not navigate away from this page while the file
                                          is being prepared.

When the backup is ready, you are prompted to save it. The default filename uses format: <software version>_<hardware serial number>_<date>_<time>_backup.tar.gz.enc . Or if you use Internet Explorer, the default extension is .tar.gz.gz . (These different filename extensions have no operational impact, and you can create and restore backups using any supported
                                          browser.)

Save the backup file to a secure location.

## Restoring a Previous Backup

### Before you Begin

When you restore an Expressway-E onto a CE1200 appliance from a CE1100 or earlier appliance backup, the CE1200 appliance may
                                             restore as Expressway-C. This issue occurs if the service setup wizard was used in the CE1100 or earlier appliance to change
                                             the type to Expressway-C and you skipped the wizard without completing the entire configuration. To avoid this issue, before
                                             you back up the appliance, run the service setup wizard, change the type to Expressway-E, and ensure that you complete the
                                             wizard.

You need the password for the backup file from which you intend to restore.

If you are restoring a backup file from a different Expressway, you need to apply the same set of license keys as exist on
                                       the system from which you intend to restore.

We recommend that you take the Expressway unit out of service before doing a restore.

The restore process involves doing a factory reset back to the original software version. Then upgrading to the same software version that was running when you took the backup .

If the backup is out of date (made on an earlier version than the version you want) these extra steps are needed after the
                                       restore:

Upgrade the software version to the required later version.

Manually redo any configuration changes made since the backup was taken.

(If you use FIPS140-2 cryptographic mode) You can't restore a backup made on a non-FIPS system, onto a system that's running
                                       in FIPS mode. You can restore a backup from a FIPS-enabled system onto a non-FIPS system.

You can't restore data to a Expressway while it's part of a cluster. You must first remove it from the cluster. For details,
                                       see Cluster Upgrades, Backup, and Restore .

### Passwords

Backups must be password protected.

If you restore to a previous backup, and the administrator account password has changed since the backup was done, you must
                                       also provide the old account password when you first log in after the restore.

Active Directory credentials are not included in system backup files. If you use NTLM device authentication, you must provide the Active Directory password to
                                       rejoin the Active Directory domain after any restore.

For backup and restore purposes, emergency account passwords are handled the same as standard administrator account passwords.

### Process

First do a factory reset, as described in Restoring the Default Configuration (Factory Reset). This removes your configuration data, and reverts the system back to its original state. The reset maintains
                                          your current software version if you've upgraded since the system was first set up.

Upgrade the system to the software version that was running when you made the backup.

For standalone systems, see Upgrade instructions .

For clustered systems, see the Expressway Cluster Creation and Maintenance Deployment Guide .

Now you can restore the system from the backup, as follows:

Go to Maintenance > Backup and restore .

In the Restore section, click Browse and navigate to the backup file that you want to restore.

In the Decryption password field, enter the password used to create the backup file.

Click Upload system backup file .

The Expressway checks the file and takes you to the Restore confirmation page.

If the backup file is invalid or the decryption password was entered incorrectly, an error message is displayed at the top
                                                         of the Backup and restore page.

The current software version and the number of calls and registrations is displayed.

Read the warning messages that appear, before you continue.

Click Continue with system restore to proceed with the restore.

This will restart the system, so make sure that no active calls exist.

When the system restarts, the Login page is displayed.

This step only applies if the backup file is out of date. That is, the software version was upgraded, or system configuration
                                          changes were made after the backup was done. In this case:

Upgrade the system again, this time to the required software version for the system.

Redo any configuration changes made after the backup (assuming you still need them on the restored system).

## Checking the Effect of Pattern

Patterns can be used when configuring:

Transforms to specify aliases to be transformed before any searches take place

Search rules to filter searches based on the alias being searched for, and to transform an alias before the search is sent to a zone

To use this tool:

Enter an Alias against which you want to test the transform.

In the Pattern section, enter the combination of Pattern type and Pattern behavior for the Pattern string being tested.

If you select a Pattern behavior of Replace , you also need to enter a Replace string .

If you select a Pattern behavior of Add prefix or Add suffix , you also need to enter an Additional text string to append/prepend to the Pattern string .

The Expressway has a set of predefined pattern matching variables that can be used to match against certain configuration elements.

Click Check pattern to test whether the alias matches the pattern.

The Result section shows whether the alias matched the pattern, and displays the resulting alias (including the effect of any transform
                                          if appropriate).

## Locating an Alias

The Locate tool ( Maintenance > Tools > Locate ) lets you test whether the Expressway can find an endpoint identified by the given alias, within the specified number of "hops" , without actually placing a call to that endpoint.

This tool is useful when diagnosing dial plan and network deployment issues.

Enter the Alias you want to locate.

Enter the Hop count for the search.

Select the Protocol used to initiate the search, either H.323 or SIP . The search may be interworked during the search process, but the Expressway always uses the native protocol first to search
                                       those target zones and policy services associated with search rules at the same priority, before searching those zones again
                                       using the alternative protocol.

Select the Source from which to simulate the search request. Choose from the Default Zone (an unknown remote system), the Default Subzone (a locally registered endpoint) or any other configured zone or subzone.

Select whether the request should be treated as Authenticated or not (search rules can be restricted so that they only apply to authenticated messages).

Optionally, you can enter a Source alias . Typically, this is only relevant if the routing process uses CPL that has rules dependent on the source alias. (If no value
                                       is specified a default alias of xcom-locate is used.)

Click Locate to start to search.

The status bar shows Searching... followed by Search completed . The results include the list of zones that were searched, any transforms and Call Policy that were applied, and if found,
                                          the zone in which the alias was located.

The locate process performs the search as though the Expressway received a call request from the selected Source zone . For more information, see the Call Routing Process section.

## Port Usage

The pages under the Maintenance > Tools > Port usage menu show, in table format, all the IP ports that have been configured on the Expressway.

The information shown on these pages is specific to that particular Expressway and varies depending on the Expressway's configuration,
                              the option keys that have been installed and the features that have been enabled.

The information can be sorted according to any of the columns on the page, so for example you can sort the list by IP port,
                              or by IP address.

Each page contains an Export to CSV option. This lets you save the information in a CSV (comma separated values) format file suitable for opening in a spreadsheet
                              application.

Note that IP ports cannot be configured separately for IPv4 and IPv6 addresses, nor for each of the two LAN interfaces. In
                              other words, after an IP port has been configured for a particular service, for example SIP UDP, this will apply to all IP
                              addresses of that service on the Expressway. Because the tables on these pages list all IP ports and all IP addresses, a single
                              IP port may appear on the list up to 4 times, depending on your Expressway configuration.

The port information is split into the following pages:

Local Inbound Ports

Local Outbound Ports

Remote Listening Ports

On Expressway-E you can also configure the specific listening ports used for firewall traversal via Configuration > Traversal > Ports .

See the Cisco Expressway IP Port Usage Configuration Guide , for your version, on the Cisco Expressway Series configuration guides page.

### Local Inbound Ports

The Local inbound ports page ( Maintenance > Tools > Port usage > Local inbound ports ) shows the listening IP ports on the Expressway that are used to receive inbound communications from other systems.

For each port listed on this page, if there is a firewall between the Expressway and the source of the inbound communications,
                                 your firewall must allow:

Inbound traffic to the IP port on the Expressway from the source of the inbound communications, and

Return traffic from that same Expressway IP port back out to the source of the inbound communication.

This firewall configuration is particularly important if this Expressway is a traversal client or traversal server, in order
                                             for Expressway firewall traversal to function correctly.

See the Cisco Expressway IP Port Usage Configuration Guide , for your version, on the Cisco Expressway Series configuration guides page.

### Local Outbound Ports

The Local outbound ports page ( Maintenance > Tools > Port usage > Local outbound ports ) shows the source IP ports on the Expressway that are used to send outbound communications to other systems.

For each port listed on this page, if there is a firewall between the Expressway and the destination of the outbound communications,
                                 your firewall must allow:

Outbound traffic out from the IP port on the Expressway to the destination of the outbound communications, and

Return traffic from that destination back to the same Expressway IP port.

This firewall configuration is particularly important if this Expressway is a traversal client or traversal server, in order
                                             for Expressway firewall traversal to function correctly.

See the Cisco Expressway IP Port Usage Configuration Guide , for your version, on the Cisco Expressway Series configuration guides page.

### Remote Listening Ports

The Remote listening ports page ( Maintenance > Tools > Port usage > Remote listening ports ) shows the destination IP addresses and IP ports of remote systems with which the Expressway communicates.

Your firewall must be configured to allow traffic originating from the local Expressway to the remote devices identified by
                                 the IP addresses and IP ports listed on this page.

There are other remote devices not listed here to which the Expressway will be sending media and signaling, but the ports
                                             on which these devices receive traffic from the Expressway is determined by the configuration of the destination device, so
                                             they cannot be listed here. If you have opened all the ports listed in the Local outbound ports page, the Expressway will be able to communicate with all remote devices. You only need to use the information on this page
                                             if you want to limit the IP ports opened on your firewall to these remote systems and ports.

See the Cisco Expressway IP Port Usage Configuration Guide , for your version, on the Cisco Expressway Series configuration guides page.

## Restarting, Rebooting, and Shutting Down

The Restart options page ( Maintenance > Restart options ) allows you to restart, reboot, or shut down the Expressway without having physical access to the hardware.

Do not restart, reboot or shut down the Expressway while the red ALM LED on the front of the unit is on. This indicates a
                                          hardware fault. Contact your Cisco customer support representative.

### Restarting

The restart function shuts down and restarts the Expressway application software, but not the operating system or hardware.
                              A restart takes approximately 3 minutes.

A restart is typically required in order for some configuration changes to take effect, or when the system is being added
                              to, or removed from, a cluster. In these cases a system alarm is raised and will remain in place until the system is restarted.

If the Expressway is part of a cluster and other peers in the cluster also require a restart, we recommend that you wait until
                              each peer has restarted before restarting the next peer.

### Rebooting

The reboot function shuts down and restarts the Expressway application software, operating system and hardware. A reboot takes
                              approximately 5 minutes.

Reboots are normally only required after software upgrades and are performed as part of the upgrade process. A reboot may
                              also be required when you are trying to resolve unexpected system errors.

### Shutting down

A shutdown is typically required if you want to unplug your unit, prior to maintenance or relocation for example. The system
                              must be shut down before it is unplugged. Avoid uncontrolled shutdowns, in particular the removal of power to the system during
                              normal operation.

### Effect on active calls

Any of these restart options will cause all active calls to be terminated. (If the Expressway is part of a cluster, only those
                              calls for which the Expressway is taking the signaling will be terminated.)

For this reason, the System status section displays the number of current calls so you can check these before you restart the system. If you do not restart
                              the system immediately, you should refresh this page before restarting to check the current status of calls.

If Mobile and remote access is enabled, the number of currently provisioned sessions is displayed (Expressway-C only).

### Restarting, rebooting or shutting down using the web interface

To restart the Expressway using the web interface:

Go to Maintenance > Restart options .

Check the number of calls currently in place.

Click Restart , Reboot , or Shutdown as appropriate and confirm the action.

Sometimes only one of these options, such as Restart for example, may be available. This typically occurs when you access the Restart options page after following a link in an alarm or a banner message.

Restart/reboot: the Restarting/Rebooting page appears, with an orange bar indicating progress.

After the system has successfully restarted or rebooted, you are automatically taken to the Login page.

Shutdown: the Shutting down page appears.

This page remains in place after the system has successfully shut down but any attempts to refresh the page or access the
                                          Expressway will be unsuccessful.

| Note | Maintenance mode is automatically disabled if the peer is restarted. |
|---|---|

| Caution | You will use root access to authorize your public key. Take care not to increase your security exposure or cause any unsupported
                                          configuration. We strongly discourage using root . |
|---|---|

| Step 1 | Use SSH to log in as root . |
|---|---|
| Step 2 | Enter mkdir /tandberg/.ssh to create .ssh directory if it is not already present. |
| Step 3 | Copy your public key to /tandberg/.ssh . |
| Step 4 | Append your public key to the authorized_keys file with cat /tandberg/.ssh/ id_rsa.pub >> /tandberg/.ssh/authorized_keys . Where id_rsa.pub is substituted with the name of your public key. Do not place your key anywhere else because the key could be lost on upgrade
                                          ( authorized_keys file does persist) |
| Step 5 | Log off and test SSH access using your own key If you cannot access the Expressway with your key, you may need to connect as root and restart the SSH daemon with /etc/init.d/sshd restart . |

| Step 1 | Upload the software image file. For the System platform component, upload to the /tmp folder on the system. For example: scp s42700x12_5_7.tar.gz root@10.0.0.1:/tmp/s42700x12_5_7.tar.gz For other components, upload to the /tmp/pkgs/new/ folder on the system, keeping the file name and extension unchanged. For example: scp root@10.0.0.1:/tmp/pkgs/new/vcs-lang-es-es_8.1_amd64.tlp |
|---|---|
| Step 2 | Wait for the file upload to complete and then check the file size. Note that the default /tmp/tandberg-image.tar.gz file entry in /tmp will be 0 bytes. |
| Step 3 | When you are ready to start the upgrade, rename (or move) the file to the required filename of /tmp/tandberg-image.tar.gz (this will start the upgrade process). For example: mv /tmp/s42700x12_5_7.tar.gz /tmp/tandberg-image.tar.gz |
| Step 4 | Enter the root password when prompted. The software installation begins automatically and you see " Software upgrade in progress " on the SSH/console. |
| Step 5 | Wait until the software has installed completely and you see " Upgrade complete! The new software will be used on the next reboot " . |
| Step 6 | We recommend that you reboot the system immediately, because any further configuration changes made before the reboot will be lost when the system restarts . |

|  | You can also get to the Language page by clicking on the Language link at the bottom of every page. |
|---|---|

| Field | Description | Usage tips |
|---|---|---|
| System default language | The default language used on the web interface. | This applies to administrator and user (FindMe) sessions. You can select from the set of installed language packs. |
| This browser | The language used by the current browser on the current client computer. It can be set to use either the system default language
                                             or a specific alternative language. | This setting applies to the browser currently in use on the client computer. If you access the Expressway user interface using
                                             a different browser or a different computer, a different language setting may be in place. |

| Note | English (en_us) is installed by default and is always available. You cannot create your own language packs. Language packs can be obtained only from Cisco. If you upgrade to a later version of Expressway software you will see a "Language pack mismatch" alarm. You may need to install a later version of the associated language pack to ensure that all text is available in the
                                                   chosen language. |
|---|---|

| Step 1 | Go to Maintenance > Language . |
|---|---|
| Step 2 | Click Browse and select the .tlp language pack you want to upload. |
| Step 3 | Click Install . The selected language pack is then verified and uploaded. This may take several seconds. |
| Step 4 | Repeat steps 2 and 3 for any other languages you want to install. |

| Step 1 | Go to the Language page ( Maintenance > Language ). |
|---|---|
| Step 2 | From the list of installed language packs, select the language packs you want to remove. |
| Step 3 | Click Remove . |
| Step 4 | Click Yes when asked to confirm. The selected language packs are then removed. This may take several seconds. |

| Step 1 | Go to Maintenance > Backup and restore . |
|---|---|
| Step 2 | Enter an Encryption password to encrypt the backup file. Caution The password will be required in future if you ever want to restore the backup file. | Caution | The password will be required in future if you ever want to restore the backup file. |
| Caution | The password will be required in future if you ever want to restore the backup file. |
| Step 3 | Click Create system backup file . |
| Step 4 | Wait for the backup file to be created. This may take several minutes. Do not navigate away from this page while the file
                                          is being prepared. |
| Step 5 | When the backup is ready, you are prompted to save it. The default filename uses format: <software version>_<hardware serial number>_<date>_<time>_backup.tar.gz.enc . Or if you use Internet Explorer, the default extension is .tar.gz.gz . (These different filename extensions have no operational impact, and you can create and restore backups using any supported
                                          browser.) |
| Step 6 | Save the backup file to a secure location. |

| Caution | The password will be required in future if you ever want to restore the backup file. |
|---|---|

| Caution | When you restore an Expressway-E onto a CE1200 appliance from a CE1100 or earlier appliance backup, the CE1200 appliance may
                                             restore as Expressway-C. This issue occurs if the service setup wizard was used in the CE1100 or earlier appliance to change
                                             the type to Expressway-C and you skipped the wizard without completing the entire configuration. To avoid this issue, before
                                             you back up the appliance, run the service setup wizard, change the type to Expressway-E, and ensure that you complete the
                                             wizard. |
|---|---|

| Step 1 | First do a factory reset, as described in Restoring the Default Configuration (Factory Reset). This removes your configuration data, and reverts the system back to its original state. The reset maintains
                                          your current software version if you've upgraded since the system was first set up. |
|---|---|
| Step 2 | Upgrade the system to the software version that was running when you made the backup. For standalone systems, see Upgrade instructions . For clustered systems, see the Expressway Cluster Creation and Maintenance Deployment Guide . |
| Step 3 | Now you can restore the system from the backup, as follows: Go to Maintenance > Backup and restore . In the Restore section, click Browse and navigate to the backup file that you want to restore. In the Decryption password field, enter the password used to create the backup file. Click Upload system backup file . The Expressway checks the file and takes you to the Restore confirmation page. If the backup file is invalid or the decryption password was entered incorrectly, an error message is displayed at the top
                                                         of the Backup and restore page. The current software version and the number of calls and registrations is displayed. Read the warning messages that appear, before you continue. Click Continue with system restore to proceed with the restore. This will restart the system, so make sure that no active calls exist. When the system restarts, the Login page is displayed. |
| Step 4 | This step only applies if the backup file is out of date. That is, the software version was upgraded, or system configuration
                                          changes were made after the backup was done. In this case: Upgrade the system again, this time to the required software version for the system. Redo any configuration changes made after the backup (assuming you still need them on the restored system). |

| Step 1 | Enter an Alias against which you want to test the transform. |
|---|---|
| Step 2 | In the Pattern section, enter the combination of Pattern type and Pattern behavior for the Pattern string being tested. If you select a Pattern behavior of Replace , you also need to enter a Replace string . If you select a Pattern behavior of Add prefix or Add suffix , you also need to enter an Additional text string to append/prepend to the Pattern string . The Expressway has a set of predefined pattern matching variables that can be used to match against certain configuration elements. |
| Step 3 | Click Check pattern to test whether the alias matches the pattern. The Result section shows whether the alias matched the pattern, and displays the resulting alias (including the effect of any transform
                                          if appropriate). |

| Step 1 | Enter the Alias you want to locate. |
|---|---|
| Step 2 | Enter the Hop count for the search. |
| Step 3 | Select the Protocol used to initiate the search, either H.323 or SIP . The search may be interworked during the search process, but the Expressway always uses the native protocol first to search
                                       those target zones and policy services associated with search rules at the same priority, before searching those zones again
                                       using the alternative protocol. |
| Step 4 | Select the Source from which to simulate the search request. Choose from the Default Zone (an unknown remote system), the Default Subzone (a locally registered endpoint) or any other configured zone or subzone. |
| Step 5 | Select whether the request should be treated as Authenticated or not (search rules can be restricted so that they only apply to authenticated messages). |
| Step 6 | Optionally, you can enter a Source alias . Typically, this is only relevant if the routing process uses CPL that has rules dependent on the source alias. (If no value
                                       is specified a default alias of xcom-locate is used.) |
| Step 7 | Click Locate to start to search. The status bar shows Searching... followed by Search completed . The results include the list of zones that were searched, any transforms and Call Policy that were applied, and if found,
                                          the zone in which the alias was located. |

| Note | This firewall configuration is particularly important if this Expressway is a traversal client or traversal server, in order
                                             for Expressway firewall traversal to function correctly. |
|---|---|

| Note | This firewall configuration is particularly important if this Expressway is a traversal client or traversal server, in order
                                             for Expressway firewall traversal to function correctly. |
|---|---|

| Note | There are other remote devices not listed here to which the Expressway will be sending media and signaling, but the ports
                                             on which these devices receive traffic from the Expressway is determined by the configuration of the destination device, so
                                             they cannot be listed here. If you have opened all the ports listed in the Local outbound ports page, the Expressway will be able to communicate with all remote devices. You only need to use the information on this page
                                             if you want to limit the IP ports opened on your firewall to these remote systems and ports. |
|---|---|

| Caution | Do not restart, reboot or shut down the Expressway while the red ALM LED on the front of the unit is on. This indicates a
                                          hardware fault. Contact your Cisco customer support representative. |
|---|---|