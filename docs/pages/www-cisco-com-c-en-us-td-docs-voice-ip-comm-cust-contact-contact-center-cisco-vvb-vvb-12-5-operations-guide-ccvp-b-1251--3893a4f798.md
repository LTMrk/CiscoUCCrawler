---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb-12-5-operations-guide-ccvp-b-1251--3893a4f798
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/VVB_12_5/operations/guide/ccvp_b_1251-cvvb-cuc-os-administration-guide/ccvp_b_1251-cvvb-cuc-os-administration-guide_chapter_00.html
retrieved_at: 2026-08-21T16:31:48.382141+00:00
---

Cisco Unified Communications Operating System Administration Guide for Cisco Virtualized Voice Browser, Release 12.5(1)

# Cisco Unified Communications Operating System Administration Guide for Cisco Virtualized Voice Browser, Release 12.5(1)

Updated: February 2, 2020

Chapter: Introduction

## Chapter: Introduction

# Introduction

Cisco Unified Contact Center
                              			 Express (Unified CCX) , a member of
                              			 the Cisco Unified Communications family of products, manages customer voice
                              			 contact centers for departments, branches, or
                           		  small to medium-size companies planning to deploy an entry-level or mid-market contact center solution.

Cisco
                           		  Unified Operating System Administration web interface in Unified CCX allows you to
                           		  configure and manage the Cisco Unified Communications Operating System.

## Overview

For Unified CCX , you can perform many common system
                              		  administration functions through the Cisco Unified Communications Operating
                              		  System. Administration tasks include the following examples:

Check software
                                    				and hardware status.

Check and update
                                    				IP addresses.

Ping other
                                    				network devices.

Manage NTP
                                    				servers.

Upgrade system
                                    				software and options.

Manage server
                                    				security, including IPSec and certificates

Manage remote
                                    				support accounts

Restart the
                                    				system.

The
                              		  following sections describe each operating system function in more detail.

## Browser
                        	 Requirements

You can access Cisco
                              		  Unified Communications Operating System using the following browsers:

Microsoft
                                    				Internet Explorer Version 7.0 or 8.0

Mozilla Firefox
                                    				Version 2.0, 3.0, or 3.5

If you are using
                                          			 Microsoft Internet Explorer Version 7.0 or higher, or Mozilla Firefox Version
                                          			 2.0, 3.0, or 3.5 browser, verify that the popup blocker is disabled.

Ensure the
                              		  URL of the Cisco Unified Communications Operating System server ( https://serverIP )
                              		  is included in the browser "Trusted Site
                                 			 Zone" or the "Local Intranet
                                 			 Site Zone" for all product features to work correctly.

## Operating System Component Status

From the Show menu, you can check the status of various
                              		  operating system components, including:

Cluster and node

Hardware

Network

System

Installed software and options

IP Preferences

## Operating System
                        	 Settings

From the Settings menu, you can view and update the following
                              		  operating system settings:

IP—Updates the
                                    				IP addresses that were entered when the application was installed.

NTP Server
                                    				settings—Configures the IP addresses of an external NTP server; add or delete
                                    				an NTP server.

SMTP
                                    				settings—Configures the SMTP host that the operating system uses to send e-mail
                                    				notifications.

From the Settings > Version window, you can choose from
                              		  the following options for restarting or shutting down the system:

Switch
                                    				Versions—Switches the active and inactive disk partitions and restarts the
                                    				system. You normally choose this option after the inactive partition has been
                                    				updated and you want to start running a newer software version.

Current
                                    				Version—Restarts the system without switching partitions.

Shutdown
                                    				System—Stops all running software and shuts down the server.

This command
                                                				  does not power down the server. To power down the server, press the power
                                                				  button.

## Operating System
                        	 Security Options

Use the
                              		  operating system security options to manage security certificates and Secure
                              		  Internet Protocol (IPSec). From the Security menu, you can choose the following security
                              		  options:

## Application Software Upgrades

Use the software upgrade options to upgrade the
                              		  application software or apply patch files.

From the Install/Upgrade menu option, you can upgrade
                              		  system software from either a local disc or a remote server. The upgraded
                              		  software is installed on the inactive partition, and you can then restart the
                              		  system and switch partitions, so the system starts running on the newer
                              		  software version. 
                              		For more information, see Cisco Unified Contact Center Express Installation and Upgrade guide available here:

http://www.cisco.com/en/US/products/sw/custcosw/ps1846/prod_installation_guides_list.html

## Services

The application provides the following operating system
                              		  utilities:

Ping—Checks connectivity with other network devices.

Remote Support—Configures an account that Cisco support personnel can
                                    				use to access the system. This account automatically expires after the number
                                    				of days that you specify.

## Command Line
                        	 Interface

You can
                              		  access a command-line interface from the console or through a secure shell
                              		  connection to the server.

For more information, see the Command Line Interface Reference Guide for Cisco Unified Contact Center Express and Cisco Unified IP IVR , located at https://www.cisco.com/en/US/products/sw/custcosw/ps1846/prod_installation_guides_list.html and see the Command Line Interface Guide for Cisco Unified Communications Solutions , located at https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html .

| Note | If you are using
                                          			 Microsoft Internet Explorer Version 7.0 or higher, or Mozilla Firefox Version
                                          			 2.0, 3.0, or 3.5 browser, verify that the popup blocker is disabled. |
|---|---|

| Note | This command
                                                				  does not power down the server. To power down the server, press the power
                                                				  button. |
|---|---|

| Type | Description |
|---|---|
| Certificate
                                    			 Management |  | Manages certificates and Certificate Signing Requests (CSR). You
                                    			 can display, upload, download, delete, and regenerate certificates. Through
                                    			 Certificate Management, you can also monitor the expiration dates of the
                                    			 certificates on the server. |
| Certificate
                                    			 Monitor |  | Monitors the certificate expiration. The system can
                                    			 automatically send you an e-mail message when a certificate is close to its
                                    			 expiration date. |
| Certificate
                                    			 Revocation |  | The Online Certificate Status Protocol (OCSP) is used to obtain
                                    			 the revocation status of the certificate. |
| IPSEC
                                    			 Management |  | Displays or updates existing IPSEC policies; sets up new IPSEC
                                    			 policies and associations. |
| Bulk Certificate
                                    			 Management |  | To support the Extension Mobility Cross Cluster (EMCC) feature,
                                    			 the system allows you to execute a bulk import and export operation to and from
                                    			 a common SFTP server that has been configured by the cluster
                                    			 administrator. |
| Single Sign
                                    			 On |  | Manages the Single Sign On configurations of specific
                                    			 applications. |

| Note | You must perform all software installations and upgrades by using the
                                          			 software upgrades features that are included in the Cisco Unified
                                          			 Communications Operating System GUI or command line interface. The system can
                                          			 upload and process only software that Cisco Systems approved. You cannot
                                          			 install or use third-party or Windows-based software applications that you may
                                          			 have been using with a previous version of Unified CCX. |
|---|---|