---
doc_id: www-cisco-com-c-en-us-td-docs-telepresence-cucm-cts-cucm-cts-admin-book-guide-cucm-cts-admin-cucm-cts-admin-verification-b62d275cef
source_url: https://www.cisco.com/c/en/us/td/docs/telepresence/cucm_cts/cucm_cts_admin_book/guide/cucm_cts_admin/cucm_cts_admin_verification.html
retrieved_at: 2026-08-17T00:10:03.301072+00:00
---

Cisco Unified Communications Manager Configuration Guide for the Cisco TelePresence System

# Cisco Unified Communications Manager Configuration Guide for the Cisco TelePresence System

Updated: April 15, 2014

Chapter: Verifying and Troubleshooting the Cisco TelePresence System Configuration

## Chapter: Verifying and Troubleshooting the Cisco TelePresence System Configuration

Revised: June 9, 2015, OL-21851-01

## Contents

The following sections describe how to verify your Cisco TelePresence System with Cisco Unified Communications Manager (Unified CM) configuration:

## Troubleshooting Your Configuration

Use the information in Table 4-1 to help you troubleshoot your configuration.

Before You Begin

First check that the following conditions have been met:

- Power has been applied.

- The Cisco TelePresence System has been installed and configured according to the instructions in Cisco TelePresence System Assembly Guides.

- Unified CM has been configured to support the Cisco TelePresence System as described in this guide.

- The endpoint can be accessed with an IP address through the Web UI.

Testing Your Unified CM Server

You also can test for proper communication between your Unified CM server by completing the following steps:

Step 1	Log in to the Admin CLI with Secure Shell (SSH).

Step 2	Enter the command utils network ping {X}, where X is the IP address or DNS name of the Unified CM server. If the command results in a 0% packet loss, the network is functioning properly. If there is any packet loss, check your network for errors.

Table 4-1 Troubleshooting the Cisco TelePresence Configuration

Problem

Possible Cause

Possible Solutions

The system does not upgrade.

- The system cannot find or download the upgrade file from the Cisco Unified CM TFTP server.

- AutoUpgrade is set to false.

1.	Check that the correct upgrade file name is configured on the TX system Device page in Cisco Unified CM.

2.	Check whether the upgrade file is uploaded to the TFTP server.

3.	Check whether TFTP service has been restarted after the upgrade file is uploaded.

4.	Check whether the TX system is pointed to correct the TFTP server where the upgrade file is located.

5.	Set AutoUpgrade to True. Determine your settings by entering the following CLI command:

show upgrade det

If AutoUpgrade is set to False, re-set it to True. Contact TAC for assistance.

See also the Cisco TelePresence Administration Software Command References home page on Cisco.com for information about CLI commands

The system was moved to a different Unified CM and the registration is rejected.

CTL File Issues

The system was associated with a different secure Unified CM at one time and the system preserved the previous Certificate Trust List (CTL) file.

Delete the CTL file through the administration interface in the Cisco Unified CM Administration interface.

The Cisco TelePresence unit does not register with Unified CM:

- From the Unified CM device page, the system status shows unregistered or unknown.

- From the codec Web user interface (UI), system status shows unknown or inaccessible for Unified CM.

CTS Unknown Issues

Cisco TelePresence System could be unknown:

- MAC address is entered incorrectly.

- Cisco Unified CM does not know about the system.

- System is not registered because it is unplugged.

Profile or Provisioning Issues

- System profile is not provisioned properly in Cisco Unified CM.

Directory Number Issues

- Directory Number (DN) is not configured.

- Verify the phone registration by doing the following:

–	Log in to the Cisco Unified CM Administration interface.

–	Click on the IP address and verify the phone registration.

- Log in to Unified CM and make sure that the system profile and the directory number (DN) are created and configured properly.

- Make sure the system MAC address is entered correctly in Unified CM.

- Delete the CTL file through the administration interface.

- Completely delete the system from Unified CM, including its associated DN, then add it back to Unified CM.

Tip	Even if you make minor changes on the Unified CM Device page (such as in the Description field), remember to click Save and restart the system.

TFTP Issues

- Unified CM or TFTP service issue.

- TFTP port 6970 is blocked so that the CTS cannot download the “device config xml” file from Unified CM TFTP server.

XML Issues

- XML configuration file is suspected to be corrupted on the Unified CM database.

- Make sure Unified CM and TFTP service is running. Restart services if necessary.

- Make sure there is no firewall or device between the system and Cisco Unified CM that blocks the 6970 port.

Hostname Issues

- Cannot resolve hostname of Unified CM.

If you are using the Unified CM hostname as the TFTP server on the system, make sure that the hostname can be resolved by the domain name system (DNS).

System un-registers from time to time.

SIP Issues

- The system experiences a SIP registration timeout.

Network Issues

- Intermittent network issues could cause packets to be dropped.

1.	Confirm that Unified CM is receiving SIP messages and whether the system is responding.

2.	Collect a packet capture if necessary to submit to Cisco technical response for further review.

Orange question mark appears in the Administration interface Troubleshooting > Microphones page for the two outside microphones of the second row table (CTS 32x0 and TX9200 only).

The second row was configured for a “reduced configuration” second row that seats eight people rather than 12. The two outside microphones are not recognized by the system.

Change the Second Row Capacity setting from 8 to 12. See Product Specific Configuration Layout Area to update your Second Row Capacity settings.

The Touch 12 device is not recognized or not available.

COP File Issues

- The image COP file was not installed or not correctly installed.

Device Information Issues

- The Phone Load Name is not correct in Unified CM.

Device Pack Issues

- The Device Pack was not installed or not correctly installed.

- The system software upgraded, but a new Device Pack was not installed.

- Re-install the COP file. Refer to the “Upgrading From Cisco TelePresence Software Releases 1.7.4 and Above” section for instructions.

- Enter the correct Phone Load Name in Unified CM:

–	Log in to Unified CM and navigate to Device > Phone.

–	Enter search criteria for your device, and click on the hyperlink under Device Name to view the Device Information page.

–	Enter the correct Phone Load Name.

- Re-install the Device Pack.

Time does not show correctly on the system or Touch 12.

Network Time Protocol ( NTP) is not configured properly or the codec does not sync up with NTP.

1.	If NTP is not configured, access Cisco Unified CM date/time group, configure NTP properly and assign to a system device pool.

2.	Make sure that the system can ping NTP, and there is no firewall blocking the 123 NTP port.

See also the Cisco TelePresence System Administration Guide .

## Managing Passwords

The following sections contain information to help you manage your passwords:

### Resetting Your Unified CM Secure Shell Password

To reset your secure shell password:

Step 1	Log into the Cisco Unified CM Administration interface.

Step 2	Navigate to Device > Phone. The Find and List Phones window appears.

Step 3	To locate a specific phone, enter search criteria and click Find.

Step 4	Click on the hyperlink under Device Name, and scroll down to the Product Specific Configuration Layout Area .

Step 5	Scroll down to the SSH Information Area .

Step 6	Change your password using the following guidelines:

- Maximum field length—64 characters

- Minimum field length—6 characters

Step 7	Under SSH admin Life, enter a number between 0 and 365. This will dictate the time parameter of your password:

- If 0, the password will never expire.

- If 365, the password will expire in 365 days.

Step 8	Save your changes by clicking Restart. This enables the updated configuration to be read and applied to the system; and then Calling Service is restarted. Alternately you can click Reset, which causes the system to reboot. On startup, the system reads the Unified CM configuration and applies any changes.

See the “SSH Information Area” section for more information about password aging.

### Resetting Your CTS Codec Password

Note You must be in the Cisco TelePresence room to read the newly requested pass code that shows on the main display. At each point where the pwrecovery account requires input, the program will wait up to 60 seconds. If nothing is entered, the Cisco TelePresence System will inform you that the entry took too long and will exit. If you encounter any difficulty, open a case with Technical Assistance Center (TAC) via the Internet at http://tools.cisco.com/ServiceRequestTool/create/ , or contact your Cisco technical support representative and provide the representative with the information you have gathered about the problem.

Before You Begin

Make sure that the system is not in a call, and that there is only one instance of someone trying to reset the password, otherwise the session will abort.

To reset your system codec password:

Step 1 SSH into the codec from your laptop.

Step 2 Login with the following:

- Username: pwrecovery

- Password: pwreset

The following message appears in the SSH client window:

Example 4-1	Welcome to Password Reset

dhcp-249:~ $ ssh pwrecovery@10.00.00.100

pwrecovery@10.00.00.100's password:

*********************************************** ***********************************************

** 							                   **

** 		Welcome to password reset             **

** 							                   **

*********************************************** *********************************************** Do you want to continue ? (y/n):y Preparing the system... Please enter the passcode:

Step 3	The system will ask whether you want to continue. Type Y then return to continue

Note If desired, type any other key then return to exit.

This system will now prepare for password reset and prompt you for a passcode. The new passcode is displayed on the system main display, as shown in the following example:

Password reset is now being run

Passcode: 919175

Note The passcode is a randomly generated number and will be different for each login attempt. If you enter the wrong passcode, the system will inform you that the passcode was incorrect and will exit, as shown in the following example. If this happens, repeat Step 1 and Step 2 .

Example 4-2	Invalid Password Reset Request

Do you want to continue ? (y/n):y

Preparing the system...

Please enter the passcode:12345

Sorry that was an invalid passcode...

Logging off

Connection to 10.00.00.100 closed.

dhcp-249:~ $

When you enter the correct passcode, the system will then reset the administration account name and password to the system defaults. The following example shows successful password reset information:

Example 4-3	Successful Password Reset Request

Please enter the passcode:507530

resetting admin name and password

stopping any existing admin session

admin account and password reset to default

success in applying security rules

Logging off

Connection to 10.00.00.100 closed.

dhcp-249:~ $

Note If you are using the system with a Cisco Unified Communications Manager, the next time you perform a “Refresh” or “Reset” from the Unified CM, the administration account name and password will be reconfigured to the values specified in the Unified CM device page.

## Managing Phone Reset and Codec Connectivity

The following sections contain information about managing the following system components:

### Resetting a Cisco TelePresence System

If a device is not registered with Cisco Unified Communications Manager, you cannot reset or restart it. If a device is registered, to restart a device without shutting it down, click the Restart button. To shut down a device and bring it back up, click the Reset button. To return to the previous window without resetting or restarting the device, click Close.

### Synchronizing a Cisco TelePresence System

To synchronize a phone with the most recent configuration changes, perform the following procedure, which applies any outstanding configuration settings in the least-intrusive manner possible. (For example, a reset/restart may not be required on some affected devices.)

Step 1	Choose Device > Phone . The Find and List Phones window appears.

Step 2	Choose the search criteria to use and Click Find . The window displays a list of phones that match the search criteria.

Step 3	Check the check boxes next to the phones that you want to synchronize. To choose all phones in the window, check the check box in the matching records title bar.

Step 4	Click Apply Config to Selected . The Apply Configuration Information dialog displays.

Step 5	Click OK .

### Restoring Connectivity to the Codec

If you lose connectivity to the CTS codec(s), power off the system by turning the following power switches to the Off position: the two left PDUs, single right PDU, and the PDU or auxiliary control unit behind the center display assembly (if present). Then power on the system by turning each switch to the On position. Connectivity should automatically be restored.

For more information about the system codec, refer to the Cisco TelePresence System Assembly, Use & Care, and Field-Replaceable Unit Guide for your system on Cisco.com:

Support > Products > TelePresence > Cisco TelePresence System

### Related Information

See the Cisco TelePresence System Troubleshooting Guide for information about system passwords and troubleshooting the Cisco TelePresence System and Cisco Unified CM Administration interfaces and related hardware components.

| Problem | Possible Cause | Possible Solutions |
|---|---|---|
| The system does not upgrade. | The system cannot find or download the upgrade file from the Cisco Unified CM TFTP server. AutoUpgrade is set to false. | 1.	Check that the correct upgrade file name is configured on the TX system Device page in Cisco Unified CM. 2.	Check whether the upgrade file is uploaded to the TFTP server. 3.	Check whether TFTP service has been restarted after the upgrade file is uploaded. 4.	Check whether the TX system is pointed to correct the TFTP server where the upgrade file is located. 5.	Set AutoUpgrade to True. Determine your settings by entering the following CLI command: show upgrade det If AutoUpgrade is set to False, re-set it to True. Contact TAC for assistance. See also the Cisco TelePresence Administration Software Command References home page on Cisco.com for information about CLI commands |
| The system was moved to a different Unified CM and the registration is rejected. | CTL File Issues The system was associated with a different secure Unified CM at one time and the system preserved the previous Certificate Trust List (CTL) file. | Delete the CTL file through the administration interface in the Cisco Unified CM Administration interface. |
| The Cisco TelePresence unit does not register with Unified CM: From the Unified CM device page, the system status shows unregistered or unknown. From the codec Web user interface (UI), system status shows unknown or inaccessible for Unified CM. | CTS Unknown Issues Cisco TelePresence System could be unknown: MAC address is entered incorrectly. Cisco Unified CM does not know about the system. System is not registered because it is unplugged. Profile or Provisioning Issues System profile is not provisioned properly in Cisco Unified CM. Directory Number Issues Directory Number (DN) is not configured. | Verify the phone registration by doing the following: –	Log in to the Cisco Unified CM Administration interface. –	Click on the IP address and verify the phone registration. Log in to Unified CM and make sure that the system profile and the directory number (DN) are created and configured properly. Make sure the system MAC address is entered correctly in Unified CM. Delete the CTL file through the administration interface. Completely delete the system from Unified CM, including its associated DN, then add it back to Unified CM. Tip	Even if you make minor changes on the Unified CM Device page (such as in the Description field), remember to click Save and restart the system. |
| TFTP Issues Unified CM or TFTP service issue. TFTP port 6970 is blocked so that the CTS cannot download the “device config xml” file from Unified CM TFTP server. XML Issues XML configuration file is suspected to be corrupted on the Unified CM database. | Make sure Unified CM and TFTP service is running. Restart services if necessary. Make sure there is no firewall or device between the system and Cisco Unified CM that blocks the 6970 port. |
| Hostname Issues Cannot resolve hostname of Unified CM. | If you are using the Unified CM hostname as the TFTP server on the system, make sure that the hostname can be resolved by the domain name system (DNS). |
| System un-registers from time to time. | SIP Issues The system experiences a SIP registration timeout. Network Issues Intermittent network issues could cause packets to be dropped. | 1.	Confirm that Unified CM is receiving SIP messages and whether the system is responding. 2.	Collect a packet capture if necessary to submit to Cisco technical response for further review. |
| Orange question mark appears in the Administration interface Troubleshooting > Microphones page for the two outside microphones of the second row table (CTS 32x0 and TX9200 only). | The second row was configured for a “reduced configuration” second row that seats eight people rather than 12. The two outside microphones are not recognized by the system. | Change the Second Row Capacity setting from 8 to 12. See Product Specific Configuration Layout Area to update your Second Row Capacity settings. |
| The Touch 12 device is not recognized or not available. | COP File Issues The image COP file was not installed or not correctly installed. Device Information Issues The Phone Load Name is not correct in Unified CM. Device Pack Issues The Device Pack was not installed or not correctly installed. The system software upgraded, but a new Device Pack was not installed. | Re-install the COP file. Refer to the “Upgrading From Cisco TelePresence Software Releases 1.7.4 and Above” section for instructions. Enter the correct Phone Load Name in Unified CM: –	Log in to Unified CM and navigate to Device > Phone. –	Enter search criteria for your device, and click on the hyperlink under Device Name to view the Device Information page. –	Enter the correct Phone Load Name. Re-install the Device Pack. |
| Time does not show correctly on the system or Touch 12. | Network Time Protocol ( NTP) is not configured properly or the codec does not sync up with NTP. | 1.	If NTP is not configured, access Cisco Unified CM date/time group, configure NTP properly and assign to a system device pool. 2.	Make sure that the system can ping NTP, and there is no firewall blocking the 123 NTP port. See also the Cisco TelePresence System Administration Guide . |