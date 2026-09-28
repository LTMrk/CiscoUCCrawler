---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-3-op-system-administration-guide-ups1030s-iptpch1-html-eff462c8d9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_3/op_system/administration/guide/ups1030s/iptpch1.html
retrieved_at: 2026-08-21T02:48:07.415132+00:00
---

Cisco Unified Communications Operating System Administration Guide For Cisco Unified Presence Server Release 1.0(3)

# Cisco Unified Communications Operating System Administration Guide For Cisco Unified Presence Server Release 1.0(3)

Updated: February 21, 2007

Chapter: Introduction

## Chapter: Introduction

## Introduction

For Cisco Unified Presence Server  1.0(3), you can perform many common system administration functions through the Cisco Unified Communications Operating System.

This chapter comprises the following topics:

• Overview

• Browser Requirements

• Operating System Status and Configuration

• Restart Options

• Security Configuration

• Software Upgrades

• Services

• Command Line Interface

## Overview

Cisco Unified Communications Operating System Administration allows you to configure and manage the Cisco Unified Communications Operating System by doing these tasks:

• Check software and hardware status.

• Check and update IP addresses.

• Ping other network devices.

• Manage NTP servers.

• Upgrade system software and options.

• Restart the system.

The following sections describe each operating system function in more detail.

## Browser Requirements

You can access Cisco Unified Presence Server Administration, Cisco Unified Presence Server Serviceability, and Cisco Unified Communications Administration by using the following browsers:

• Microsoft Internet Explorer version 6.0 or later

• Netscape Navigator version 7.1 or later

Note Cisco does not support or test other browsers, such as Mozilla Firefox.

## Operating System Status and Configuration

From the Show menu, you can check the status of various operating system components, including

• Cluster and nodes

• Hardware

• Network

• System

• Installed software and options

For more information see Chapter 3, "Platform Status and Configuration."

## Settings

From the Settings menu, you can view and update the following operating system settings:

• Ethernet—Updates the IP addresses and Dynamic Host Configuration Protocol (DHCP) client settings that were entered when the application was installed.

• NTP Server settings—Configures the IP addresses of an external NTP server; add or delete an NTP server.

• SMTP settings—Configures the SMTP host that the operating system will use for sending e-mail notifications.

For more information see Chapter 4, "Settings."

## Restart Options

From the Restart menu , you can choose from the following options for restarting or shutting down the system:

• Switch Versions—Switches the active and inactive disk partitions and restarts the system. You normally choose this option after the inactive partition has been updated and you want to start running a newer software version.

• Current Version—Restarts the system without switching partitions.

• Shutdown System—Stops all running software and shuts down the server.

Note This command does not power down the server. To power down the server, press the power button.

For more information see Chapter 5, "System Restart."

## Security Configuration

The operating system security options enable you to manage security certificates and Secure Internet Protocol (IPSec). From the Security menu, you can choose the following security options:

• Certificate Management—Manages certificates, Certificate Trust Lists (CTL), and Certificate Signing Requests (CSR). You can display, upload, download, delete, and regenerate certificates. Through Certificate Management, you can also monitor the expiration dates of the certificates on the server.

• IPSEC Management—Displays or updates existing IPSEC policies; sets up new IPSEC policies and associations.

For more information, see Chapter 6, "Security."

## Software Upgrades

The software upgrade options enable you to upgrade the software version that is running on the operating system or to install specific software options, including Cisco Unified Presence Server Locale Installers and TFTP server files.

From the Install/Upgrade menu option, you can upgrade system software from either a local disc or a remote server. The upgraded software gets installed on the inactive partition, and you can then restart the system and switch partitions, so the system starts running on the newer software version.

Note For Cisco Unified Presence Server 1.0(3), you must do all software installations and upgrades by using the Software Upgrades menu options. The system can upload and process only software that Cisco Systems approved.

For more information see Chapter 7, "Software Upgrades."

## Services

The application provides the following operating system utilities:

• Ping—Checks connectivity with other network devices.

• Remote Support—Sets up an account that Cisco support personnel can use to access the system. This account automatically expires after the number of days that you specify.

For more information see Chapter 8, "Services."

## Command Line Interface

The command line interface, which you can access from the console or through a secure shell connection to the server, provides a subset of the operating system functionality that is available through the operating system user interface. Keep in mind that the command line interface is designed for system emergencies and not as a replacement for the user interface.

For more information see Appendix A, "Command Line Interface."