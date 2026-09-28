---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-installandupgrade-eec0e96155
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/installandupgrade/guide/ccvp_b_1261-installation-and-upgrade-guide-for-cisco-unified-customer-voice-portal/ccvp_b_1252-installation-and-upgrade-guide-for-cisco-unified-customer-voice-portal_chapter_01.html
retrieved_at: 2026-08-21T17:03:53.932333+00:00
---

Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

# Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

Updated: May 14, 2021

Chapter: Pre-Installation

## Chapter: Pre-Installation

- Pre-Installation

- Pre-Installation Tasks

# Pre-Installation

The Cisco Unified Customer Voice Portal (CVP), Release 12.6(1) is a patch/minor release (MR). Before installing the 12.6(1)
                        MR, the base Unified CVP 12.5(1) version has to be installed.

For more information on installing the base Unified CVP 12.5(1) version, refer to the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.5(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html

Download the MR patch from this location: https://software.cisco.com/download/home/270563413/type/280840592/release/12.6(1) .

## Pre- Installation Tasks

Close all programs.

Stop any third-party services and applications that are running on the server.

Back up C:\Cisco\CVP for all Unified CVP components except Operations Console.

Unified CVP Server log files are saved in <CVP_HOME>\logs ; VXML Server log files are saved in <CVP_HOME>\VXMLServer\logs and <CVP_HOME>\VXMLServer\applications\<app_name>\logs .

Ensure that the servers are listed as supported hardware and sized appropriately. For information on platform hardware specifications
                                 and compatible third party software version requirements, see https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-technical-reference-list.html .

Back up the existing Unified CVP installation files onto a different computer for redundancy in case the automatic backup
                                 fails.

Back up the property files of Unified CVP Server, OAMP, and Reporting Server that need modification. Restore them after upgrade
                                 is complete.

This MR encrypts the keystore password, which is required for exchanging certificates. For detailed steps, refer to the Unified CVP Security section in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Exclude the following folders from on-access scanning configuration of the AV program from all Anti Virus scans:

c:\Cisco , c:\Temp , c:\tmp , c:\db , c:\IFMXDATA

| Note | Unified CVP Server log files are saved in <CVP_HOME>\logs ; VXML Server log files are saved in <CVP_HOME>\VXMLServer\logs and <CVP_HOME>\VXMLServer\applications\<app_name>\logs . |
|---|---|

| Note | Exclude the following folders from on-access scanning configuration of the AV program from all Anti Virus scans: c:\Cisco , c:\Temp , c:\tmp , c:\db , c:\IFMXDATA |
|---|---|