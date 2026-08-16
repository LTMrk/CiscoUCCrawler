---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-documentation-guide-uccx--415d77f9aa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/documentation/guide/uccx_b_1251su1documentation-guide.html
retrieved_at: 2026-08-16T15:03:56.864596+00:00
---

Cisco Unified Contact Center Express Documentation Guide, Release 12.5(1) SU1

# Cisco Unified Contact Center Express Documentation Guide, Release 12.5(1) SU1

### Download Options

Updated: January 31, 2021

First Published: January 31, 2021

This documentation guide provides details of all the documents for this release of Unified Contact Center Express (Unified
               CCX), Release 12.5(1) SU1 and contains links to the documents.

For the latest version of all of the documents of Unified CCX, see:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/tsd-products-support-series-home.html .

## Document Changes

The following tables identify the documents that changed for this release.

New Solution Documents in This Release

There are no new solution documents in this release.

New Documents in This Release

There are no new Unified CCX documents in this release.

Documents Updated in This Release

The following table lists the documents that are updated for this release.

Document

Notes

Cisco Unified Contact Center Express Administration and Operations Guide

Updates to this document are as follows:

Removed the commands, set cuic trace and show cuic trace

Included Syslog Support for Critical Cisco Finesse Log Messages

Removed the Cisco Finesse Trace Logging section

Added Finesse Log Configuration, Connected Agents, and Multi-Tab Gadget

The procedure to set up certificates in Chrome has been updated with Edge Chromium

Added the command set cuic properties report-query-timeout

Updated SRTP with the information related to RmCm provider user

Added information related to Data Check and Data Resync when SRTP is selected

Added information related to data synchronization

Added info about restoring from a backup when SRTP is enabled and disabled

Introduced setting of webapp session timeout

Added the commands show webapp session timeout , show cli session timeout , set webapp session maxlimit , and set webapp session timeout

Updated Agent ID details to support 64 characters

Added a note about secure JTAPI connection for the SRTP field

Added information about custom logon message

Removed Cisco Unified Intelligence Center Services and added a note about CUIC CLI

Added the commands utils cuic logging list , utils cuic logging config set , utils cuic logging update , utils cuic logging config show , utils cuic logging reset, utils cuic logging config clear, utils cuic session list, and utils cuic session delete

Updated the description of Authorization Status and Status fields with Added Authorized - Reserved and Not Authorized - Reserved

Added the fields Reserved Count , License Control , Current License Type , Overage Allowance , and I have purchased High Availability License Smart License Management

Added a new topic Utils FIPS to mention the points to be considered before enabling FIPS

Added the new alerts EmailOAuthConnectionFailed and EmailAuthenticationFailed in Unified CCX Alerts

Added the new fields Authentication Type and Private Key in Contact Service Queues

Added a note for Email password field in Contact Service Queues

Added information about accessibility support for visually challenged

Updated Localize Accessibility Messages

Added a new topic to list Specific License Reservation commands

Added the new field HTTP in Mail Server Configuration

Included Agent Device Selection

Included Auto Answer

Cisco Unified Contact Center Express Developer Guide

Updates to this document are as follows:

Added new attributes emailAuthType and emailOAuthDetails

Added information about emailAuthType for accountPassword attribute

Added a new attribute useHttpProxy

Added new elements emailAuthType , emailOAuthDetails , and useHttpProxy

Cisco Unified Contact Center Express CTI Protocol Developer Guide

Updates to this document are as follows:

Updated the maximum supported CTI Protocol version to 18

Updated the configuration mask with Terminal Information

Introduced a new event as part of Agent Device Selection

Updated the message with new field ActiveTerminal

Introduced a new field ConfigMsgMaskGranted

Updated the FieldDataID field is 2 bytes

Updated FieldDataID values 302 -305 for Agent Device Selection

New error code CCX_ACTIVE_TERMINAL_NOT_SPECIFIED for Agent Device Selection

The Maximum size of the Agent ID field is updated to 129

Cisco Unified Contact Center Express Database Schema Guide

Updates to this document are as follows:

A new field autoanswer is included in the Team table

The storage size of the resourceLoginID and reskiller fileds are updated to 128

Added two new fields emailAuthType and emailOAuthDetails

Added a point about SMS/Email survey

Added new fields surveyname , dispatchid , and usehttpproxy

Removed the fields wdcode and wdcontextservicefieldsets

Cisco Unified Contact Center Express Features Guide

Updates to this document are as follows:

The step to accept certificates in Chrome is updated to include Edge Chromium

Added a note about Custom logon message

Added new fields HTTP , Authentication Type , and Private Key

Added a note about authentication type in Email password field

Added information about JAWS and a related note

Added information about Overage Allowance

Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express

Updates to this document are as follows:

Added Multi-Tab Gadgets

Added Custom logon details

The procedure to accept certificates in Chrome has been updated with Edge Chromium (Microsoft Edge)

Added Agent Device Selection

Cisco Unified Contact Center Express Installation and Upgrade Guide

Updates to this document are as follows:

Added details about COP file

Added the point about disabling SRTP before upgrade

Added a caution for installing second node

Cisco Unified Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR

Updates to this document are as follows:

For CSR generation, updated the supported key lengths that are restricted

Updated the introduction of Set Up Customized Logon Message to reflect all the applications that are impacted

Cisco Unified Contact Center Express Reporting User Guide

Updates to this document are as follows:

Updated the procedure to trust self signed certificates of Chrome with Edge Chromium (Microsoft Edge)

Updated information about Custom messages during sign in

Cisco Unified Contact Center Express Editor Step Reference Guide

Updates to this document are as follows:

Added the note about hostname validation

Added info about HTTP Content-type header

Solution Design Guide for Cisco Unified Contact Center Express

Updates to this document are as follows:

Changed Cisco WFO to Webex WFO and Advanced Quality Management to Quality Management

Added info about secure JTAPI connection between CUCM and Unified CM Telephony and RmCm

Added Agent Device Selection

Documents Not Updated in This Release

Getting Started with IP IVR Guide

Cisco Unified Contact Center Express Getting Started with Scripts

Cisco Unified Contact Center Express Expression Language Reference Guide

Port Utilization Guide for Cisco Unified Contact Center Express Solution

Documents Retired in This Release

None

Other Documentation Sources

This table lists other documentation sources that are updated in this release:

Document

Notes

Compatibility Matrix for Cisco Unified Contact Center Express 12.5(1)

Replaces the Compatibility Matrix

Updated to meet Cisco Unified Contact Center Express, Release 12.5(1) SU1 requirements.

To view the page, see

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html .

## Plan

The guides listed in this section relate to planning and designing a
                  		Unified CCX system.

### Cisco Customer
                     		  Contact Solutions Ordering Guide

This document
                     		  describes the pricing, packaging structure and ordering for Unified CCX.

The latest guide
                     		  is located at:

https://www.cisco.com/en/US/docs/voice_ip_comm/uc_system/design/guides/UCgoList.html .

### Cisco Unified
                     		  Contact Center Express Solution Design Guide

This document
                     		  describes system-level best practices and design guidelines for Unified CCX
                     		  Solution and the solution components.

The latest guide
                     		  is located at:

https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_implementation_design_guides_list.html

### Release Notes
                     		  for Unified Contact Center Express Solution

This document
                     		  describes the new features, updated features, and caveats for Unified CCX
                     		  Solution. Users should read the latest release notes before initially
                     		  installing or upgrading their Unified CCX system.

The latest guide
                     		  is located at:

https://www.cisco.com/en/US/products/sw/custcosw/ps1846/prod_release_notes_list.html .

### Open Source
                     		  Used in Unified Contact Center Express

This document
                     		  lists the licenses and notices for open source software that are used in
                     		  Unified CCX.

The latest guide
                     		  is located at:

https://www.cisco.com/c/en/us/about/legal/open-source-documentation-responsive.html?flt0_general-table0=Unified%20contact%20center%20express&flt1_general-table0=12.5(1)#~documentation .

### Compatibility
                     		  Matrix for Unified Contact Center Express

This compatibility
                     		  document lists supported product combinations for active Unified CCX product
                     		  sets.

The latest
                     		  compatibility information is located at:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html

### Virtualization
                     		  for Cisco Unified Contact Center Express

The virtualization
                     		  document describes Unified CCX virtualization requirements, guidelines, and
                     		  procedures.

The latest
                     		  virtualization-related information is located at:

https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-contact-center-express.html

## Install and
               	 Upgrade

The guides listed in this section relate to installing and upgrading
                  		Unified CCX.

### Cisco Unified
                     		  Contact Center Express Installation and Upgrade Guide

This document
                     		  explains the deployment options, how to install, upgrade, uninstall, and patch
                     		  Unified CCX, and how to change a Unified CCX deployment.

The latest guide
                     		  is located at:

https://www.cisco.com/en/US/products/sw/custcosw/ps1846/prod_installation_guides_list.html .

### Getting
                     		  Started with Cisco Unified IP IVR

This document
                     		  describes how to install and set up Unified IP IVR.

The latest guide
                     		  is located at:

https://www.cisco.com/en/US/products/sw/custcosw/ps1846/prod_installation_guides_list.html .

## Configure

The guides listed in
                  		this section relate to configuring a Unified CCX system. Configuration tasks
                  		are normally completed after you install the product or system.

### Cisco Unified
                     		  CCX Administration and Operations Guide

This document provides instructions for using the Unified CCX Administration web interface to provision the subsystems of
                     the Unified CCX package and to configure Unified CCX applications. This document also describes all the operations that are
                     related to Unified CCX:

Using the Unified CCX Serviceability interface to configure, monitor, and troubleshoot Unified CCX services and components.

Using Real-Time Monitoring Tool (RTMT) to monitor system performance and troubleshoot system problems.

Backing up and restoring.

Using CLI commands to configure, administer and troubleshoot Unified CCX.

Using the TCP and UCP ports.

The latest guide is located at:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html .

### Cisco Unified Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR

This document describes the system administration functions through the Cisco Unified Operating System for Unified CCX.

The latest guide
                     		  is located at:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html .

### Cisco
                     		  Unified Contact Center Express Features Guide

This document describes Cisco Webex Experience Management . The Cisco Webex Experience Management is a cloud service to configure surveys.

The latest guide
                     		  is located at:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-feature-guides-list.html .

### Port
                     		  Utilization Guide for Cisco Unified Contact Center Express Solutions

This document
                     		  describes all the operations using the TCP and UCP ports that are related to
                     		  Unified CCX and its components.

The latest guide
                     		  is located at:

https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_installation_and_configuration_guides_list.html .

### Cisco Unified
                     		  Contact Center Express CTI Protocol Developer Guide

This document
                     		  describes how to use the Unified CCX CTI protocol messages, and provides the
                     		  CTI protocol message definitions, and provides client application development
                     		  guidelines.

The latest guide
                     		  is located at:

https://developer.cisco.com/docs/contact-center-express/#!previous-documentation-pdfs .

### Cisco Unified
                     		  Contact Center Express Developer Guide

This document
                     		  describes all the configuration REST APIs that are available for Unified CCX.

The latest guide
                     		  is located at:

https://developer.cisco.com/docs/contact-center-express/

### Cisco Unified
                     		  Contact Center Express Getting Started with Scripts

This document is
                     		  volume 1 of the Scripting and Development Series, which contains three volumes,
                     		  and describes how to use the Unified CCX Editor to develop interactive scripts.
                     		  It presents the properties of Unified CCX Editor.

The latest guide
                     		  is located at:

https://developer.cisco.com/docs/contact-center-express/

### Cisco Unified
                     		  Contact Center Express Editor Step Reference Guide

This document is
                     		  volume 2 of the Scripting and Development Series, which contains three volumes,
                     		  and describes how to use the Unified CCX Editor to develop interactive scripts.
                     		  It describes how to use the Cisco Editor interface to create interactive
                     		  scripts.

The latest guide
                     		  is located at:

https://developer.cisco.com/docs/contact-center-express/

### Cisco Unified
                     		  Contact Center Express Expression Language Reference Guide

This document is
                     		  volume 3 of the Scripting and Development Series, which contains three volumes,
                     		  and describes how to use the Unified CCX Editor to develop interactive scripts.
                     		  It describes the language used for evaluation expressions in Unified CCX
                     		  scripts, prompt templates, and grammar templates.

The latest guide
                     		  is located at:

https://developer.cisco.com/docs/contact-center-express/

### Cisco Unified Contact Center Express Report Developer Guide

This document describes the call, chat, and email detail records. It describes how to create new reports by using Cisco Unified
                     Intelligence Center.

The latest guide is located at:

## User

The guides listed in this section are for agents, supervisors, and reporting administrators of Unified CCX.

### Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express

This document describes how to use Finesse agent desktop and Finesse supervisor desktop.

The latest guide is located at:

https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_user_guide_list.html .

### Cisco Unified Contact Center Express Reporting User Guide

This document describes the features that are available to a user using Unified Intelligence Center and all the fields in
                     the Historical Reports and provides the query designs for the Historical Reports. This document also describes the fields,
                     charts, available views, filters, and grouping for the Historical and Live Data Reports.

The latest guide is located at:

https://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_user_guide_list.html .

## Reference

The guides listed in
                  		this section are technical references related to Unified CCX.

### Cisco Unified
                     		  CCX Database Schema Guide

This document
                     		  describes how data is organized in the Unified CCX databases.

The latest guide is located at: https://www.cisco.com/en/US/products/sw/custcosw/ps1846/prod_technical_reference_list.html .

## Cisco Security
               	 Advisories

Addressing security
                  		issues in Cisco products is the responsibility of the Cisco Product Security
                  		Incident Response Team (PSIRT). The Cisco PSIRT is a dedicated, global team
                  		that manages the receipt, investigation, and public reporting of security
                  		vulnerability information that relates to Cisco products and networks.

For information on
                  		existing security issues, see Cisco Security Advisories, Responses, and Alerts
                  		at:

https://tools.cisco.com/security/center/publicationListing.x

## Related
               	 Documentation

This section
                     		  provides links to the documentation of the product components that are deployed
                     		  with Unified CCX.

Subject

Link

Finesse

For
                                 						Cisco Finesse documentation, see:

https://www.cisco.com/en/US/products/ps11324/tsd_products_support_series_home.html .

MRCP,
                                 						ASR and TTS

For
                                 						Media Resource Control Protocol (MRCP), Automated Speech Recognition (ASR), and
                                 						the MRCP Text-to-Speech (TTS) client components, see the Third-Party section of
                                 						the latest compatibility information is located at:

https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html .

For Cisco Customer Collaboration Platform documentation, see:

https://www.cisco.com/c/en/us/support/contact-center/unified-contact-center-express-12-5-1/model.html

Cisco
                                 						Unified Communications Manager

For
                                 						Cisco Unified Communications Manager documentation, see:

https://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html .

Cisco
                                 						Unified Intelligence Center

For
                                 						Cisco Unified Intelligence Center documentation, see:

https://www.cisco.com/en/US/products/ps9755/tsd_products_support_series_home.html .

Cisco Webex Workforce Optimization

For Cisco Webex Workforce Optimization documentation, see:

### This Document Applies to These Products

- Unified Contact Center Express 12.5(1)

| Document | Notes |
|---|---|
| Cisco Unified Contact Center Express Administration and Operations Guide | Updates to this document are as follows: Removed the commands, set cuic trace and show cuic trace Included Syslog Support for Critical Cisco Finesse Log Messages Removed the Cisco Finesse Trace Logging section Added Finesse Log Configuration, Connected Agents, and Multi-Tab Gadget The procedure to set up certificates in Chrome has been updated with Edge Chromium Added the command set cuic properties report-query-timeout Updated SRTP with the information related to RmCm provider user Added information related to Data Check and Data Resync when SRTP is selected Added information related to data synchronization Added info about restoring from a backup when SRTP is enabled and disabled Introduced setting of webapp session timeout Added the commands show webapp session timeout , show cli session timeout , set webapp session maxlimit , and set webapp session timeout Updated Agent ID details to support 64 characters Added a note about secure JTAPI connection for the SRTP field Added information about custom logon message Removed Cisco Unified Intelligence Center Services and added a note about CUIC CLI Added the commands utils cuic logging list , utils cuic logging config set , utils cuic logging update , utils cuic logging config show , utils cuic logging reset, utils cuic logging config clear, utils cuic session list, and utils cuic session delete Updated the description of Authorization Status and Status fields with Added Authorized - Reserved and Not Authorized - Reserved Added the fields Reserved Count , License Control , Current License Type , Overage Allowance , and I have purchased High Availability License Smart License Management Added a new topic Utils FIPS to mention the points to be considered before enabling FIPS Added the new alerts EmailOAuthConnectionFailed and EmailAuthenticationFailed in Unified CCX Alerts Added the new fields Authentication Type and Private Key in Contact Service Queues Added a note for Email password field in Contact Service Queues Added information about accessibility support for visually challenged Updated Localize Accessibility Messages Added a new topic to list Specific License Reservation commands Added the new field HTTP in Mail Server Configuration Included Agent Device Selection Included Auto Answer |
| Cisco Unified Contact Center Express Developer Guide | Updates to this document are as follows: Added new attributes emailAuthType and emailOAuthDetails Added information about emailAuthType for accountPassword attribute Added a new attribute useHttpProxy Added new elements emailAuthType , emailOAuthDetails , and useHttpProxy |
| Cisco Unified Contact Center Express CTI Protocol Developer Guide | Updates to this document are as follows: Updated the maximum supported CTI Protocol version to 18 Updated the configuration mask with Terminal Information Introduced a new event as part of Agent Device Selection Updated the message with new field ActiveTerminal Introduced a new field ConfigMsgMaskGranted Updated the FieldDataID field is 2 bytes Updated FieldDataID values 302 -305 for Agent Device Selection New error code CCX_ACTIVE_TERMINAL_NOT_SPECIFIED for Agent Device Selection The Maximum size of the Agent ID field is updated to 129 |
| Cisco Unified Contact Center Express Database Schema Guide | Updates to this document are as follows: A new field autoanswer is included in the Team table The storage size of the resourceLoginID and reskiller fileds are updated to 128 Added two new fields emailAuthType and emailOAuthDetails Added a point about SMS/Email survey Added new fields surveyname , dispatchid , and usehttpproxy Removed the fields wdcode and wdcontextservicefieldsets |
| Cisco Unified Contact Center Express Features Guide | Updates to this document are as follows: The step to accept certificates in Chrome is updated to include Edge Chromium Added a note about Custom logon message Added new fields HTTP , Authentication Type , and Private Key Added a note about authentication type in Email password field Added information about JAWS and a related note Added information about Overage Allowance |
| Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express | Updates to this document are as follows: Added Multi-Tab Gadgets Added Custom logon details The procedure to accept certificates in Chrome has been updated with Edge Chromium (Microsoft Edge) Added Agent Device Selection |
| Cisco Unified Contact Center Express Installation and Upgrade Guide | Updates to this document are as follows: Added details about COP file Added the point about disabling SRTP before upgrade Added a caution for installing second node |
| Cisco Unified Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR | Updates to this document are as follows: For CSR generation, updated the supported key lengths that are restricted Updated the introduction of Set Up Customized Logon Message to reflect all the applications that are impacted |
| Cisco Unified Contact Center Express Reporting User Guide | Updates to this document are as follows: Updated the procedure to trust self signed certificates of Chrome with Edge Chromium (Microsoft Edge) Updated information about Custom messages during sign in |
| Cisco Unified Contact Center Express Editor Step Reference Guide | Updates to this document are as follows: Added the note about hostname validation Added info about HTTP Content-type header |
| Solution Design Guide for Cisco Unified Contact Center Express | Updates to this document are as follows: Changed Cisco WFO to Webex WFO and Advanced Quality Management to Quality Management Added info about secure JTAPI connection between CUCM and Unified CM Telephony and RmCm Added Agent Device Selection |

| Document | Notes |
|---|---|
| Compatibility Matrix for Cisco Unified Contact Center Express 12.5(1) | Replaces the Compatibility Matrix Updated to meet Cisco Unified Contact Center Express, Release 12.5(1) SU1 requirements. To view the page, see https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html . |

| Subject | Link |
|---|---|
| Finesse | For
                                 						Cisco Finesse documentation, see: https://www.cisco.com/en/US/products/ps11324/tsd_products_support_series_home.html . |
| MRCP,
                                 						ASR and TTS | For
                                 						Media Resource Control Protocol (MRCP), Automated Speech Recognition (ASR), and
                                 						the MRCP Text-to-Speech (TTS) client components, see the Third-Party section of
                                 						the latest compatibility information is located at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html . |
| Customer Collaboration Platform | For Cisco Customer Collaboration Platform documentation, see: https://www.cisco.com/c/en/us/support/contact-center/unified-contact-center-express-12-5-1/model.html |
| Cisco
                                 						Unified Communications Manager | For
                                 						Cisco Unified Communications Manager documentation, see: https://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html . |
| Cisco
                                 						Unified Intelligence Center | For
                                 						Cisco Unified Intelligence Center documentation, see: https://www.cisco.com/en/US/products/ps9755/tsd_products_support_series_home.html . |
| Cisco Webex Workforce Optimization | For Cisco Webex Workforce Optimization documentation, see: https://www.cisco.com/c/en/us/support/contact-center/webex-workforce-optimization/series.html . |