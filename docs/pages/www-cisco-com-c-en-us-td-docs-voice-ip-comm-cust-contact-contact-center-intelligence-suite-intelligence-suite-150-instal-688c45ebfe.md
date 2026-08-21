---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-150-instal-688c45ebfe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_150/install/guide/cuic_b_install_upgrade_guide_15_0/cuic_m_1501_controller_configuration.html
retrieved_at: 2026-08-21T04:41:07.991636+00:00
---

Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 15.0(1)

# Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 15.0(1)

Updated: April 30, 2025

Chapter: Controller Configuration

## Chapter: Controller Configuration

- Controller Configuration

- Complete                              	 Configuration for First Node

# Controller Configuration

## Complete
                        	 Configuration for First Node

When you complete
                              		  the basic install configuration and select Yes to indicate that you are installing the first
                              		  node, perform the following steps to complete the configuration for the
                              		  Controller.

The first screen you
                              		  see is the Network
                                 			 Time Protocol Client Configuration screen.

This screen gives
                              		  the option of setting the time for the first node (the Controller) from a time
                              		  that you set on the Hardware Clock screen - or - from an external Network Time
                              		  Protocol server that you define.

Step 1

Select Yes at the Network
                                          				Time Protocol Client Configuration screen.

The Network Time Protocol Client Configuration screen
                                          				opens.

Step 2

Enter the IP
                                       			 address, NTP server name, or NTP Server Pool name for at least one external NTP
                                       			 server.

You can add up
                                          				to five NTP servers and make changes to the NTP server list at a later time.

Step 3

When you
                                       			 complete the NTP configuration, select OK .

The Security
                                          				Configuration screen opens.

Step 4

In the Security
                                          				Configuration screen:

Enter the
                                             				  Database Access Security password. This is the password that servers in the
                                             				  cluster use to communicate with each another. You
                                                					 must enter the same security password for all servers.

Select OK to open the SMTP Host Configuration screen.

Step 5

In the SMTP Host Configuration screen, select whether you want to configure an SMTP host to receive platform-level emails, for example, emails about certificate
                                       expiration. This field is optional. You will configure email for report scheduling in the Administration console.

The Unified Intelligence Center email client does not support SSL/TLS based SMTP servers to email the scheduled Unified Intelligence
                                                      Center reports.

If

Then

You want to configure an SMTP Host.

Select Yes to open the second SMTP screen opens.

Proceed to Step 6.

You do not want to configure an SMTP Host.

Select No to open the Application User Configuration screen.

Proceed to Step 7.

Step 6

In the second SMTP
                                          				Host Configuration screen:

Enter the
                                             				  hostname or IP address for the SMTP server.

Select OK to open the Application User Configuration screen.

Step 7

Complete the Application User Configuration screen. The application user for the Controller becomes
                                       			 the System Application User and the default Super User.

Enter the
                                             				  application username.

Enter and
                                             				  confirm the application user password.

Select OK to open the Platform Configuration Confirmation screen. This
                                             				  screen states that the platform configuration is complete.

Step 8

In the Platform Configuration Confirmation screen, select OK .

Step 9

In
                                       			 the Virtual
                                          				Machine Question message, click Yes and click OK to continue the installation.

| Note | NTP server configuration is
                                       		  mandatory and is set for the first node. Other nodes set their time to the time
                                       		  on the first node. |
|---|---|

| Step 1 | Select Yes at the Network
                                          				Time Protocol Client Configuration screen. The Network Time Protocol Client Configuration screen
                                          				opens. |
|---|---|
| Step 2 | Enter the IP
                                       			 address, NTP server name, or NTP Server Pool name for at least one external NTP
                                       			 server. You can add up
                                          				to five NTP servers and make changes to the NTP server list at a later time. Note You should use a minimum of
                                                   				three external NTP servers. | Note | You should use a minimum of
                                                   				three external NTP servers. |
| Note | You should use a minimum of
                                                   				three external NTP servers. |
| Step 3 | When you
                                       			 complete the NTP configuration, select OK . The Security
                                          				Configuration screen opens. |
| Step 4 | In the Security
                                          				Configuration screen: Enter the
                                             				  Database Access Security password. This is the password that servers in the
                                             				  cluster use to communicate with each another. You
                                                					 must enter the same security password for all servers. Select OK to open the SMTP Host Configuration screen. |
| Step 5 | In the SMTP Host Configuration screen, select whether you want to configure an SMTP host to receive platform-level emails, for example, emails about certificate
                                       expiration. This field is optional. You will configure email for report scheduling in the Administration console. Note The Unified Intelligence Center email client does not support SSL/TLS based SMTP servers to email the scheduled Unified Intelligence
                                                      Center reports. If Then You want to configure an SMTP Host. Select Yes to open the second SMTP screen opens. Proceed to Step 6. You do not want to configure an SMTP Host. Select No to open the Application User Configuration screen. Proceed to Step 7. | Note | The Unified Intelligence Center email client does not support SSL/TLS based SMTP servers to email the scheduled Unified Intelligence
                                                      Center reports. | If | Then | You want to configure an SMTP Host. | Select Yes to open the second SMTP screen opens. Proceed to Step 6. | You do not want to configure an SMTP Host. | Select No to open the Application User Configuration screen. Proceed to Step 7. |
| Note | The Unified Intelligence Center email client does not support SSL/TLS based SMTP servers to email the scheduled Unified Intelligence
                                                      Center reports. |
| If | Then |
| You want to configure an SMTP Host. | Select Yes to open the second SMTP screen opens. Proceed to Step 6. |
| You do not want to configure an SMTP Host. | Select No to open the Application User Configuration screen. Proceed to Step 7. |
| Step 6 | In the second SMTP
                                          				Host Configuration screen: Enter the
                                             				  hostname or IP address for the SMTP server. Select OK to open the Application User Configuration screen. |
| Step 7 | Complete the Application User Configuration screen. The application user for the Controller becomes
                                       			 the System Application User and the default Super User. Note Although it is possible to
                                                   				enter unique Application User credentials on each installed node, you should
                                                   				enter the same Application User Name and password on all nodes.
                                                   				The Application User credentials entered during the Controller installation are
                                                   				the only ones recognized by Unified CCE. Enter the
                                             				  application username. Enter and
                                             				  confirm the application user password. Select OK to open the Platform Configuration Confirmation screen. This
                                             				  screen states that the platform configuration is complete. | Note | Although it is possible to
                                                   				enter unique Application User credentials on each installed node, you should
                                                   				enter the same Application User Name and password on all nodes.
                                                   				The Application User credentials entered during the Controller installation are
                                                   				the only ones recognized by Unified CCE. |
| Note | Although it is possible to
                                                   				enter unique Application User credentials on each installed node, you should
                                                   				enter the same Application User Name and password on all nodes.
                                                   				The Application User credentials entered during the Controller installation are
                                                   				the only ones recognized by Unified CCE. |
| Step 8 | In the Platform Configuration Confirmation screen, select OK . The installation begins.
                                       			 The system displays a Virtual Machine Question message about a locked CD-ROM
                                       			 door. |
| Step 9 | In
                                       			 the Virtual
                                          				Machine Question message, click Yes and click OK to continue the installation. The
                                       			 system displays a reboot message. After the reboot, the system automatically
                                       			 proceeds with the installation. |

| Note | You should use a minimum of
                                                   				three external NTP servers. |
|---|---|

| Note | The Unified Intelligence Center email client does not support SSL/TLS based SMTP servers to email the scheduled Unified Intelligence
                                                      Center reports. |
|---|---|

| If | Then |
|---|---|
| You want to configure an SMTP Host. | Select Yes to open the second SMTP screen opens. Proceed to Step 6. |
| You do not want to configure an SMTP Host. | Select No to open the Application User Configuration screen. Proceed to Step 7. |

| Note | Although it is possible to
                                                   				enter unique Application User credentials on each installed node, you should
                                                   				enter the same Application User Name and password on all nodes.
                                                   				The Application User credentials entered during the Controller installation are
                                                   				the only ones recognized by Unified CCE. |
|---|---|