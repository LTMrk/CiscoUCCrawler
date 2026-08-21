---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1501-installation-guide-cfin-b-1-4cc4499648
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1501/installation/guide/cfin_b_1501_cisco-installation-and-upgrade-guide-15_0/cfin_m_1501_upgrade.html
retrieved_at: 2026-08-21T15:53:00.952474+00:00
---

Cisco Finesse Installation and Upgrade Guide, Release 15.0(1)

# Cisco Finesse Installation and Upgrade Guide, Release 15.0(1)

Updated: April 30, 2025

Chapter: Upgrade

## Chapter: Upgrade

# Upgrade

## Supported Upgrade Paths

The following table lists the supported upgrade paths to Cisco Finesse Release 15.0(1):

Current Version

Upgrade Path

Release 12.5(2), 12.6(1), or 12.6(2)

Upgrade to Release 15.0(1)

To upgrade from Cisco Finesse 12.6(1) to Cisco Finesse 15.0(1), you must download and install ucos.keymanagement.v02.cop.sgn file from Software Download .

To upgrade from releases prior to the supported versions (current version) listed above, you must first upgrade to one of
                                             those current versions before proceeding with the upgrade to version 15.0(1).

## Aligned Partitions Support

Cisco Finesse supports aligned partitions with a fresh installation.

If you perform an upgrade from a previous release, the platform detects the unaligned partitions and displays the following
                              error:

ERROR-UNSUPPORTED: Partitions unaligned

You can run Cisco Finesse with the unaligned partitions, as there’s no functional impact to Finesse. However, you can’t experience
                              the benefits of aligned partitions unless you perform a fresh installation.

To support aligned partitions, do the following:

Upgrade Cisco Finesse.

Perform a backup on the primary Finesse server using the Disaster Recovery System (DRS) application. To access the DRS application,
                                    direct your browser to https:// FQDN of Finesse server :8443/drf.

Perform a fresh installation of Cisco Finesse.

Access the DRS application and perform a restore from your backup.

For more information about DRS backup and restore, see the Cisco Finesse Administration Guide and the detailed online help provided with the DRS application.

## Perform Upgrade

You must upgrade the primary Finesse node first and then the secondary Finesse node. Both the primary and secondary Finesse
                              nodes must be running the same version before the upgrade.

### Before you begin

Upgrade Finesse during off-peak hours or during a maintenance window to avoid service interruptions.

Perform a DRS backup on the primary Finesse server. To access the DRS application, direct your browser to https:// FQDN of Finesse server :8443/drf. For more information, see the online help that is provided with the DRS application.

For small deployments, allocate a minimum of 10 GB RAM for virtual machine before upgrading to Cisco Finesse Release 15.0
                                    (1) SU1. This allocation prevents out-of-memory (OOM) errors and ensures optimal performance after the upgrade.

For more information on virtualization details, see Virtualization for Cisco Finesse .

For large deployments, allocate extra vRAM and other resources to avoid impacting the performance of the upgraded version.
                                    For more information on the virtualization details, see Virtualization for Cisco Finesse .

Place the Cisco Finesse ISO file on an FTP or SFTP server that you can access from your Finesse system or burn the ISO file
                                    to DVD.

The Finesse desktop has a new look due to the Multi-Tab gadget-based layout. To save the existing layout, sign in to the cfadmin
                                    (https:// FQDN of Finesse server:8445 /cfadmin) and copy the custom layout from Desktop Layout > Manage Desktop Layout . Save the custom layout as a text file in your local file system.

Icons (both custom and in-built) that appear on the Finesse desktop and the left navigation bar are now customizable. Finesse
                                    specific tabs with no change in labels automatically display their respective in-built icons. Tabs that are created or modified
                                    have a default icon. You can customize these icons in the desktop layout through the administration portal of Finesse. You
                                    can upload custom icons into the Finesse third-party gadget. For more information,  see Default Layout XML section in the Cisco Finesse Administration Guide .

For upgraded layouts, Notification Center, Search Gadgets, and sample configurations for customizing desktop properties don’t appear by default. The administrator must copy the XML
                                    from the View Default Layout and add to the respective custom layouts. For more information, see the Cisco Finesse Administration Guide and Cisco Finesse Agent and Supervisor Desktop User Guide .

Gadgets within commented sections aren’t modified automatically. After the upgrade, if you want to use the gadgets that are
                                                in the commented sections, you must manually modify the name, format, and path of the gadgets.

The maxRow is changed from being a query parameter to an attribute. During an upgrade, it is removed from the URL of the Team Performance
                                    gadget and is added as an attribute. After the upgrade, the height of the rows in the Team Performance gadget remains the
                                    same.

In upgrade scenarios, by default, the first two call variables are displayed in the agent call pop over and in the supervisor
                                    active call details. You can modify the configuration of the pop over variables to improve the agent and supervisor experience.

After upgrades, manually remove the Context Service gadgets from the Desktop Layout and Team Desktop Layout.

If you upgrade Cisco Finesse before CCE, the older CCE version does not support separate Administrative Workstation Database
                                    (AWDB) ports. To ensure compatibility, perform the following:

In Cisco Finesse Administrative portal, set the same port number for both the Primary and Secondary AWDB Port.

After you upgrade CCE, update the Secondary AWDB Port to a different value as needed.

If you upgrade CCE before Cisco Finesse, the older Cisco Finesse version supports only a single port configuration. To ensure
                                    compatibility, perform the following:

In CCE, set the same port for both the primary and secondary AWDB connections. Cisco Finesse uses the single configured port
                                          for both AWDB connections until you upgrade Cisco Finesse.

After you upgrade Cisco Finesse, configure separate ports in Cisco Finesse Administrative portal to match the CCE configuration.

After the successful upgrade, the CAs that are unapproved by Cisco are removed from the platform trust store. However, you
                                          can add them back, if necessary.

For information about the list of CAs that we support, see the Cisco Trusted External Root Bundle .

For information about adding a certificate, see Insert a New Tomcat-trust Certificate section in the CUCM Certificate Management and Change Notification .

Step 1

SSH to your Finesse system and sign-in with the platform administration account.

Step 2

Access the CLI and run the utils system upgrade initiate command.

Step 3

Follow the instructions that are provided by the utils system upgrade initiate command.

If you choose to install from a remote source (FTP or SFTP server), provide the location and credentials for the remote file
                                          system.

If you choose to install from the local CD/DVD drive, ensure that the drive is connected to the Finesse virtual machine (VM)
                                          as follows:

Right-click the VM and choose Edit Settings .

Click the Hardware tab.

In the left pane, select CD/DVD Drive .

In the right pane, under Device Status, check the Connected and Connect at power on check boxes.

Under Device Type, select Datastore ISO File .

Click Browse and navigate to the Finesse ISO file.

Click OK .

Finesse also prompts you for SMTP Server information, but it’s not mandatory. If you don’t have an SMTP Server, you can skip
                                          the SMTP prompt.

Step 4

At the Automatically switch versions if the upgrade is successful prompt, type yes . The upgrade isn’t active until a switch version is performed.

Once the switch version is complete, the system reboots.

Step 5

At the Start installation (yes/no) prompt, type yes to start the  upgrade.

Step 6

If you’re installing from the local CD/DVD drive, when the upgrade enters the BIOS screen, on the Boot tab, move CD-ROM Drive
                                       to the top. Save your settings and exit.

Step 7

After the upgrade is complete, disconnect the CD/DVD drive.

Right-click the VM and choose Edit Settings .

Click the Hardware tab.

Select CD/DVD Drive 1 .

Clear the Connected and Connect at power on check boxes.

Click OK .

Step 8

Perform the preceding steps on the secondary Finesse server.

Step 9

Sign in to the Finesse desktop to verify that the upgrade was successful (https:// FQDN of Finesse server:8445 /desktop).

After Finesse restarts, wait approximately 20 minutes before you attempt to sign in to the desktop. Finesse services may take
                                                      a few minutes to reach the STARTED state.

### What to do next

After the system upgrade, ensure that all agents, supervisors, and administrators clear their browser cache.

If you had a modified desktop layout before the upgrade, perform the following steps to ensure you obtain the latest changes:

Sign in to the Finesse administration console and click the Desktop Layout tab.

On the Manage Desktop Layout gadget, click Restore Default Layout .

Click Save .

Using the text file of the desktop layout that you saved before the upgrade as a reference, modify the layout to include the
                                          changes that you made to the previous layout.

Click Save to save your changes.

In the Manage Reasons (Not Ready) gadget, check for Not Ready reason codes with code values that are not unique. Edit any
                                    that you find to give them unique values.

In the Manage Reasons (Sign Out) gadget, check for Sign Out reason codes with code values that aren’t unique. Edit any that
                                    you find to give them unique values.

Reset the third-party account password as it is a Unix user account. Use the utils reset_3rdpartygadget_password command to reset the third-party account password. You may reset to the previously configured password or change to a new
                                    password.

The sample configurations for customizing manage digital channel properties do not appear by default. For the gadget to appear
                                    in the Agent Desktop, the administrator must copy the XML code from the View Default Layout, add it to the respective custom
                                    layouts, and uncomment the tab. For more information, see the Add Manage Digital Channels gadget section in the Cisco Finesse Administration Guide .

Export the Finesse Tomcat certificates and import them to CTI Gateway (CG) and Peripheral Gateway (PG) systems. You must upload
                                    both ECDSA and RSA certificates. For more information, refer to the Add Certificate for HTTPS Gadget section in the Cisco Finesse Administration Guide .

## Perform Rollback

If a problem occurs with the upgrade, you can roll back to the earlier release.

Step 1

Perform a switch-version on the primary node.

Access the CLI and enter the command utils system switch-version .

Enter yes to confirm.

The system attempts to switch back to the original version and reboots if the switch is successful.

Step 2

Repeat Step 1 on the secondary node.

Step 3

1 hour after the switch version is complete, use the following command on both nodes to confirm that the replication is successful: utils dbreplication runtimestate .

The replication is successful if the output shows a replication status of 2.

If the replication is unsuccessful,
                                                      run the following database replication commands on the primary node:

utils dbreplication stop
                                                         all

utils dbreplication reset
                                                         all

After you enter these commands, wait again for 1 hour (or more depending on the volume of data) before again using the utils dbreplication runtimestate command to confirm the  replication is successful.

### Customers Also Viewed

- Understand UCCX Finesse Architecture Deep Dive

| Current Version | Upgrade Path |
|---|---|
| Release 12.5(2), 12.6(1), or 12.6(2) | Upgrade to Release 15.0(1) |

| Note | To upgrade from Cisco Finesse 12.6(1) to Cisco Finesse 15.0(1), you must download and install ucos.keymanagement.v02.cop.sgn file from Software Download . To upgrade from releases prior to the supported versions (current version) listed above, you must first upgrade to one of
                                             those current versions before proceeding with the upgrade to version 15.0(1). |
|---|---|

| Note | Gadgets within commented sections aren’t modified automatically. After the upgrade, if you want to use the gadgets that are
                                                in the commented sections, you must manually modify the name, format, and path of the gadgets. |
|---|---|

| Note | After the successful upgrade, the CAs that are unapproved by Cisco are removed from the platform trust store. However, you
                                          can add them back, if necessary. For information about the list of CAs that we support, see the Cisco Trusted External Root Bundle . For information about adding a certificate, see Insert a New Tomcat-trust Certificate section in the CUCM Certificate Management and Change Notification . |
|---|---|

| Step 1 | SSH to your Finesse system and sign-in with the platform administration account. |
|---|---|
| Step 2 | Access the CLI and run the utils system upgrade initiate command. |
| Step 3 | Follow the instructions that are provided by the utils system upgrade initiate command. If you choose to install from a remote source (FTP or SFTP server), provide the location and credentials for the remote file
                                          system. If you choose to install from the local CD/DVD drive, ensure that the drive is connected to the Finesse virtual machine (VM)
                                          as follows: Right-click the VM and choose Edit Settings . Click the Hardware tab. In the left pane, select CD/DVD Drive . In the right pane, under Device Status, check the Connected and Connect at power on check boxes. Under Device Type, select Datastore ISO File . Click Browse and navigate to the Finesse ISO file. Click OK . Finesse also prompts you for SMTP Server information, but it’s not mandatory. If you don’t have an SMTP Server, you can skip
                                          the SMTP prompt. |
| Step 4 | At the Automatically switch versions if the upgrade is successful prompt, type yes . The upgrade isn’t active until a switch version is performed. Note Once the switch version is complete, the system reboots. | Note | Once the switch version is complete, the system reboots. |
| Note | Once the switch version is complete, the system reboots. |
| Step 5 | At the Start installation (yes/no) prompt, type yes to start the  upgrade. |
| Step 6 | If you’re installing from the local CD/DVD drive, when the upgrade enters the BIOS screen, on the Boot tab, move CD-ROM Drive
                                       to the top. Save your settings and exit. |
| Step 7 | After the upgrade is complete, disconnect the CD/DVD drive. Right-click the VM and choose Edit Settings . Click the Hardware tab. Select CD/DVD Drive 1 . Clear the Connected and Connect at power on check boxes. Click OK . |
| Step 8 | Perform the preceding steps on the secondary Finesse server. |
| Step 9 | Sign in to the Finesse desktop to verify that the upgrade was successful (https:// FQDN of Finesse server:8445 /desktop). Note After Finesse restarts, wait approximately 20 minutes before you attempt to sign in to the desktop. Finesse services may take
                                                      a few minutes to reach the STARTED state. | Note | After Finesse restarts, wait approximately 20 minutes before you attempt to sign in to the desktop. Finesse services may take
                                                      a few minutes to reach the STARTED state. |
| Note | After Finesse restarts, wait approximately 20 minutes before you attempt to sign in to the desktop. Finesse services may take
                                                      a few minutes to reach the STARTED state. |

| Note | Once the switch version is complete, the system reboots. |
|---|---|

| Note | After Finesse restarts, wait approximately 20 minutes before you attempt to sign in to the desktop. Finesse services may take
                                                      a few minutes to reach the STARTED state. |
|---|---|

| Step 1 | Perform a switch-version on the primary node. Access the CLI and enter the command utils system switch-version . Enter yes to confirm. The system attempts to switch back to the original version and reboots if the switch is successful. |
|---|---|
| Step 2 | Repeat Step 1 on the secondary node. |
| Step 3 | 1 hour after the switch version is complete, use the following command on both nodes to confirm that the replication is successful: utils dbreplication runtimestate . The replication is successful if the output shows a replication status of 2. Note If the replication is unsuccessful,
                                                      run the following database replication commands on the primary node: utils dbreplication stop
                                                         all utils dbreplication reset
                                                         all After you enter these commands, wait again for 1 hour (or more depending on the volume of data) before again using the utils dbreplication runtimestate command to confirm the  replication is successful. | Note | If the replication is unsuccessful,
                                                      run the following database replication commands on the primary node: utils dbreplication stop
                                                         all utils dbreplication reset
                                                         all After you enter these commands, wait again for 1 hour (or more depending on the volume of data) before again using the utils dbreplication runtimestate command to confirm the  replication is successful. |
| Note | If the replication is unsuccessful,
                                                      run the following database replication commands on the primary node: utils dbreplication stop
                                                         all utils dbreplication reset
                                                         all After you enter these commands, wait again for 1 hour (or more depending on the volume of data) before again using the utils dbreplication runtimestate command to confirm the  replication is successful. |

| Note | If the replication is unsuccessful,
                                                      run the following database replication commands on the primary node: utils dbreplication stop
                                                         all utils dbreplication reset
                                                         all After you enter these commands, wait again for 1 hour (or more depending on the volume of data) before again using the utils dbreplication runtimestate command to confirm the  replication is successful. |
|---|---|