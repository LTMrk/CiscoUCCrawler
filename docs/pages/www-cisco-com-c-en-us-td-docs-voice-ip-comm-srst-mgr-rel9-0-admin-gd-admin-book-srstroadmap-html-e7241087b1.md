---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-srstroadmap-html-e7241087b1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/srstroadmap.html
retrieved_at: 2026-08-21T23:37:35.650523+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 10, 2014

Chapter: Cisco Unified SRST Manager Roadmap

## Chapter: Cisco Unified SRST Manager Roadmap

# Feature History

This section lists the features documented in the Cisco Unified SRST Manager Administration Guide and maps them to the modules in which they appear.

Note Cisco Unified Survivable Remote Site Telephony (SRST) Manager is End-of-Life (EOL). Hence, provisioning for Unified E-SRST through Unified SRST Manager is not supported for Unified E-SRST Release 12.2 and later releases. For more information, see Migration from Unified SRST Manager to Unified E-SRST .

Feature and Release Support

Table -1 lists the Cisco Unified Survivable Remote Site Telephony (SRST) Manager version that introduced support for a given feature. Unless noted otherwise, subsequent versions of Cisco Unified SRST Manager supports that feature. The features that were introduced or modified in Cisco Unified SRST Manager 9.0.6 and later appear in the table.

Note Not all features may be supported in your Cisco Unified SRST Manager version.

To determine the correct Cisco Unified Communications Manager version and Cisco Unified Survivable Remote Site Telephony (SRST/ESRST) release that supports a specific Cisco Unified SRST Manager version, see the Cisco Unified SRST Manager Compatibility Matrix at: http://docwiki.cisco.com/wiki/Cisco_Unified_SRST_Manager_Compatibility_Matrix

Table -1 Supported Cisco Unified SRST Manager Features

11.0

Configuration Changes

Users can view the list of CLIs that are pushed to router by Cisco Unified SRST Manager.

Viewing Configuration Changes

AXL Upgrade

Administrative XML (AXL) support is upgraded to 9.0 from Cisco Unified SRST Manager 11.0 onwards.

Supported Phones and Platforms

Rollback

In case of a provisioning failure, the Cisco Unified SRST Manager restores the router back to the original configuration state by removing all the new CLIs that were added before the failure.

Changing the Information for a Single Cisco Unified SRST Site

Intelligent Provisioning

The Cisco Unified SRST Manager triggers provisioning if there are configuration changes from the last successful provisioning.

About Scheduled Provisioning

ESRST Scalability

From Cisco Unified SRST Manager Release 11.0 onwards, the scale of Enhanced SRST (ESRST) mode is increased to match the scale of classic SRST for both Session Initiation Protocol (SIP) and Signaling Connection Control Protocol (SCCP) phones.

Cisco Unified Survivable Remote Site Telephony and Cisco Unified Enhanced Survivable Remote Site Telephony Version 11.0 Data Sheet

New Phone Support

Cisco Unified SRST Manager Release 11.0 supports new phone models.

Cisco Unified SRST Manager Compatibility Matrix

Alert Enhancement

Error messages are made more meaningful to enhance the debug ability.

System Alerts

DNS Enhancement

Entering the DNS server details is optional while configuring Cisco Unified Communications Manager from Cisco Unified SRST Manager.

Using the Central Call Agent Wizard to Add Cisco Unified Communications Manager Information

User Management

Enables Cisco Unified SRST Manager with multiple user support.

Configuring Users for Cisco Unified SRST Manager

Fast Track Support

Fast track is supported from Cisco Unified SRST Manager 11.0 onwards for SIP phones in ESRST mode.

Cisco Unified SRST Manager Compatibility Matrix

Jabber CSF Client Support

Support is provided for Cisco Jabber - Client Services Framework (CSF) Client.

Cisco Unified SRST Manager Compatibility Matrix

Scheduling

From Cisco Unified SRST Manager 11.0 onwards, scheduled provisioning is optional.

Using the Central Call Agent Wizard to Add Cisco Unified Communications Manager Information

New Platform Support

Cisco Unified SRST Manager 11.0 supports five new platforms.

Cisco Unified SRST Manager Compatibility Matrix

ESXi 5.1 and ESXi 5.5 Support

Cisco Unified SRST Manager 11.0 supports ESXi 5.1 and ESXi 5.5.

Cisco Unified SRST Manager Overview

9.0.6

No Dial Plan Support

Dial Plan is not supported from Cisco Unified SRST Manager 9.0.6. A note has been added in the applicable sections.

Cisco Unified SRST Manager Overview

AXL Upgrade

Administrative XML (AXL) support is upgraded to 8.5 from Cisco Unified SRST Manager 9.0.6 onwards.

Supported Phones and Platforms

| Version | Feature Name | Feature Description | Documented In |
|---|---|---|---|
| 11.0 | Configuration Changes | Users can view the list of CLIs that are pushed to router by Cisco Unified SRST Manager. | Viewing Configuration Changes |
| AXL Upgrade | Administrative XML (AXL) support is upgraded to 9.0 from Cisco Unified SRST Manager 11.0 onwards. | Supported Phones and Platforms |
| Rollback | In case of a provisioning failure, the Cisco Unified SRST Manager restores the router back to the original configuration state by removing all the new CLIs that were added before the failure. | Changing the Information for a Single Cisco Unified SRST Site |
| Intelligent Provisioning | The Cisco Unified SRST Manager triggers provisioning if there are configuration changes from the last successful provisioning. | About Scheduled Provisioning |
| ESRST Scalability | From Cisco Unified SRST Manager Release 11.0 onwards, the scale of Enhanced SRST (ESRST) mode is increased to match the scale of classic SRST for both Session Initiation Protocol (SIP) and Signaling Connection Control Protocol (SCCP) phones. | Cisco Unified Survivable Remote Site Telephony and Cisco Unified Enhanced Survivable Remote Site Telephony Version 11.0 Data Sheet |
| New Phone Support | Cisco Unified SRST Manager Release 11.0 supports new phone models. | Cisco Unified SRST Manager Compatibility Matrix |
| Alert Enhancement | Error messages are made more meaningful to enhance the debug ability. | System Alerts |
| DNS Enhancement | Entering the DNS server details is optional while configuring Cisco Unified Communications Manager from Cisco Unified SRST Manager. | Using the Central Call Agent Wizard to Add Cisco Unified Communications Manager Information |
| User Management | Enables Cisco Unified SRST Manager with multiple user support. | Configuring Users for Cisco Unified SRST Manager |
| Fast Track Support | Fast track is supported from Cisco Unified SRST Manager 11.0 onwards for SIP phones in ESRST mode. | Cisco Unified SRST Manager Compatibility Matrix |
| Jabber CSF Client Support | Support is provided for Cisco Jabber - Client Services Framework (CSF) Client. | Cisco Unified SRST Manager Compatibility Matrix |
| Scheduling | From Cisco Unified SRST Manager 11.0 onwards, scheduled provisioning is optional. | Using the Central Call Agent Wizard to Add Cisco Unified Communications Manager Information |
| New Platform Support | Cisco Unified SRST Manager 11.0 supports five new platforms. | Cisco Unified SRST Manager Compatibility Matrix |
| ESXi 5.1 and ESXi 5.5 Support | Cisco Unified SRST Manager 11.0 supports ESXi 5.1 and ESXi 5.5. | Cisco Unified SRST Manager Overview |
| 9.0.6 | No Dial Plan Support | Dial Plan is not supported from Cisco Unified SRST Manager 9.0.6. A note has been added in the applicable sections. | Cisco Unified SRST Manager Overview |
| AXL Upgrade | Administrative XML (AXL) support is upgraded to 8.5 from Cisco Unified SRST Manager 9.0.6 onwards. | Supported Phones and Platforms |