---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-english-operating-system-guide-1-0-1-iptpch1-html-d5f7c5345b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0/english/operating_system/guide/1_0_1/iptpch1.html
retrieved_at: 2026-08-21T02:45:01.833092+00:00
---

Cisco Unified Communications Operating System Administration Guide, Release 1.0(1)

# Cisco Unified Communications Operating System Administration Guide, Release 1.0(1)

Updated: July 17, 2006

Chapter: Introduction

## Chapter: Introduction

## Introduction

For Cisco Unified Presence Server 1.0(1), you can perform many common system administration functions through the Cisco Unified Communications Operating System.

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

## Settings

From the Settings menu, you can view and update the following operating system settings:

• Ethernet—Updates the IP addresses and Dynamic Host Configuration Protocol (DHCP) settings that were entered when the application was installed.

• NTP Server settings—Configures the IP addresses of an external NTP server; add or delete an NTP server.

• SMTP settings—Configures the SMTP host that the operating system will use for sending e-mail notifications.

## Restart Options

From the Restart menu , you can choose from the following options for restarting or shutting down the system:

• Switch Versions—Switches the active and inactive disk partitions and restarts the system. You normally choose this option after the inactive partition has been updated and you want to start running a newer software version.

• Current Version—Restarts the system without switching partitions.

• Shutdown System—Stops all running software and shuts down the server.

## Security Configuration

The operating system security options enable you to manage security certificates and Secure Internet Protocol (IPSec). From the Security menu, you can choose the following security options:

• Certificate Management—Manages certificates, Certificate Trust Lists (CTL), and Certificate Signing Requests (CSR). You can display, upload, download, delete, and regenerate certificates. Through Certificate Management, you can also monitor the expiration dates of the certificates on the server.

• IPSEC Management—Displays or updates existing IPSEC policies; sets up new IPSEC policies and associations.

## Software Upgrades

The software upgrade options enable you to upgrade the software version that is running on the operating system or to install specific software options, including Cisco Unified Presence Server Locale Installers, dial plans, and TFTP server files.

From the Install/Upgrade menu option, you can upgrade system software from either a local disc or a remote server. The upgraded software gets installed on the inactive partition, and you can then restart the system and switch partitions, so the system starts running on the newer software version.

## Services

The application provides the following operating system utilities:

• Ping—Checks connectivity with other network devices.

• Remote Support—Sets up an account that Cisco support personnel can use to access the system. This account automatically expires after the number of days that you specify.

## Command Line Interface

The command line interface, which you can access from the console or through a secure shell connection to the server, provides a subset of the operating system functionality that is available through the operating system user interface. Keep in mind that the command line interface is designed for system emergencies and not as a replacement for the user interface.