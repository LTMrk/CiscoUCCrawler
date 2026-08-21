---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su6-admingd-cucm-b-administration-guide-1251su6-cucm-b-test-a93daffcf9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU6/adminGd/cucm_b_administration-guide-1251su6/cucm_b_test-adminguide_chapter_0110.html
retrieved_at: 2026-08-21T08:37:15.823675+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6 and 12.5(1)SU7

# Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6 and 12.5(1)SU7

Updated: April 8, 2025

Chapter: Manage Device Firmware

## Chapter: Manage Device Firmware

# Manage Device Firmware

## Device Firmware
                        	 Updates Overview

Device loads are the software and firmware for devices such as IP phones, telepresence systems, and others that are provisioned
                              by and register to Cisco Unified Communications Manager . During installation or upgrade, Cisco Unified Communications Manager includes the latest loads available based on when the version of Cisco Unified Communications Manager was released. Cisco regularly releases updated firmware to introduce new features and software fixes and you may wish to
                              update your phones to a newer load without waiting for a Cisco Unified Communications Manager upgrade that includes that load.

Before endpoints can upgrade to a new version of software, the files required by the new load must be made available for download
                              at a location the endpoints have access to. The most common location is the Cisco UCM node with the Cisco TFTP service activated,
                              called the "TFTP server" . Some phones also support using an alternate download location, called a "load server" .

If you want to get a list, view, or download files that already in the tftp directory on any server you can use the CLI command
                              file list tftp to see the files in the TFTP directory, file view tftp to view a file, and file get tftp to get a copy of a
                              file in the TFTP directory. For more information, see the Command Line Interface Reference Guide for Cisco Unified Communications Solutions . You may also use a web browser to download any TFTP file by going to the URL "http://<tftp_server>:6970/<filename>" .

Tip

You can apply a new load to a single device before configuring it as a systemwide default. This method is useful for testing
                                          purposes. Remember, however, that all other devices of that type use the old load until you update the systemwide defaults
                                          with the new load.

## Install a Device Pack or Individual Firmware

Install a device package to introduce new phone types and
                              upgrade the firmware for multiple phone models.

Individual firmware for existing devices can be installed or upgraded with the following options: Cisco Options Package (COP)
                                    files—The COP file contains the firmware files and the database updates so when installed on Publisher, it updates the default
                                    firmware apart from installing the firmware files.

Firmware files only—It is supplied in a zip file, contains individual device firmware files that you must manually extract
                                    and upload to the appropriate directory on the TFTP servers.

After you have successfully installed the firmware as mentioned in step 6, the phone device default for the phone model is
                                          updated to the latest version. If you are not prepared to upgrade phones at this time, we recommend that you adjust this value
                                          back to the previous firmware load that is currently running on the phones and readjust per your business needs. Alternatively,
                                          disable the TFTP service temporarily during device pack installation and restart the service after you are ready to upgrade
                                          phones.

If phones experience a network or call manager disconnect after a device pack install and the device default firmware is a
                                          later version, they restart and try to obtain the latest firmware before a TFTP restart.

Step 1

From Cisco
                                       			 Unified OS Administration, choose Software
                                             				  Upgrades > Install/Upgrade .

Step 2

Fill in the
                                       			 applicable values in the Software Location section and click Next .

Step 3

In the Available Software drop-down list, select the device
                                       			 package file and click Next .

Step 4

Verify that
                                       			 the MD5 value is correct, and then click Next .

Step 5

In the warning
                                       			 box, verify that you selected the correct firmware, and then click Install .

Step 6

Check that you received a success message.

Step 7

Restart the Cisco TFTP service on all nodes where the service is running.

Step 8

Reset the
                                       			 affected devices to upgrade the devices to the new load.

Step 9

From Cisco
                                       			 Unified CM Administration, choose Device > Device
                                             				  Settings > Device Defaults and manually change
                                       			 the name of the load file (for specific devices) to the new load.

Step 10

Click Save , and then reset the devices.

Step 11

Restart the Cisco Tomcat service on all cluster nodes.

Step 12

Do one of the following:

- If you are running 11.5(1)SU4 or lower, 12.0(1) or 12.0(1)SU1, reboot the cluster.

- If you are running an 11.5(x) release at 11.5(1)SU5 or higher, or any release higher at 12.0(1)SU2 or higher, reboot the Cisco CallManager service on the publisher node. However, if you are running the Cisco CallManager service on subscriber nodes only, you can skip this task.

### Potential Issues with Firmware Installs

Here are some potential issues that you may run across after installing a device pack:

Issue

Cause/Resolution

New devices won't register

This could occur due from a device type mismatch. This can be
                                             caused by:

The device was added in the Phone Configuration window using the
                                                   wrong device type. For example, Cisco DX80 was selected as the
                                                   phone type instead of Cisco TelePresence DX80. Reconfigure the
                                                   device with the correct device type.

The Cisco CallManager service
                                                   doesn't know about the new device type. In this case, restart the Cisco CallManager service on the publisher
                                                   node.

Endpoints aren't upgrading to the new firmware

The device pack wasn't installed on the TFTP server. As a result, the firmware isn't available for download by the phones.

The Cisco TFTP service wasn't restarted after the install so the service doesn't know about the new files. Make sure to install the device
                                                   pack on the TFTP server.

Phone Configuration window in Cisco Unified CM Administration shows broken links where the icon image should be for a new
                                             device type

Restart the Cisco Tomcat service on all nodes from the CLI.

## Remove Unused
                        	 Firmware from the System

The Device
                                 			 Load Management window allows you to delete unused firmware (device
                              		  loads) and associated files from the system to increase disk space. For
                              		  example, you can delete unused loads before an upgrade to prevent upgrade
                              		  failures due to insufficient disk space. Some firmware files may have dependent
                              		  files that are not listed in the Device
                                 			 Load Management window. When you delete a firmware, the dependent
                              		  files are also deleted. However, the dependent files are not deleted if they
                              		  are associated with additional firmware.

You must delete
                                          			 unused firmware separately for each server in the cluster.

### Before you begin

Caution

Before you delete unused firmware, ensure that you are deleting the right loads. The deleted loads cannot be restored without
                                          performing a DRS restore of the entire cluster. We recommend that you take a backup before deleting the firmware.

Ensure that you do not delete files for devices that use multiple loads of files. For example, certain CE endpoints use multiple
                                          loads. However, only one load is referenced as In Use in the Device Load Management window.

Step 1

From Cisco
                                       			 Unified OS Administration, choose Software
                                             				  Upgrades > Device Load Management .

Step 2

Specify the
                                       			 search criteria and click Find .

Step 3

Select the
                                       			 device load that you want to delete. You can select multiple loads if required.

Step 4

Click Delete
                                          				Selected Loads .

Step 5

Click OK .

## Set up Default
                        	 Firmware for a Phone Model

Use this procedure to set the default firmware load for a specific
                              		  phone model. When a new phone registers, Cisco Unified Communications Manager tries to send
                              		  the default firmware to the phone, unless the phone configuration specifies has
                              		  an overriding firmware load specified in the Phone Configuration window.

For an individual phone, the setting of the Phone Load Name field in the Phone Configuration window overrides the
                                          			 default firmware load for that particular phone.

### Before you begin

Make sure that the firmware is loaded onto the TFTP server.

Step 1

In Cisco Unified CM
                                       			 Administration, choose Device > Device
                                             				  Settings > Device Defaults .

Step 2

Under Device Type , locate the phone models for which
                                       			 you want to assign the default firmware.

Step 3

In the accompanying Load Information field, enter the firmware
                                       			 load.

Step 4

(Optional) Enter the default Device Pool and default Phone Template for that phone model.

Step 5

Click Save .

## Set the Firmware
                        	 Load for a Phone

Use this procedure to assign a firmware load for a specific phone. You
                              		  may want to do this if you want to use a different firmware load than the
                              		  default that is specified in the Device Defaults Configuration window.

If you wish to assign a version for many phones you can use the
                                             				Bulk Administration Tool to configure the Phone Load Name field using a CSV file or
                                             				query. For details, see the Bulk Administration Guide for Cisco Unified Communications
                                                				  Manager .

Step 1

In Cisco Unified CM
                                       			 Administration, choose Device > Phone .

Step 2

Click Find and select an individual phone.

Step 3

In the Phone Load Name field, enter the name of the
                                       			 firmware. For this phone, the firmware load specified here overrides the
                                       			 default firmware load that is specified in the Device Defaults Configuration window.

Step 4

Complete any remaining fields in the Phone Configuration window. For help with the
                                       			 fields and their settings, see the online help.

Step 5

Click Save .

Step 6

Click Apply Config to push the changed fields to the
                                       			 phone.

## Using a Load
                        	 Server

If you want phones to download firmware updates from a server that is
                              		  not the TFTP server you may configure a "load server" on the phone’s Phone Configuration page. A load server may be
                              		  another Cisco Unified Communications Manager or a
                              		  third-party server. A third-party server must be capable of providing any files
                              		  the phone requests through HTTP on TCP Port 6970 (preferred) or the UDP-based
                              		  TFTP protocol. Some phone models such as the DX family Cisco TelePresence
                              		  devices only support HTTP for firmware updates.

If you wish to assign a load server for many phones you can use the
                                          			 Bulk Administration Tool to configure the Load Server field using a CSV file or query.
                                          			 For details, see the Bulk Administration Guide for Cisco Unified Communications
                                             				Manager .

Step 1

In Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find and select an individual phone.

Step 3

In the Load Server field, enter the IP Address or
                                       			 hostname of the alternate server.

Step 4

Complete any remaining fields in the Phone Configuration window. For help with the
                                       			 fields and their settings, see the online help.

Step 5

Click Save .

Step 6

Click Apply Config to push the changed fields to the
                                       			 phone.

## Find Devices with Non-default Firmware Loads

The Firmware Load Information window in Unified Communications Manager enables you to quickly locate devices that are not using the default firmware load for their device type.

Each device can have an individually assigned firmware load that overrides the default.

Use the following procedure to locate devices that are not using the default firmware load.

Step 1

Choose Device > Device Settings > Firmware Load Information .

The page updates to display a list of device types that require firmware loads. For each device type, the Devices Not Using
                                          Default Load column links to configuration settings for any devices that use a non-default load.

Step 2

To view a list of devices of a particular device type that are using a non-default device load, click the entry for that device
                                       type in the Devices Not Using Default Load column.

The window that opens lists the devices of a particular device type that are not running the default firmware load.

| Tip | You can apply a new load to a single device before configuring it as a systemwide default. This method is useful for testing
                                          purposes. Remember, however, that all other devices of that type use the old load until you update the systemwide defaults
                                          with the new load. |
|---|---|

| Note | Refer to the README file for installation instructions that are specific to the COP or Firmware files package. |
|---|---|

| Note | After you have successfully installed the firmware as mentioned in step 6, the phone device default for the phone model is
                                          updated to the latest version. If you are not prepared to upgrade phones at this time, we recommend that you adjust this value
                                          back to the previous firmware load that is currently running on the phones and readjust per your business needs. Alternatively,
                                          disable the TFTP service temporarily during device pack installation and restart the service after you are ready to upgrade
                                          phones. If phones experience a network or call manager disconnect after a device pack install and the device default firmware is a
                                          later version, they restart and try to obtain the latest firmware before a TFTP restart. |
|---|---|

| Step 1 | From Cisco
                                       			 Unified OS Administration, choose Software
                                             				  Upgrades > Install/Upgrade . |
|---|---|
| Step 2 | Fill in the
                                       			 applicable values in the Software Location section and click Next . |
| Step 3 | In the Available Software drop-down list, select the device
                                       			 package file and click Next . |
| Step 4 | Verify that
                                       			 the MD5 value is correct, and then click Next . |
| Step 5 | In the warning
                                       			 box, verify that you selected the correct firmware, and then click Install . |
| Step 6 | Check that you received a success message. Note Skip to Step 8 if you are rebooting the cluster. | Note | Skip to Step 8 if you are rebooting the cluster. |
| Note | Skip to Step 8 if you are rebooting the cluster. |
| Step 7 | Restart the Cisco TFTP service on all nodes where the service is running. |
| Step 8 | Reset the
                                       			 affected devices to upgrade the devices to the new load. |
| Step 9 | From Cisco
                                       			 Unified CM Administration, choose Device > Device
                                             				  Settings > Device Defaults and manually change
                                       			 the name of the load file (for specific devices) to the new load. |
| Step 10 | Click Save , and then reset the devices. |
| Step 11 | Restart the Cisco Tomcat service on all cluster nodes. |
| Step 12 | Do one of the following: If you are running 11.5(1)SU4 or lower, 12.0(1) or 12.0(1)SU1, reboot the cluster. If you are running an 11.5(x) release at 11.5(1)SU5 or higher, or any release higher at 12.0(1)SU2 or higher, reboot the Cisco CallManager service on the publisher node. However, if you are running the Cisco CallManager service on subscriber nodes only, you can skip this task. |

| Note | Skip to Step 8 if you are rebooting the cluster. |
|---|---|

| Issue | Cause/Resolution |
|---|---|
| New devices won't register | This could occur due from a device type mismatch. This can be
                                             caused by: The device was added in the Phone Configuration window using the
                                                   wrong device type. For example, Cisco DX80 was selected as the
                                                   phone type instead of Cisco TelePresence DX80. Reconfigure the
                                                   device with the correct device type. The Cisco CallManager service
                                                   doesn't know about the new device type. In this case, restart the Cisco CallManager service on the publisher
                                                   node. |
| Endpoints aren't upgrading to the new firmware | Possible reasons: The device pack wasn't installed on the TFTP server. As a result, the firmware isn't available for download by the phones. The Cisco TFTP service wasn't restarted after the install so the service doesn't know about the new files. Make sure to install the device
                                                   pack on the TFTP server. |
| Phone Configuration window in Cisco Unified CM Administration shows broken links where the icon image should be for a new
                                             device type | Restart the Cisco Tomcat service on all nodes from the CLI. |

| Note | You must delete
                                          			 unused firmware separately for each server in the cluster. |
|---|---|

| Caution | Before you delete unused firmware, ensure that you are deleting the right loads. The deleted loads cannot be restored without
                                          performing a DRS restore of the entire cluster. We recommend that you take a backup before deleting the firmware. Ensure that you do not delete files for devices that use multiple loads of files. For example, certain CE endpoints use multiple
                                          loads. However, only one load is referenced as In Use in the Device Load Management window. |
|---|---|

| Step 1 | From Cisco
                                       			 Unified OS Administration, choose Software
                                             				  Upgrades > Device Load Management . |
|---|---|
| Step 2 | Specify the
                                       			 search criteria and click Find . |
| Step 3 | Select the
                                       			 device load that you want to delete. You can select multiple loads if required. |
| Step 4 | Click Delete
                                          				Selected Loads . |
| Step 5 | Click OK . |

| Note | For an individual phone, the setting of the Phone Load Name field in the Phone Configuration window overrides the
                                          			 default firmware load for that particular phone. |
|---|---|

| Step 1 | In Cisco Unified CM
                                       			 Administration, choose Device > Device
                                             				  Settings > Device Defaults . The Device Defaults Configuration window appears
                                       			 displaying the default firmware loads for the various phone models that Cisco Unified Communications Manager supports. The
                                       			 firmware appears in the Load Information column. |
|---|---|
| Step 2 | Under Device Type , locate the phone models for which
                                       			 you want to assign the default firmware. |
| Step 3 | In the accompanying Load Information field, enter the firmware
                                       			 load. |
| Step 4 | (Optional) Enter the default Device Pool and default Phone Template for that phone model. |
| Step 5 | Click Save . |

| Note | If you wish to assign a version for many phones you can use the
                                             				Bulk Administration Tool to configure the Phone Load Name field using a CSV file or
                                             				query. For details, see the Bulk Administration Guide for Cisco Unified Communications
                                                				  Manager . |
|---|---|

| Step 1 | In Cisco Unified CM
                                       			 Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select an individual phone. |
| Step 3 | In the Phone Load Name field, enter the name of the
                                       			 firmware. For this phone, the firmware load specified here overrides the
                                       			 default firmware load that is specified in the Device Defaults Configuration window. |
| Step 4 | Complete any remaining fields in the Phone Configuration window. For help with the
                                       			 fields and their settings, see the online help. |
| Step 5 | Click Save . |
| Step 6 | Click Apply Config to push the changed fields to the
                                       			 phone. |

| Note | If you wish to assign a load server for many phones you can use the
                                          			 Bulk Administration Tool to configure the Load Server field using a CSV file or query.
                                          			 For details, see the Bulk Administration Guide for Cisco Unified Communications
                                             				Manager . |
|---|---|

| Step 1 | In Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select an individual phone. |
| Step 3 | In the Load Server field, enter the IP Address or
                                       			 hostname of the alternate server. |
| Step 4 | Complete any remaining fields in the Phone Configuration window. For help with the
                                       			 fields and their settings, see the online help. |
| Step 5 | Click Save . |
| Step 6 | Click Apply Config to push the changed fields to the
                                       			 phone. |

| Note | Each device can have an individually assigned firmware load that overrides the default. |
|---|---|

| Step 1 | Choose Device > Device Settings > Firmware Load Information . The page updates to display a list of device types that require firmware loads. For each device type, the Devices Not Using
                                          Default Load column links to configuration settings for any devices that use a non-default load. |
|---|---|
| Step 2 | To view a list of devices of a particular device type that are using a non-default device load, click the entry for that device
                                       type in the Devices Not Using Default Load column. The window that opens lists the devices of a particular device type that are not running the default firmware load. |