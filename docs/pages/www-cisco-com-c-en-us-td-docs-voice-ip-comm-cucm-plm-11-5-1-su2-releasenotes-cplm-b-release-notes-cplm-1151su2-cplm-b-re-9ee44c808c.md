---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-11-5-1-su2-releasenotes-cplm-b-release-notes-cplm-1151su2-cplm-b-re-9ee44c808c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/11_5_1_SU2/releasenotes/cplm_b_release-notes-cplm-1151su2/cplm_b_release-notes-cplm-1151su2_chapter_01.html
retrieved_at: 2026-08-20T22:35:48.996558+00:00
---

Release Notes for Cisco Prime License Manager, Release 11.5(1)SU2

# Release Notes for Cisco Prime License Manager, Release 11.5(1)SU2

## Results

Updated: March 22, 2018

Chapter: New and Changed Information

## Chapter: New and Changed Information

# New and Changed Information

## Encryption
                        	 License

With this release, Cisco Prime License Manager supports the encryption license which enables the higher levels of the product encryption for the registered products. Some
                              newer Cisco products, such as Cisco Unified Communications Manager Release 11.5(1)SU3, and Cisco Unity Connection, Release 11.5(1)SU3 require an encryption license to run the product in mixed
                              mode.

Procure the
                              		  encryption license along with the PAK and install it. For more details on
                              		  buying the licenses, see the Ordering Guide at http://www.cisco.com/c/en/us/partners/tools/collaboration-ordering-guides.html .

For more details on encryption fulfillment, see "License Management" chapter of the Cisco Prime License Manager User Guide at http://www.cisco.com/c/en/us/support/cloud-systems-management/prime-license-manager/products-user-guide-list.html .

## Privilege Level
                        	 Updates for CLI Commands

With this release, the command privilege level for the following two
                              		  CLI commands has changed from 0 to 1. Only users with a minimum privilege level
                              		  of 1 have access to run either of these commands:

license management set log level core_services

license management set log level
                                       				  product_instances

For more information about the license management set log level commands, see the "Cisco Prime License Manager CLI Commands" chapter of the Cisco Prime License Manager User Guide at http://www.cisco.com/c/en/us/support/cloud-systems-management/prime-license-manager/products-user-guide-list.html .

## RC4
                        	 Ciphers

With this release, Cisco Prime License Manager does not support RC4
                              		  Ciphers and they are arcfour256, arcfour128, and arcfour.

## Set Minimum TLS
                        	 Version

With this release, Cisco
                                 			 Prime License Manager supports the configuration of a minimum
                              		  Transport Layer Security (TLS) version. For example, you can set your system to
                              		  support TLS 1.2, this would ensure a secure connection for Cisco
                                 			 Prime License Manager and it accepts TLS 1.2 connections only.

The supported TLS
                              		  versions are TLS 1.0, 1.1, and 1.2 with version 1.0 as the default minimum
                              		  supported version. After you reconfigure the minimum TLS version, TLS versions
                              		  that are the same as, or higher than, the TLS minimum are supported.

Enter the command set tls min-version tlsversion to set the minimum version of TLS that is
                              		  supported by the system. You can use, the command show tls min-version to view the minimum configured
                              		  version of TLS.

For more
                              		  information about the minimum TLS version commands, see the "Set Commands" chapter and the " Show
                                 			 Commands" chapter of the Command Line
                                 			 Interface Reference Guide for Cisco Unified Communications Solutions at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .