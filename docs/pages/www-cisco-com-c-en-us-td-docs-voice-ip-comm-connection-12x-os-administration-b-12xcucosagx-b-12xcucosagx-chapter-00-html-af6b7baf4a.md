---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-os-administration-b-12xcucosagx-b-12xcucosagx-chapter-00-html-af6b7baf4a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/os_administration/b_12xcucosagx/b_12xcucosagx_chapter_00.html
retrieved_at: 2026-08-17T03:39:52.502660+00:00
---

Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 12.x

# Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 12.x

Updated: August 4, 2017

Chapter: Introduction

## Chapter: Introduction

# Introduction

For Cisco Unified Communications Manager and Cisco Unity
                        		Connection, you can perform many common system administration functions through
                        		the Cisco Unified Communications Operating System.

## Overview

Cisco Unified Communications Operating System Administration
                           		allows you to configure and manage the Cisco Unified Communications Operating
                           		System. Administration tasks include the following examples:

Check software and hardware status.

Check and update IP addresses.

Ping other network devices.

Manage NTP servers.

Upgrade system software and options.

Manage server security, including IPSec and certificates

Manage remote support accounts

Restart the system.

The following sections describe each operating system function
                           		in more detail.

## Browser Requirements

You can access Cisco Unified Communications Operating System with the following browsers:

You can access Cisco Unified Communications Operating System with this browser...

...if you use one of these operating systems

Microsoft Internet Explorer 8

Microsoft XP service pack 3

Microsoft Vista service pack 2 or later service pack

Microsoft Windows 7 with the latest service pack

Mozilla Firefox 3.x

Microsoft XP service pack 3

Microsoft Vista service pack 2 or later service pack

Microsoft Windows 7 with the latest service pack

Apple MAC OS X with the latest service pack

Safari 4.x

Apple MAC OS X

Ensure the URL of the Cisco Unified Communications Operating System server ( https:// servername ) is included in the browser “Trusted Site Zone” or the “Local Intranet Site Zone” for all product features to work correctly.

## Operating System
                        	 Status and Configuration

From the Show menu, you can check the status of various operating system
                           		components, including

Cluster and nodes

Hardware

Network

System

Installed software and options

For more information, see “ Status
                              		  and Configuration ”

## Settings

From the Settings menu, you can view and update the following
                           		operating system settings:

IP—Updates the IP addresses and Dynamic Host Configuration
                                 			 Protocol (DHCP) client settings that were entered when the application was
                                 			 installed.

NTP Server settings—Configures the IP addresses of an external
                                 			 NTP server; add or delete an NTP server.

SMTP settings—Configures the SMTP host that the operating system
                                 			 use for sending e-mail notifications.

For more information, see “ Settings ”

From the Settings > Version window , you can select from the following options for restarting or shutting
                           		down the system:

Switch Versions—Switches the active and inactive disk partitions
                                 			 and restarts the system. You normally select this option after the inactive
                                 			 partition has been updated and you want to start running a newer software
                                 			 version.

Current Version—Restarts the system without switching
                                 			 partitions.

Shutdown System—Stops all running software and shuts down the
                                 			 server.

This command does not power down the server. To power down the
                                             				server, press the power button.

For more information see Chapter “ Version
                              		  Settings ”.

## Security
                        	 Configuration

The operating system security options enable you to manage
                           		security certificates and Secure Internet Protocol (IPSec). From the Security menu, you can select the following security
                           		options:

Certificate Management—Manages certificates, Certificate Trust
                                 			 Lists (CTL), and Certificate Signing Requests (CSR). You can display, upload,
                                 			 download, delete, and regenerate certificates. Through Certificate Management,
                                 			 you can also monitor the expiration dates of the certificates on the server.

IPSEC Management—Displays or updates existing IPSEC policies;
                                 			 sets up new IPSEC policies and associations.

For more information, see Chapter  “ Security ”.

## Software
                        	 Upgrades

The software upgrade options enable you to upgrade the software
                           		version that is running on the operating system or to install specific software
                           		options, including Cisco Unified Communications Operating System Locale
                           		Installers, dial plans, and TFTP server files.

From the Install/Upgrade menu option, you can upgrade system software from either a local disc
                           		or a remote server. The upgraded software gets installed on the inactive
                           		partition, and you can then restart the system and switch partitions, so the
                           		system starts running on the newer software version.

For more information, see Chapter “ Software
                              		  Upgrades ”.

The application provides the following operating system
                           		utilities:

Ping—Checks connectivity with other network devices.

Remote Support—Sets up an account that Cisco support personnel
                                 			 can use to access the system. This account automatically expires after the
                                 			 number of days that you specify.

For more information, see Chapter “ Services ”.

## Command Line Interface

You can access a command line interface from the console or through a secure shell connection to the server. For more information,
                           refer to the Command Line Interface Reference Guide for Cisco Unifed Communications Solutions.

| You can access Cisco Unified Communications Operating System with this browser... | ...if you use one of these operating systems |
|---|---|
| Microsoft Internet Explorer 8 | Microsoft XP service pack 3 Microsoft Vista service pack 2 or later service pack Microsoft Windows 7 with the latest service pack |
| Mozilla Firefox 3.x | Microsoft XP service pack 3 Microsoft Vista service pack 2 or later service pack Microsoft Windows 7 with the latest service pack Apple MAC OS X with the latest service pack |
| Safari 4.x | Apple MAC OS X |

| Note | This command does not power down the server. To power down the
                                             				server, press the power button. |
|---|---|

| Note | You
                                    		must do all software installations and upgrades with the software upgrades
                                    		features that are included in the Cisco Unified Communications Operating System
                                    		GUI and command line interface. The system can upload and process only software
                                    		that Cisco Systems approved. You cannot install or use third-party or
                                    		Windows-based software applications that you may have been using with a
                                    		previous version of Cisco Unified Communications Manager. |
|---|---|