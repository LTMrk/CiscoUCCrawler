---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-compat-devpacks-admin-cmdp-bk-cd82f19c-00-cisco-unified-communications--26ad2faee5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/Devpacks_admin/CMDP_BK_CD82F19C_00_cisco-unified-communications-manager-device/Cisco_Unified_Communications_Manager_Device_Package_Installation_and_Administration.html
retrieved_at: 2026-08-16T23:48:14.820605+00:00
---

Cisco Unified Communications Manager Device Package Installation Guide

# Cisco Unified Communications Manager Device Package Installation Guide

## Results

Updated: July 8, 2015

Chapter: Cisco Unified
	 Communications Manager Device Package Installation

## Chapter: Cisco Unified
	 Communications Manager Device Package Installation

# Cisco Unified
                     	 Communications Manager Device Package Installation

## Introduction

This document provides the information you need to install and manage the Cisco Unified Communications Manager device packages.

For a listing of recent device packages, see Cisco Unified Communications Manager Device Package Compatibility Matrix .

To download a recent device package, see the Download Software page on Cisco.com and select your Cisco Unified Communications Manager version.

## Software Version
                        	 Identification

To determine the version of Cisco Unified Communications Manager software that is running on your server, access Cisco Unified
                              Communications Manager Administration and then click Help > About .

## Software
                        	 Compatibility

Cisco Unified Communications Manager device package releases are compatible with Cisco Unified Communications Manager.

Cisco Collaboration Endpoint releases don't always coincide with Cisco Unified Communications Manager releases, so we recommend
                              that you upgrade to the latest firmware.

For the latest compatibility information, see the following:

Cisco Unified Communications Manager Device Package Compatibility Matrix : http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html .

Software download page for Collaboration Endpoints: https://software.cisco.com/download/home/283611953

Support documentation for Collaboration Endpoints: https://www.cisco.com/c/en/us/support/collaboration-endpoints/index.html .

## Install a Device
                        	 Pack

Install a device package to introduce new phone types and upgrade the firmware for multiple phone models.

Apply this device package to all your Cisco Unified Communications Manager servers, beginning with the publisher server and
                              the TFTP server.

To install and upgrade all software, use the Software Upgrades menu options. The system can upload and process only Cisco
                              approved software. You cannot install or use third-party or Windows-based software applications that you used with a previous
                              version of Cisco Unified Communications Manager.

The device package is necessary to obtain configuration capability for new features and phone models. Otherwise individual
                                          device firmware is installed with the individual device load Cisco Options Package file. You can also upload the individual
                                          device load files to the TFTP directory. After the new files are present in the TFTP folder, restart the TFTP service from
                                          the Cisco Unified Serviceability Web Page. Then go to CCMAdmin > Device > Device Settings > Device Defaults and manually change the name of the load file (for specific devices) to the new load. Click Save . Reset the devices.

### Before you begin

We recommend that you apply a device package during a maintenance window.

You install device packages on the active partition and cannot uninstall them. We recommend that you take a Disaster Recovery
                              System (DRS) backup before you install a device package. For backup procedure, see the Disaster Recovery System Administration Guide for each version of Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

From your web browser, log in to the Cisco Unified Communications Operating System Administration web page.

From the
                                       			 Software Upgrades menu, select Install/Upgrade .

Fill in the
                                       			 appropriate values in the Software Location section and click Next .

In the
                                       			 Available Software drop-down box, select the device package file and click Next .

Verify that
                                       			 the MD5 has the correct value. Click Next .

In the Warning
                                       			 box, verify that you selected the correct firmware and click Install .

Check that you received a Success message.

Restart the Cisco TFTP service on all nodes where the service is running.

Reset the affected devices to upgrade the devices to the new load.

From Cisco Unified CM Administration, choose Device > Device Settings > Device Defaults and manually change the name of the load file for specific devices to the new load.

Click Save . Reset the devices.

Restart the Cisco Tomcat service on all cluster nodes.

If you are running 11.5(1)SU4 or lower, 12.0(1) or 12.0(1)SU1, reboot the cluster.

If you are running 11.5(1)SU5 or higher, or 12.0(1)SU2 or higher, reboot the Cisco CallManager service on the publisher node.
                                       However, if you are running the Cisco Call Manager service on the subscriber nodes only, you can skip this task.

## Troubleshoot a Device Package Installation

The following table lists common issues associated with a device package installation. Use this information to troubleshoot
                              your installation.

Issue

Resolution

A new device doesn't register.

This issue often occurs because of a device type mismatch. Check the following:

The device was added in the Phone Configuration window using the wrong device type. For example, Cisco DX80 was selected as
                                                the phone type instead of Cisco TelePresence DX80. Reconfigure the device with the correct device type.

The Cisco Unified Communications Manager service doesn’t recognize the new device type. Restart the Cisco Unified Communications
                                                Manager service on the publisher node.

Devices aren’t upgrading to the new firmware.

Possible reasons:

The device pack wasn’t installed on the TFTP server. As a result, the firmware isn’t available for download by the devices.

The Cisco TFTP service wasn’t restarted after the install. Make sure to install the device pack on the TFTP server.

The Phone Configuration window in Cisco Unified CM Administration shows a broken link instead of device icon.

Restart the Cisco Tomcat service from the Command Line Interface (CLI).

## Uninstall a Device
                        	 Pack

You cannot uninstall a device package. However, you can change the device defaults for the devices that you wish to roll back.

From your web browser, log in to the Cisco Unified CM Administration web page.

Navigate to Device > Device
                                          				Settings > Device
                                          				Defaults .

Set the
                                       			 affected devices back to their previous firmware settings.

Click Save .

Reset the
                                       			 affected devices.

## Log File
                        	 Information

The system creates log files that you can view using the Cisco Unified Communications Manager Serviceability Real-Time Monitoring
                              Tool. Follow these paths to view each of the log files:

Select Trace and Log Central > Remote Browse > Install and Upgrade Logs .

Select Trace and Log Central > Collect Files > Install and Upgrade Logs .

Select Trace and Log Central > Query Wizard > Install and Upgrade Logs .

Select Trace and Log Central > Schedule Collection > Install and Upgrade Logs .

## Unified
                        	 Communications Manager Endpoints Locale Installer

By default, Cisco
                              		  IP Phones are set up for the English (United States) locale. To use the Cisco
                              		  IP Phones in other locales, you must install the locale-specific version of the
                              		  Unified Communications Manager Endpoints Locale Installer on every Cisco
                              		  Unified Communications Manager server in the cluster. The Locale Installer
                              		  installs the latest translated text for the phone user interface and
                              		  country-specific phone tones on your system so that they are available for the
                              		  Cisco IP Phones.

To access the Locale Installer required for a release, access https://software.cisco.com/download/navigator.html?mdfid=286037605&flowid=46245 , navigate to your phone model, and select the Unified Communications Manager Endpoints Locale Installer link.

For more information, see the documentation for your particular Cisco Unified Communications Manager release.

The latest
                                          			 Locale Installer may not be immediately available; continue to check the
                                          			 website for updates.

## Cisco IP Phone Documentation Updates on Cisco Unified Communications Manager

The Cisco Unified Communications Manager Self Care Portal (Release 10.0 and later) and User Options web pages (Release 9.1
                              and earlier) provide  links to the IP Phone user guides in PDF format. These user guides are stored on the Cisco Unified Communications
                              Manager and are up to date when the Cisco Unified Communications Manager release is first made available to customers.

After a Cisco Unified Communications Manager release, subsequent updates to the user guides appear only on the Cisco website.
                              The phone firmware release notes contain the applicable documentation URLs. In the web pages, updated documents display "Updated" beside the document link.

The Cisco Unified Communications Manager Device Packages and the Unified Communications Manager Endpoints Locale Installer
                                          do not update the English user guides on the Cisco Unified Communications Manager.

You and your users should check the Cisco website for updated user guides and download the PDF files. You can also make the
                              files available to your users on your company website.

You may want to bookmark the web pages for the phone models that are deployed in your company and send these URLs to your
                                          users.

### Customers Also Viewed

- Cisco Unified Communications Manager Device Package Compatibility Matrix --- Current Cisco Unified Communications Manager Device Package Releases

| Note | Review the Show Software page in Cisco Unified OS Administration to determine your installed device package. We recommend
                                       that you don't install an older version of the device package. |
|---|---|

| Note | The device package is necessary to obtain configuration capability for new features and phone models. Otherwise individual
                                          device firmware is installed with the individual device load Cisco Options Package file. You can also upload the individual
                                          device load files to the TFTP directory. After the new files are present in the TFTP folder, restart the TFTP service from
                                          the Cisco Unified Serviceability Web Page. Then go to CCMAdmin > Device > Device Settings > Device Defaults and manually change the name of the load file (for specific devices) to the new load. Click Save . Reset the devices. |
|---|---|

| Step 1 | From your web browser, log in to the Cisco Unified Communications Operating System Administration web page. |
|---|---|
| Step 2 | From the
                                       			 Software Upgrades menu, select Install/Upgrade . |
| Step 3 | Fill in the
                                       			 appropriate values in the Software Location section and click Next . |
| Step 4 | In the
                                       			 Available Software drop-down box, select the device package file and click Next . |
| Step 5 | Verify that
                                       			 the MD5 has the correct value. Click Next . |
| Step 6 | In the Warning
                                       			 box, verify that you selected the correct firmware and click Install . |
| Step 7 | Check that you received a Success message. Note Skip to Step 9 if rebooting the cluster. | Note | Skip to Step 9 if rebooting the cluster. |
| Note | Skip to Step 9 if rebooting the cluster. |
| Step 8 | Restart the Cisco TFTP service on all nodes where the service is running. |
| Step 9 | Reset the affected devices to upgrade the devices to the new load. |
| Step 10 | From Cisco Unified CM Administration, choose Device > Device Settings > Device Defaults and manually change the name of the load file for specific devices to the new load. |
| Step 11 | Click Save . Reset the devices. |
| Step 12 | Restart the Cisco Tomcat service on all cluster nodes. |
| Step 13 | If you are running 11.5(1)SU4 or lower, 12.0(1) or 12.0(1)SU1, reboot the cluster. |
| Step 14 | If you are running 11.5(1)SU5 or higher, or 12.0(1)SU2 or higher, reboot the Cisco CallManager service on the publisher node.
                                       However, if you are running the Cisco Call Manager service on the subscriber nodes only, you can skip this task. |

| Note | Skip to Step 9 if rebooting the cluster. |
|---|---|

| Issue | Resolution |
|---|---|
| A new device doesn't register. | This issue often occurs because of a device type mismatch. Check the following: The device was added in the Phone Configuration window using the wrong device type. For example, Cisco DX80 was selected as
                                                the phone type instead of Cisco TelePresence DX80. Reconfigure the device with the correct device type. The Cisco Unified Communications Manager service doesn’t recognize the new device type. Restart the Cisco Unified Communications
                                                Manager service on the publisher node. |
| Devices aren’t upgrading to the new firmware. | Possible reasons: The device pack wasn’t installed on the TFTP server. As a result, the firmware isn’t available for download by the devices. The Cisco TFTP service wasn’t restarted after the install. Make sure to install the device pack on the TFTP server. |
| The Phone Configuration window in Cisco Unified CM Administration shows a broken link instead of device icon. | Restart the Cisco Tomcat service from the Command Line Interface (CLI). |

| Step 1 | From your web browser, log in to the Cisco Unified CM Administration web page. |
|---|---|
| Step 2 | Navigate to Device > Device
                                          				Settings > Device
                                          				Defaults . |
| Step 3 | Set the
                                       			 affected devices back to their previous firmware settings. |
| Step 4 | Click Save . |
| Step 5 | Reset the
                                       			 affected devices. |

| Note | The latest
                                          			 Locale Installer may not be immediately available; continue to check the
                                          			 website for updates. |
|---|---|

| Note | The Cisco Unified Communications Manager Device Packages and the Unified Communications Manager Endpoints Locale Installer
                                          do not update the English user guides on the Cisco Unified Communications Manager. |
|---|---|

| Tip | You may want to bookmark the web pages for the phone models that are deployed in your company and send these URLs to your
                                          users. |
|---|---|