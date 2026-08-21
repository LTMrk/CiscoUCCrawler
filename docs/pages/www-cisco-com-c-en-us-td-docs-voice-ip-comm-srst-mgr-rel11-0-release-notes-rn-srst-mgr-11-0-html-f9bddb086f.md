---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel11-0-release-notes-rn-srst-mgr-11-0-html-f9bddb086f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel11_0/release_notes/rn_srst_mgr_11_0.html
retrieved_at: 2026-08-21T21:29:13.412593+00:00
---

Release Notes for Cisco Unified SRST Manager Release 11.0

# Release Notes for Cisco Unified SRST Manager Release 11.0

- 11.0

- 9.0.7

### Download Options

Updated: December 3, 2015

## Table of Contents

Release Notes for Cisco Unified SRST Manager Release 11.0

System Requirements

Specifications-Based Platforms

System Requirements

VMware Feature Support

Tested Reference Configuration Platforms

Hardware Supported by Cisco Unified SRST Manager Release 11.0

Compatibility Matrix

File Package (OVA Download)

New Features and Enhancements

Release 11.0

Release 11.0.1

Release 11.0.2

Licensing

Limitations

Release 11.0

Release 11.0.1

Release 11.0.2

Caveats

Caveats in Cisco Unified SRST Manager 11.0

Caveats in Cisco Unified SRST Manager 11.0.1

Caveats in Cisco Unified SRST Manager 11.0.2

Additional References

Obtaining Documentation and Submitting a Service Request

First Published: August 17, 2015 Last Updated: May 18, 2017

This release notes document supports Cisco Unified SRST Manager Release 11.0.x. Table 1 describes the history of Cisco Unified SRST Manager Release 11.0.x.

Table 1 Cisco Unified SRST Manager Release 11.0.x History

Cisco Unified SRST Manager Version

Release Date

11.0.2

May 18, 2017

11.0.1

December 3, 2015

11.0

August 17, 2015

This Release Note document contains the following sections:

## System Requirements

Cisco Unified SRST Manager Release 11.0.x operates within a VMWare Elastic Sky X (ESXi) environment. The software is packaged as an Open Virtual Appliance (OVA) template for installation within the ESXi environment (4.1, 5.0, 5.1 and 5.5). To learn more about Unified Communications in a virtualized environment, see Unified Communications in a Virtualized Environment .

This section contains the following information:

Specifications-Based Platforms

### Specifications-Based Platforms

### System Requirements

See Table 2 for specifications-based information pertaining to server hardware and VMware feature requirements for operating Cisco Unified SRST Manager.

Table 2 Specifications–Based Server System Requirements

For Information On...

See...

Hardware requirements

http://docwiki.cisco.com/wiki/Specification-Based_Hardware_Support

VMware feature system requirements

http://docwiki.cisco.com/wiki/Implementing_Virtualization_Deployments#Configuring_Hardware_Platforms

### VMware Feature Support

Cisco Unified SRST Manager requires VMware ESXi 4.1, 5.0, 5.1 and 5.5.

Additional feature support information is available at:

http://docwiki.cisco.com/wiki/Implementing_Virtualization_Deployments#VMware_Feature_Support

### Tested Reference Configuration Platforms

This section provides information about tested reference configuration platforms. For extensive information about tested reference configurations (TRC), including details about specific server models, see: http://docwiki.cisco.com/wiki/Tested_Reference_Configurations_TRC

### Hardware Supported by Cisco Unified SRST Manager Release 11.0

The following tested reference configurations are supported by Cisco Unified SRST Manager Release 11.0:

- Cisco UCS B-Series Blade Servers

- Cisco UCS C260 M2 Rack-Mount Server Tested Reference Configuration 1

- Cisco UCS C210 Rack-Mount Servers

- Cisco UCS C200 Rack-Mount Servers

For detailed information on supported tested reference configurations, see the Installation and Upgrade Guide for Cisco Unified SRST Manager .

### Compatibility Matrix

For information about the Cisco Unified SRST Manager Release 11.0 compatibility matrix, see:

http://docwiki.cisco.com/wiki/Cisco_Unified_SRST_Manager_Compatibility_Matrix

### File Package (OVA Download)

Cisco Unified SRST Manager Release 11.0.x is packaged as an OVA template for installation within the ESXi environment (4.1, 5.0, 5.1 and 5.5). To simplify the installation process, the OVA file includes the following:

- Virtual machine system settings preconfigured for Cisco Unified SRST Manager

- Cisco Unified SRST Manager software

The file package is available for download at:

http://www.cisco.com/en/US/partner/products/sw/voicesw/ps2169/index.html

For more information on downloading the OVA file package, see the Installation and Upgrade Guide for Cisco Unified SRST Manager .

## New Features and Enhancements

### Release 11.0

This section describes the new features and enhancements in Cisco Unified SRST Manager Release 11.0.x:

- Configuration Changes

Users can view the list of CLI which are pushed to the router between the latest two successful provisioning and also view the complete list of CLI s that were pushed to Cisco Unified SRST Manager at any point of time. For more information, refer to Administration Guide for Cisco Unified SRST Manager.

- Rollback

In case of a provisioning failure, Cisco Unified SRST Manager restores the router back to the original configuration state by removing all the new CLI that were added before the failure. For more information, refer to Administration Guide for Cisco Unified SRST Manager.

- Intelligent Provisioning

Cisco Unified SRST Manager triggers the provisioning only after checking the need for provisioning. For more information, refer to Administration Guide for Cisco Unified SRST Manager.

- ESRST Scalability

From Cisco Unified SRST Manager Release 11.0 onwards, the scale of ESRST mode has increased to match the scale of Classic SRST for both SIP and SCCP Phones. For more information, refer to Cisco Unified Survivable Remote Site Telephony and Cisco Unified Enhanced Survivable Remote Site Telephony Data Sheet .

- Alert Changes

Debug-ability is enhancement by making error messages more meaningful and intuitive. For more information, refer to Administration Guide for Cisco Unified SRST Manager.

- DNS Enhancement

Entering the DNS server details is made optional from Cisco Unified SRST Manager Release 11.0. For more information, refer to Administration Guide for Cisco Unified SRST Manager.

- User Management

One Cisco Unified SRST Manager can have multiple users. For more information, refer to Administration Guide for Cisco Unified SRST Manager.

- Fast Track Support

Fast track is supported from Cisco Unified SRST Manager 11.0 onwards for SIP phones in ESRST mode only. For more information, refer to Cisco Unified SRST Manager Compatibility Matrix .

- Jabber CSF Client Support

Provides support for Cisco Jabber - Client Services Framework (CSF) Client. For more information, refer to Cisco Unified SRST Manager Compatibility Matrix .

- Scheduling

From Cisco Unified SRST Manager 11.0 onwards, scheduled provisioning is optional. For more information, refer to Administration Guide for Cisco Unified SRST Manager.

- New Platform Support

Cisco Unified SRST Manager 11.0 supports five new platforms. For more information on the platforms supported, refer to Cisco Unified SRST Manager Compatibility Matrix .

### Release 11.0.1

There are no new features and enhancements in Release 11.0.1.

### Release 11.0.2

There are no new features and enhancements in Release 11.0.2.

## Licensing

Cisco Unified SRST Manager is licensed software, that is provided without charge to Cisco customers, for use in the Enhanced Survivable Remote Site Telephony (E-SRST) solution. Installation requires acceptance of the terms of the license.

## Limitations

### Release 11.0

For information about Cisco Unified SRST Manager limitations, see:

http://www.cisco.com/en/US/partner/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/overview.html

### Release 11.0.1

There are no new limitations in Cisco Unified SRST Release 11.0.1.

### Release 11.0.2

There are no new limitations in Cisco Unified SRST Release 11.0.2.

## Caveats

Caveats describe unexpected behavior in Cisco Unified SRST Manager Release 11.0.x. Severity 1 caveats are the most serious caveats. Severity 2 caveats are less serious. Severity 3 caveats are moderate caveats, and only selected severity 3 caveats are included in the caveats document.

### Caveats in Cisco Unified SRST Manager 11.0

The following issues were resolved in Cisco Unified SRST Manager Release11.0.

Table 3 Resolved Caveats in Cisco Unified SRST Manager Release 11.0

Bug ID

Summary

CSCur13595

Cisco Unified SRST Manager fails to provision phones with special characters in Username.

CSCur90899

Cisco Unified SRST Manager release 11.0 supports voicemail for SIP Phones.

CSCus18855

Cisco Unified SRST Manager fails to configure SNR time delay.

CSCus56685

Cisco Unified SRST provisioning fails while executing CLI command on ID network.

CSCUs94998

Cisco Unified SRST Manager fails to provision dissociation CLIs when softkey template is deleted from phones registered on Unified Communications Manager.

CSCus18806

Cisco Unified SRST Manager phone template issues and IOS release number correction.

### Caveats in Cisco Unified SRST Manager 11.0.1

The following issues were resolved in Cisco Unified SRST Manager 11.0.1.

Table 4 Resolved Caveats in Cisco Unified SRST Manager Release 11.0.1

Bug ID

Summary

CSCuv99960

Incorporate flash validation changes in Unified SRST Manager

CSCuw92657

Unified SRST manager fails to provision Unified 88XX Series phones that have BEKEM modules

### Caveats in Cisco Unified SRST Manager 11.0.2

The following issues were resolved in Cisco Unified SRST Manager 11.0.2.

Table 5 Resolved Caveats in Cisco Unified SRST Manager Release 11.0.2

Bug ID

Summary

CSCve28314

SRST Manager tries to configure fast track in CME-SRST 11 although the phone type is supported

CSCvd67787

SRST manager configures the expansion module as a 7915 instead of a 7916

CSCvc35210

SRST Manager provisioning fails throwing NulllPointerException

CSCvc12158

SRST Manager Site Provisioning Unsuccessful

CSCuz80882

SRST Manager - Unable to create phone softkey template for site

CSCuz75540

SRST manager - provisioning fails while configuring ephone-dn name cli

CSCuw92657

SRST manager failing to provision 88XX phones that have BEKEM modules

CSCvb27900

SRST manager will not boot, shows error stating "no space left on disk"

CSCux68042

SRST manager 9.0.7 provisioning for gateway fails with CUCM 10.0.1.10000

## Additional References

Table 6 lists the related documentation available for Cisco Unified SRST Manager Release 11.0.

Table 6 Cisco Unified SRST Manager Release 11.0 Documentation

Documentation

Title

Installation and Upgrade Guide for Cisco Unified SRST Manager

Contains information about installing Cisco Unified SRST Manager Release 11.0.

Administration Guide for Cisco Unified SRST Manager

Contains administrator information for Cisco Unified SRST Manager Release 11.0. Includes information about the following:

- Tasks that are performed from the GUI, including online help

- Tasks that are performed from the CLI

- CLI command information for commands that are specific to Cisco Unified SRST Manager Release 11.0.

- Maintenance

Cisco Unified SRST Manager Compatibility Matrix

Describes the software and platforms compatible with Cisco Unified SRST Manager.

## Obtaining Documentation and Submitting a Service Request

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http://www.cisco.com/en/US/docs/general/whatsnew/whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)

### Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)

### Copyright © 2017, Cisco Systems, Inc. All rights reserved.

### This Document Applies to These Products

- Unified Survivable Remote Site Telephony

| Cisco Unified SRST Manager Version | Release Date |
|---|---|
| 11.0.2 | May 18, 2017 |
| 11.0.1 | December 3, 2015 |
| 11.0 | August 17, 2015 |

| For Information On... | See... |
|---|---|
| Hardware requirements | http://docwiki.cisco.com/wiki/Specification-Based_Hardware_Support |
| VMware feature system requirements | http://docwiki.cisco.com/wiki/Implementing_Virtualization_Deployments#Configuring_Hardware_Platforms |

| Bug ID | Summary |
|---|---|
| CSCur13595 | Cisco Unified SRST Manager fails to provision phones with special characters in Username. |
| CSCur90899 | Cisco Unified SRST Manager release 11.0 supports voicemail for SIP Phones. |
| CSCus18855 | Cisco Unified SRST Manager fails to configure SNR time delay. |
| CSCus56685 | Cisco Unified SRST provisioning fails while executing CLI command on ID network. |
| CSCUs94998 | Cisco Unified SRST Manager fails to provision dissociation CLIs when softkey template is deleted from phones registered on Unified Communications Manager. |
| CSCus18806 | Cisco Unified SRST Manager phone template issues and IOS release number correction. |

| Bug ID | Summary |
|---|---|
| CSCuv99960 | Incorporate flash validation changes in Unified SRST Manager |
| CSCuw92657 | Unified SRST manager fails to provision Unified 88XX Series phones that have BEKEM modules |

| Bug ID | Summary |
|---|---|
| CSCve28314 | SRST Manager tries to configure fast track in CME-SRST 11 although the phone type is supported |
| CSCvd67787 | SRST manager configures the expansion module as a 7915 instead of a 7916 |
| CSCvc35210 | SRST Manager provisioning fails throwing NulllPointerException |
| CSCvc12158 | SRST Manager Site Provisioning Unsuccessful |
| CSCuz80882 | SRST Manager - Unable to create phone softkey template for site |
| CSCuz75540 | SRST manager - provisioning fails while configuring ephone-dn name cli |
| CSCuw92657 | SRST manager failing to provision 88XX phones that have BEKEM modules |
| CSCvb27900 | SRST manager will not boot, shows error stating "no space left on disk" |
| CSCux68042 | SRST manager 9.0.7 provisioning for gateway fails with CUCM 10.0.1.10000 |

| Documentation | Title |
|---|---|
| Installation and Upgrade Guide for Cisco Unified SRST Manager | Contains information about installing Cisco Unified SRST Manager Release 11.0. |
| Administration Guide for Cisco Unified SRST Manager | Contains administrator information for Cisco Unified SRST Manager Release 11.0. Includes information about the following: Tasks that are performed from the GUI, including online help Tasks that are performed from the CLI CLI command information for commands that are specific to Cisco Unified SRST Manager Release 11.0. Maintenance |
| Cisco Unified SRST Manager Compatibility Matrix | Describes the software and platforms compatible with Cisco Unified SRST Manager. |