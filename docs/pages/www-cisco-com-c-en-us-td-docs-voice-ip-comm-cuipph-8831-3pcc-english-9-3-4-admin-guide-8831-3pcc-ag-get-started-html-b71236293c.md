---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-3pcc-english-9-3-4-admin-guide-8831-3pcc-ag-get-started-html-b71236293c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/3PCC/english/9_3_4/admin-guide/8831-3pcc-ag/get-started.html
retrieved_at: 2026-08-21T02:09:13.551596+00:00
---

Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Administration Guide, Release 9.3(4)

# Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Administration Guide, Release 9.3(4)

Updated: October 22, 2014

Chapter: Get Started

## Chapter: Get Started

## Get Started

This chapter contains basic information on Cisco Unified IP Conference Phone 8831 for Third-Party Call Control. This chapter contains the following sections:

## Overview of the Conference Phone

The Cisco Unified IP Conference Phone 8831 for Third-Party Call Control is a full-featured VoIP (Voice-over-Internet Protocol) phone that provides voice communication over an IP network. It provides all the features of traditional business phones, such as call forwarding, redialing, speed dialing, transferring calls, and conference calling. The Conference Phone is targeted for solutions centered on 3rd-Party SIP-based IP PBX.

For more information on phone features, see the data sheets for this product.

## Network Configurations

The Cisco Unified IP Conference Phone 8831 for Third-Party Call Control is used as a part of a SIP network as it supports Session Initiation Protocol (SIP).

This document describes some common network configurations; however, your configuration can vary, depending on the type of equipment used by your service provider.

### Other SIP IP PBX Call Control Systems

The Cisco Unified IP Conference Phone 8831 for Third-Party Call Control are compatible with other SIP IP PBX call control systems, such as BroadSoft, MetaSwitch, and Asterisk. Configuration of these systems is not described in this document. For more information, see the documentation for the SIP PBX system to which you are connecting the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control.

## Use the Web-Based Configuration Utility

Your phone system administrator can allow you to view the phone statistics and modify some or all of the parameters by using the phone web user interface. The features of the conference phone that can be modified by the user by using the phone web user interface are described in this document.

To access the IP phone configuration utility, launch a web browser on a computer that can reach the phone on the subnetwork and enter the IP address of the phone in your web browser address bar. For example, http://192.168.1.8 . If you are connected to a VPN, you must first exit the VPN.

Note If your service provider disabled access to the configuration utility, you must contact the service provider to proceed.

### Determine the IP Address of the Phone

The IP address is assigned by a DHCP server, so the phone must be booted up and connected to the subnetwork.

To display your IP address:

Step 1 Click Admin Login > advanced > Info > System Status .

Step 2 Scroll to System Information . The IP Address is displayed under Current IP.

### Allow Web Access to the Conference Phone

To view the phone parameters by using the phone web user interface, the configuration profile must be enabled. To make changes to any of the parameters by using the phone web user interface, the configuration profile must be writable. Your system administrator might have disabled the phone option to make the phone web user interface viewable or writable.

For more information, see the provisioning guide for the conference phone.

To allow or disallow from the phone viewing of the phone web user interface:

Step 1 Click Admin login > Advanced > Voice Tab > System .

Step 2 Scroll to System Configuration .

Step 3 Set Enable Web Server to Yes .

### Save the Configuration Profile

Click Submit All Changes when you have finished modifying the fields in the phone web user interface to update the configuration profile. The phone is rebooted and the changes are applied.

Click Undo All Changes if you want to clear all changes made this session and return to the parameter values set before the session began or since the last time you clicked Submit All Changes .

## Understand Administrator and User Views

The Cisco Unified IP Conference Phone 8831 for Third-Party Call Control firmware provides specific privileges for login to a user account and an administrator account. The Administrator account name is admin , and the User account name is user . These account names cannot be changed. The Admin account is designed to give the service provider or VAR configuration access to the Cisco IP phone, while the User account is designed to give limited and configurable control to the end user of the device.

The User and Admin accounts can be independently password protected. If the service provider set an Administrator account password, you are prompted for it when you click Admin Login . If it does not yet exist, the screen is refreshed, displaying the administration parameters. No default passwords are assigned to either the Administrator or the User accounts. Only the Administrator account can assign or change passwords.

The Administrator account can view and modify all web profile parameters, including web parameters available to the user login. The phone system administrator can further restrict the parameters that a User account can view and modify by using a provisioning profile .

The configuration parameters that are available to the User account are configurable in the conference phone. User access to the conference phone web user interface can be disabled.

### Restrict User Access to the Phone Interface Menus

The Admin account can set the phone web user interface to allow or disable access by the User account. Allowing User account access gives a user the option of setting parameters, such as speed dial numbers and caller ID blocking through the phone web user interface.

The ability to configure individual parameters can be restricted by using phone profile provisioning. For more information on provisioning, see the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Provisioning Guide on cisco.com.

To change the user account access to the phone LCD GUI setup menu:

Step 1 Click Admin Login > advanced > Voice > System .

Step 2 Under System Configuration in the Phone-UI-user-mode field, choose Yes .

### Access Administrative Options

To access administrative options, either:

- Log in to the configuration utility, then click Admin Login .

- Enter the IP address of the phone in a Web browser and include the admin/ extension. For example: http://192.168.1.220/admin/

### Use the Web Administration Tabs

Each tab contains parameters related to that feature. Some tasks require that you set multiple parameters in different tabs.

Appendix A, “Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Field Reference,” briefly describes each parameter available on the phone web user interface.

## View Phone Information

You can check the current status of the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control by clicking the Info tab. The Info tab shows information about all phone extensions, including phone statistics and the registration status.

### View Reboot Reasons

The phone stores the most recent five reasons the phone was refreshed or rebooted. When the phone is reset to factory defaults, this information is deleted.

The list describes the reboot and refresh reasons for Cisco Unified IP Conference Phone 8831 for Third-Party Call Control.

Upgrade

The reboot was a result of an upgrade operation (regardless whether the upgrade completed or failed).

Provisioning

The reboot was the result of changes made to parameter values by using the IP phone screen or phone web user interface, or as a result of synchronization.

SIP Triggered

The reboot was triggered by a SIP request.

RC

The reboot was triggered as a result of remote customization.

User Triggered

The user manually triggered a cold reboot.

IP Changed

The reboot was triggered after the phone IP address was changed.

You can view the reboot history from the phone web user interface, the IP phone screen, and the phone Status Dump file (http:// phoneIP /status.xml or http:// phoneIP /admin/status.xml).

### View the Reboot History on the Phone Web User Interface

The Info > System Information > Reboot History page displays the device reboot history, the five most recent reboot dates and times and a reason for the reboot. Each field displays the reason for the reboot and a time stamp indicating when the reboot took place. For example:

The reboot history is displayed in reverse chronological order; the reason for the most recent reboot is displayed in Reboot Reason 1 .

### View the Reboot History on the Phone Screen

Reboot History is located under Apps > Admin Settings > Status menu. In the Reboot History window, the reboot entries are displayed in reverse chronological order, similar to the sequence that is displayed on the phone web user interface.

### View the Reboot History in the Status Dump File

The reboot history is stored in the Status Dump file (http:// <phone_IP_address> /admin/status.xml). In this file, tags Reboot_Reason_1 to Reboot_Reason_3 store the reboot history, as shown in this example:

## Wireless Microphone Region Setting

The Wireless Microphone Frequency Lock enhancement provides a secure Digital Enhanced Cordless Telecommunications (DECT) frequency for wireless microphones by locking the wireless region setting.

When the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control is shipped from the manufacturer, the mask and the Wireless Microphone Region setting are already configured for a particular region. For all devices, no matter the firmware release, no wireless region setting is available to the user.

If your Cisco Unified IP Conference Phone 8831 for Third-Party Call Control is operating with an earlier firmware release, you must upgrade to firmware release 9.3(4) so that the Wireless Microphone Region can be locked. Six new firmware versions lock this setting for customers who are running firmware versions earlier than firmware release 9.3(4).

If a device is shipped with firmware release 9.3(4) or later, its wireless region setting is set during manufacturing to one of the following values:

- NA – North America

- EU – Europe

- JP – Japan

- BR– Brazil

- TW– Taiwan

- LA – Latin America

Note For devices that are shipped with firmware release 9.3(4) and later, the wireless region cannot be changed.

If a device is shipped with firmware release 9.3(3), only one wireless region, NA (North America), exists.

Note Although you cannot change the value of the Wireless Microphone Region setting, you can check its value. To do so, execute Info > System Status > Product Information and check the Wireless Microphone Region value on the webpage.

Refer to the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Release Notes for Firmware Release 9.3(4) if you need to upgrade a device from firmware release 9.3(3) to 9.3(4).

| Reason | Description |
|---|---|
| Upgrade | The reboot was a result of an upgrade operation (regardless whether the upgrade completed or failed). |
| Provisioning | The reboot was the result of changes made to parameter values by using the IP phone screen or phone web user interface, or as a result of synchronization. |
| SIP Triggered | The reboot was triggered by a SIP request. |
| RC | The reboot was triggered as a result of remote customization. |
| User Triggered | The user manually triggered a cold reboot. |
| IP Changed | The reboot was triggered after the phone IP address was changed. |