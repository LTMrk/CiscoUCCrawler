---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-docguide-12-5-1-cucm-b-documentation-guide-cucm-imp-1251-html-132db22563
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/docguide/12_5_1/cucm_b_documentation-guide-cucm_imp_1251.html
retrieved_at: 2026-08-16T17:53:32.578934+00:00
---

Documentation Guide for Cisco Unified Communications Manager and IM and Presence Service, Release 12.5(1)

# Documentation Guide for Cisco Unified Communications Manager and IM and Presence Service, Release 12.5(1)

### Download Options

Updated: June 17, 2025

# Documentation Guide

## About this Guide

This guide contains an overview of the documentation that is available for Release 12.5(1) of Cisco Unified Communications
                     Manager and the IM and Presence Service, in addition to subsequent SU releases.

### SU Releases

If an SU document version exists that matches the specific SU release that you are running, use that SU document rather than
                              the baseline 12.5(1) version as the document contains updated information that was not in the 12.5(1) baseline.

If the document was republished for SU releases, but not the specific SU that you are running, use the latest version of the
                              document where the document version is less than, or equal to, the version that you are running. For example, if you are running
                              12.5(1)SU1, you can use documents from 12.5(1) or 12.5(1)SU1 (use the latest version of the document), but you cannot use
                              documents from 12.5(1)SU2 as it is a higher release, and may contain features that are not included in your release.

If no SU version of the document exists, use the 12.5(1) baseline version.

## Documentation Restructure 12.5(1)SU1 and Later

Following is a summary of the documentation restructure effort that was a part of 12.5(1)SU1. For this release and later releases,
                     many Unified Communications Manager documents were restructured in order to improve usability and to streamline the documentation
                     set. As part of this effort, one new guide is added, three existing guides are reworked, and five existing guides are deprecated.
                     This overall effort reduces the size of the Unified Communications Manager documentation suite by four guides.

Restructured Documents

Description

System Configuration Guide

As of 12.5(1)SU1, the System Configuration Guide is shortened and streamlined to create a complete post-install system setup. Basic security and SSO configurations are added
                              to fill out the basic setup, while advanced call processing features are moved to the Feature Configuration Guide . This new guide forms the Unified Communications Manager prerequisite for deploying an advanced Cisco call processing solution.

Feature Configuration Guide

This guide is expanded as the following advanced call processing topics are moved to this guide from the System Configuration Guide :

Call Control Discovery

External Call Control

Call Queuing

Call Throttling

Logical Partitioning

Location Awareness

Flexible DSCP Marking and Video Promotion

SIP Normalization and Transparency

SDP Transparency Profiles

Mobile and Remote Access

In addition, the following new sections are added for 12.5(1)SU1 and later:

Headsets Managements

Video Endpoints Management

Administration Guide

As of 12.5(1)SU1, the Administration Guide for Cisco Unified Communications Manager is expanded to include consolidated administration information from the Changing the IP Address, Hostname and Domain document, the Cisco Unified Reporting Administration Guide document and many sections from the existing Cisco Unified Serviceability Administration Guide documentation, all of which are deprecated for 12.5(1)SU1 and later.

In addition to the above updates, an overview of troubleshooting information has been inserted into the Administration Guide .

Call Reporting and Billing Administration Guide

This new document simplifies call reporting and billing administration documentation, consolidating existing material from
                              the documents Cisco Unified CDR Analysis and Reporting Administration Guide and the Call Detail Records Administration Guide , both of which are now deprecated. It also adds CDR Repository and billing server information that was available previously
                              with the Serviceability documentation. The new guide simplifies the overall structure and provides a clearer setup process:

Restructured Documents

Description

Security Guide

The Security Guide is restructured for Release 12.5(1)SU3. The new guide is streamlined and enhanced to make it easy to configure
                              and deploy security for Unified Communications Manager and registered endpoints. The new guide is split into three sections:

Basic Security —Contains information on how to configure basic security on Unified Communications Manager and on registered endpoints.

User Security —Contains information on how to manage identity, authentication, and user access.

Advanced Security Features —Contains information on how to deploy advanced security features such as FIPS Mode, Enhanced Security Mode, and V.150.

The book also includes enhanced information with new topics on subjects like Security Hardening and Identity Management that
                              help you make security decisions for your deployment.

Push Notifications Deployment for Cisco Jabber on iPhone and iPad

This document describes how to configure Push Notifications for Cisco Jabber on iPhone and iPad with Cisco Unified Communications
                              Manager and the IM and Presence Service. The guide is updated to include Push Notifications support for Cisco Jabber and Cisco
                              Webex clients that run on both Android devices and iOS devices.

## Documents for Cisco Unified Communications Manager 12.5(x)

This section summarizes the documents that are available for Cisco Unified Communications Manager Release 12.5(1), and subsequent
                     12.5(1) SU releases.

Document

Description

Release Guides

Compatibility Matrix

Provides detailed information about upgrade paths and compatible devices and applications for Cisco Unified Communications
                                 Manager and IM and Presence Service.

Release Notes for Cisco Unified Communications Manager and the IM and Presence Service

Describes release-specific information such as system requirements, new features, changed information, documentation updates,
                                 and open caveats for the latest release of Cisco Unified Communications Manager and IM and Presence Service.

New and Changed Features

This chapter from the Release Notes contains information on the new and changed features for this release.

Readme Files

The OVA Readme contains information on deploying the 12.5 OVA template.

The SU Readme files contain information on bug fixes and updates that are included in the SU release.

Release Notes for Prime Collaboration Deployment

Release-specific information for the latest release of Cisco Prime Collaboration Deployment.

Release Notes for Prime Collaboration Deployment 12.5(1)

Release Notes for Prime Collaboration Deployment 12.6(1)

Open Source Documents

The Open Source document contain licenses and notices for open source software used in the respective products.

Install and Upgrade Guides

Installation Guide

Use this guide to install Cisco Unified Communications Manager and IM and Presence Service on the publisher database and subscriber
                                 nodes.

Upgrade and Migration Guide

Use this guide to upgrade to the latest release of Cisco Unified Communications Manager and IM and Presence Service.

Replacing a Single Server or Cluster

Use this guide to replace an entire cluster or a single server in a cluster for Cisco Unified Communications Manager.

Cisco Collaboration on Virtual Servers

Use this guide to get technical information that you need to run Cisco Unified Communications Manager on virtual servers.

Configuration Guides

System Configuration Guide

Use this guide to configure the call control system of Cisco Unified Communications Manager. This guide includes Day 1 configurations
                                 such as inbound and outbound calling, dial plans, and network resources.

For 12.5(1)SU1 and later, this guide is restructured and streamlined to be a post-install basic setup. Basic security and
                                          SSO configurations are added while advanced call processing is moved to the Feature Configuration Guide . This streamlined guide forms the prerequisite to deploying an advanced call control solution.

System Configuration 12.5(1)

System Configuration 12.5(1)SU1

System Configuration 12.5(1)SU2

System Configuration 12.5(1)SU3

System Configuration 12.5(1)SU4

System Configuration 12.5(1)SU7

12.5(1)SU4-SU7 is now a consolidated guide.

Feature Configuration Guide

Use this guide to configure features for Cisco Unified Communications Manager. Refer to this guide after you configure the
                                 call control system.

For 12.5(1)SU1 and later, the guide is expanded with advanced call processing features that were in the System Configuration
                                          Guide previously. In addition, the Cisco Headsets and Video Endpoints Management features are added.

This document describes how to configure Push Notifications for Cisco Jabber on iPhone and iPad with Cisco Unified Communications
                                 Manager and the IM and Presence Service.

Programming Guides

Cisco Unified JTAPI Developers Guide

Describes the Cisco implementation of JTAPI for the Cisco Unified Communications Manager platform.

Cisco Unified TAPI Developers Guide

Describes the Cisco TAPI Service Provider (TSP), which allows developers to create customized IP telephony applications for
                                 Cisco users. Cisco conforms as closely as possible to the JTAPI specification while providing extensions that enhance JTAPI
                                 and expose the advanced features of Cisco Unified Communications Manager to applications

Maintain and Operate Guides

Administration Guide

Use this guide to complete administrative tasks on a configured Cisco Unified Communications Manager system. You can use this
                                 to perform tasks such as adding users, adding devices, running backups and restores.

For 12.5(1)SU1 and later, this guide is expanded to include sections that were previously in the Changing the IP Address, Hostname and Domain , Cisco Unified Reporting Administration Guide and Cisco Unified Serviceability Administration Guide .

Administration Guide 12.5(1)

Administration Guide 12.5(1)SU1

Administration Guide 12.5(1)SU3

Administration Guide 12.5(1)SU4

Administration Guide 12.5(1)SU6

Administration Guide 12.5(1)SU7

12.5(1)SU6-SU7 is now a consolidated guide.

Security Guide

Use this guide to configure authentication and encryption for Cisco Unified Communications Manager, Cisco Unified IP Phones,
                                 Cisco Unified Survivable Remote Site Telephony (Unified SRST) references, Media Gateway Control Protocol (MGCP) gateways,
                                 and Cisco Unity and Cisco Unity Connection voice-messaging ports

SAML SSO Deployment Guide

Use this guide to learn key concepts, terminology, and high-level information that you need to configure and enable the SAML-based
                                 SSO solution across a defined set of Cisco collaboration applications.

Prime Collaboration Deployment Administration Guide

Use Cisco Prime Collaboration Deployment to migrate existing Unified Communication server clusters to new clusters. It also
                                 describes how to perform operations on existing clusters such as fresh installs, upgrades, migrations, installs, upgrades,
                                 and IP address or hostname changes.

Prime Collaboration Deployment Administration 12.5(1)

Prime Collaboration Deployment Administration 12.6(1)

Bulk Administration Guide

Use the Bulk Administration Tool to add, update, or delete a large numbers of users, devices, or ports in Cisco Unified Communications
                                 Manager.

Bulk Administration 12.5(1)SU2

Bulk Administration 12.5(1)SU4

Bulk Administration 12.5(1)SU6

Cisco Unified Serviceability Adminstration Guide

Use Cisco Unified Serviceability to configure alarms, traces, and SNMP for Cisco Unified Communications Manager and the IM
                                 and Presence Service. This document also describes how to activate, start, and stop feature and network services

Serviceability Administration Guide 12.5(1)

Serviceability Administration Guide 12.5(1)SU1

Real-Time Monitoring Tool Administration Guide

Use this guide to install and use the Cisco Unified Real-Time Monitoring Tool to monitor the real-time behavior of system
                                 components for Cisco Unified Communications Manager and IM and Presence Service.

Real-Time Monitoring Tool Administration Guide 12.5(1)

Real-Time Monitoring Tool Administration Guide 12.5(1)SU3

Real-Time Monitoring Tool Administration Guide 12.5(1)SU4

Changing the IP Address and Hostname

Use this guide to change the IP address, hostname, or domain for Cisco Unified Communications Manager and IM and Presence
                                 Service.

For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Administration Guide for Cisco Unified Communications Manager .

Cisco Unified CDR Analysis and Reporting Administration Guide

Use this guide to configure and use Cisco Unified Communications Manager CDR Analysis and Reporting (CAR), to create user,
                                 system, device, and billing report.

For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Call Reporting and Billing Administration Guide thereby deprecating this book.

Call Detail Records Administration Guide

Refer to this guide for examples and descriptions of CDR and CMR records in CDR Analysis and Reporting.

For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Call Reporting and Billing Administration Guide thereby deprecating this book.

Command Line Interface Reference Guide

Refer to this guide for the Command Line Interface (CLI) commands that are available for a Cisco Unified Communications Solution

Dial Plan Deployment Guide

Use this guide to deploy a dial plan. This guide applies to all releases of Cisco Unified Communications Manager.

Dialed Number Analyzer

Use the Dialed Number Analyzer to test and diagnose a deployed Cisco Unified Communications Manager dial plan configuration.

Managed Services Guide

Use this guide to monitor and maintain service provider networks, including the monitoring of system health, SNMP traps and
                                 syslog messages, MIBs, Cisco Unified Serviceability alerts and alarms, CiscoLog messages, and Cisco Unified Real-Time Monitoring
                                 Tool traces, perfmons, and alerts.

Call Reporting and Billing Administration Guide

For 12.5(1)SU1 and later, this guide replaces both the CDR Analysis and Reporting Administration Guide and the Call Detail Records Adminstration Guide . This guide contains configuration information to set up call reporting and billing via the CDR Analysis and Reporting system
                                 as well as a description of the CDR and CMR contents.

End User Guides

Self Care Portal User Guide

Refer your end users to this user guide for procedures on how to use the Cisco Unified Communications Self Care Portal to
                                 customize user options such as speed dials, conference settings, and IM and Presence status on their Cisco Unified IP Phones.

Manager Assistant User Guide

Use this guide to configure the Cisco Unified Communications Manager Assistant (Manager Assistant).

Troubleshooting Guides

Troubleshooting Guide

Use this guide to troubleshoot and resolve Cisco Unified Communications Manager system and configuration problems.

## Documents for IM and Presence Service 12.5(x)

This section summarizes the documents that are available for the IM and Presence Service, Release 12.5(1) and subsequent 12.5(1)
                     SU releases.

Document

Description

Compatibility Matrix

Provides detailed information about upgrade paths and compatible devices and applications for Cisco Unified Communications
                                 Manager and IM and Presence Service.

Release Notes for Cisco Unified Communications Manager and the IM and Presence Service

Describes release-specific information such as system requirements, new features, changed information, documentation updates,
                                 and open caveats for the latest release of Cisco Unified Communications Manager and IM and Presence Service.

Readme Files

The OVA Readme contains information on deploying the 12.5 OVA template.

The SU Readme files contain information on bug fixes and updates that are included in the SU release.

Release Notes for Prime Collaboration Deployment

Release-specific information for the latest release of Cisco Prime Collaboration Deployment.

Release Notes for Prime Collaboration Deployment 12.5(1)

Release Notes for Prime Collaboration Deployment 12.6(1)

Install and Upgrade Guides

Installation Guide

Use this guide to install Cisco Unified Communications Manager and IM and Presence Service on the publisher database and subscriber
                                 nodes.

Upgrade and Migration Guide

Use this guide to upgrade to the latest release of Cisco Unified Communications Manager and IM and Presence Service.

Configuration Guides

Configuration and Administration for IM and Presence Service

Use this guide to configure and administer the IM and Presence Service.

Configuration and Adminisration Guide 12.5(1)

Configuration and Administration Guide 12.5(1)SU1

Configuration and Administration Guide 12.5(1)SU2

Configuration and Administration Guide 12.5(1)SU3

Configuration and Administration Guide 12.5(1)SU4

Configuration and Administration Guide 12.5(1)SU7

12.5(1)SU4-SU7 is now a consolidated guide.

Database Setup Guide

Use this guide to configure an external database to store information synchronized from the IM and Presence Service.

Database Setup Guide 12.5(1)

Database Setup Guide 12.5(1)SU1

Instant Messaging Compliance Guide

Use this guide to configure the Instant Messaging Compliance feature on the IM and Presence Service.

Interdomain Federation Guide

Use this guide to configure IM and Presence Service for interdomain federation over the SIP protocol with Microsoft Lync/OCS,
                                 and over the XMPP protocol with IBM Sametime, Googletalk, Webex Connect, and another IM and Presence Service enterprise.

Interdomain Federation Guide 12.5(1)SU3

Partitioned Intradomain Federation Guide

Use this guide to configure Partitioned Intradomain Federation between IM and Presence Service and Microsoft Lync/OCS.

MS Outlook Calendar Integration

Use this guide to integrate IM and Presence Service with Microsoft Exchange Calendar 2003, 2007, or 2010.

MS Outlook Calendar Integration 12.5(1)

MS Outlook Calendar Integration 12.5(1)SU2

Push Notifications Deployment for Cisco Jabber on iPhone and iPad

This document describes how to configure Push Notifications for Cisco Jabber on iPhone and iPad with Cisco Unified Communications
                                 Manager and the IM and Presence Service.

Remote Call Control with Microsoft Lync Server Guide

Use this guide to integrate IM and Presence Service with Microsoft Lync Server for Remote Call Control (RCC).

Programming Guides

Cisco Unified TAPI Developers Guide

Describes the Cisco TAPI Service Provider (TSP), which allows developers to create customized IP telephony applications for
                                 Cisco users. Cisco conforms as closely as possible to the JTAPI specification while providing extensions that enhance JTAPI
                                 and expose the advanced features of Cisco Unified Communications Manager to applications.

Maintain and Operate Guides

Security Guide

Use this guide to configure authentication and encryption for Cisco Unified Communications Manager, Cisco Unified IP Phones,
                                 Cisco Unified Survivable Remote Site Telephony (Unified SRST) references, Media Gateway Control Protocol (MGCP) gateways,
                                 and Cisco Unity and Cisco Unity Connection voice-messaging ports.

SAML SSO Deployment Guide

Use this guide to learn key concepts, terminology, and high-level information that you need to configure and enable the SAML-based
                                 SSO solution across a defined set of Cisco collaboration applications.

Prime Collaboration Deployment Administration Guide

Use Cisco Prime Collaboration Deployment to migrate existing Unified Communication server clusters to new clusters. It also
                                 describes how to perform operations on existing clusters such as fresh installs, upgrades, migrations, installs, upgrades,
                                 and IP address or hostname changes.

Prime Collaboration Deployment Administration 12.5(1)

Prime Collaboration Deployment Administration 12.6(1)

Changing the IP Address and Hostname

Use this guide to change the IP address, hostname, or domain for Cisco Unified Communications Manager and IM and Presence
                                 Service.

For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Administration Guide for Cisco Unified Communications Manager .

Cisco Unified Serviceability Administration Guide

Use Cisco Unified Serviceability to configure alarms, traces, and SNMP for Cisco Unified Communications Manager and the IM
                                 and Presence Service. This document also describes how to activate, start, and stop feature and network services.

Serviceability Administration 12.5(1)

Serviceability Administration 12.5(1)SU1

Cisco Unified Real-Time Monitoring Tool Administration Guide

Use this guide to install and use the Cisco Unified Real-Time Monitoring Tool to monitor the real-time behavior of system
                                 components for Cisco Unified Communications Manager and IM and Presence Service.

Real-Time Monitoring Tool Administration Guide 12.5(1)

Real-Time Monitoring Tool Administration Guide 12.5(1)SU3

Real-Time Monitoring Tool Administration Guide 12.5(1)SU4

Managed Services Guide

Use this guide to monitor and maintain service provider networks, including the monitoring of system health, SNMP traps and
                                 syslog messages, MIBs, Cisco Unified Serviceability alerts and alarms, CiscoLog messages, and Cisco Unified Real-Time Monitoring
                                 Tool traces, perfmons, and alerts.

Command Line Interface Reference Guide

Refer to this guide for the Command Line Interface (CLI) commands that are available for a Cisco Unified Communications Solution.

Jabber for Everyone Quick Start Guide

Jabber for everyone makes Cisco Jabber presence and instant messaging (IM) available at a small end user cost for customers
                                 who have deployed Cisco Unified Communications Manager for all or part of their organization.

This document describes the necessary steps required for deployment of Cisco Jabber. This is a quick start guide and will
                                 not cover any of the advanced features supported by Cisco Jabber.

| Restructured Documents | Description |
|---|---|
| System Configuration Guide | As of 12.5(1)SU1, the System Configuration Guide is shortened and streamlined to create a complete post-install system setup. Basic security and SSO configurations are added
                              to fill out the basic setup, while advanced call processing features are moved to the Feature Configuration Guide . This new guide forms the Unified Communications Manager prerequisite for deploying an advanced Cisco call processing solution. |
| Feature Configuration Guide | This guide is expanded as the following advanced call processing topics are moved to this guide from the System Configuration Guide : Call Control Discovery External Call Control Call Queuing Call Throttling Logical Partitioning Location Awareness Flexible DSCP Marking and Video Promotion SIP Normalization and Transparency SDP Transparency Profiles Mobile and Remote Access In addition, the following new sections are added for 12.5(1)SU1 and later: Headsets Managements Video Endpoints Management |
| Administration Guide | As of 12.5(1)SU1, the Administration Guide for Cisco Unified Communications Manager is expanded to include consolidated administration information from the Changing the IP Address, Hostname and Domain document, the Cisco Unified Reporting Administration Guide document and many sections from the existing Cisco Unified Serviceability Administration Guide documentation, all of which are deprecated for 12.5(1)SU1 and later. In addition to the above updates, an overview of troubleshooting information has been inserted into the Administration Guide . |
| Call Reporting and Billing Administration Guide | This new document simplifies call reporting and billing administration documentation, consolidating existing material from
                              the documents Cisco Unified CDR Analysis and Reporting Administration Guide and the Call Detail Records Administration Guide , both of which are now deprecated. It also adds CDR Repository and billing server information that was available previously
                              with the Serviceability documentation. The new guide simplifies the overall structure and provides a clearer setup process: |

| Restructured Documents | Description |
|---|---|
| Security Guide | The Security Guide is restructured for Release 12.5(1)SU3. The new guide is streamlined and enhanced to make it easy to configure
                              and deploy security for Unified Communications Manager and registered endpoints. The new guide is split into three sections: Basic Security —Contains information on how to configure basic security on Unified Communications Manager and on registered endpoints. User Security —Contains information on how to manage identity, authentication, and user access. Advanced Security Features —Contains information on how to deploy advanced security features such as FIPS Mode, Enhanced Security Mode, and V.150. The book also includes enhanced information with new topics on subjects like Security Hardening and Identity Management that
                              help you make security decisions for your deployment. |
| Push Notifications Deployment for Cisco Jabber on iPhone and iPad | This document describes how to configure Push Notifications for Cisco Jabber on iPhone and iPad with Cisco Unified Communications
                              Manager and the IM and Presence Service. The guide is updated to include Push Notifications support for Cisco Jabber and Cisco
                              Webex clients that run on both Android devices and iOS devices. |

| Document | Description |
|---|---|
| Release Guides |
| Compatibility Matrix | Provides detailed information about upgrade paths and compatible devices and applications for Cisco Unified Communications
                                 Manager and IM and Presence Service. |
| Release Notes for Cisco Unified Communications Manager and the IM and Presence Service | Describes release-specific information such as system requirements, new features, changed information, documentation updates,
                                 and open caveats for the latest release of Cisco Unified Communications Manager and IM and Presence Service. |
| New and Changed Features | This chapter from the Release Notes contains information on the new and changed features for this release. |
| Readme Files | The OVA Readme contains information on deploying the 12.5 OVA template. The SU Readme files contain information on bug fixes and updates that are included in the SU release. |
| Release Notes for Prime Collaboration Deployment | Release-specific information for the latest release of Cisco Prime Collaboration Deployment. Release Notes for Prime Collaboration Deployment 12.5(1) Release Notes for Prime Collaboration Deployment 12.6(1) |
| Open Source Documents | The Open Source document contain licenses and notices for open source software used in the respective products. |
| Install and Upgrade Guides |
| Installation Guide | Use this guide to install Cisco Unified Communications Manager and IM and Presence Service on the publisher database and subscriber
                                 nodes. |
| Upgrade and Migration Guide | Use this guide to upgrade to the latest release of Cisco Unified Communications Manager and IM and Presence Service. |
| Replacing a Single Server or Cluster | Use this guide to replace an entire cluster or a single server in a cluster for Cisco Unified Communications Manager. |
| Cisco Collaboration on Virtual Servers | Use this guide to get technical information that you need to run Cisco Unified Communications Manager on virtual servers. |
| Configuration Guides |
| System Configuration Guide | Use this guide to configure the call control system of Cisco Unified Communications Manager. This guide includes Day 1 configurations
                                 such as inbound and outbound calling, dial plans, and network resources. Note For 12.5(1)SU1 and later, this guide is restructured and streamlined to be a post-install basic setup. Basic security and
                                          SSO configurations are added while advanced call processing is moved to the Feature Configuration Guide . This streamlined guide forms the prerequisite to deploying an advanced call control solution. System Configuration 12.5(1) System Configuration 12.5(1)SU1 System Configuration 12.5(1)SU2 System Configuration 12.5(1)SU3 System Configuration 12.5(1)SU4 System Configuration 12.5(1)SU7 Note 12.5(1)SU4-SU7 is now a consolidated guide. | Note | For 12.5(1)SU1 and later, this guide is restructured and streamlined to be a post-install basic setup. Basic security and
                                          SSO configurations are added while advanced call processing is moved to the Feature Configuration Guide . This streamlined guide forms the prerequisite to deploying an advanced call control solution. | Note | 12.5(1)SU4-SU7 is now a consolidated guide. |
| Note | For 12.5(1)SU1 and later, this guide is restructured and streamlined to be a post-install basic setup. Basic security and
                                          SSO configurations are added while advanced call processing is moved to the Feature Configuration Guide . This streamlined guide forms the prerequisite to deploying an advanced call control solution. |
| Note | 12.5(1)SU4-SU7 is now a consolidated guide. |
| Feature Configuration Guide | Use this guide to configure features for Cisco Unified Communications Manager. Refer to this guide after you configure the
                                 call control system. Note For 12.5(1)SU1 and later, the guide is expanded with advanced call processing features that were in the System Configuration
                                          Guide previously. In addition, the Cisco Headsets and Video Endpoints Management features are added. | Note | For 12.5(1)SU1 and later, the guide is expanded with advanced call processing features that were in the System Configuration
                                          Guide previously. In addition, the Cisco Headsets and Video Endpoints Management features are added. |
| Note | For 12.5(1)SU1 and later, the guide is expanded with advanced call processing features that were in the System Configuration
                                          Guide previously. In addition, the Cisco Headsets and Video Endpoints Management features are added. |
| Push Notifications Deployment for Cisco Jabber on iPhone and iPad | This document describes how to configure Push Notifications for Cisco Jabber on iPhone and iPad with Cisco Unified Communications
                                 Manager and the IM and Presence Service. |
| Programming Guides |
| Cisco Unified JTAPI Developers Guide | Describes the Cisco implementation of JTAPI for the Cisco Unified Communications Manager platform. |
| Cisco Unified TAPI Developers Guide | Describes the Cisco TAPI Service Provider (TSP), which allows developers to create customized IP telephony applications for
                                 Cisco users. Cisco conforms as closely as possible to the JTAPI specification while providing extensions that enhance JTAPI
                                 and expose the advanced features of Cisco Unified Communications Manager to applications |
| Maintain and Operate Guides |
| Administration Guide | Use this guide to complete administrative tasks on a configured Cisco Unified Communications Manager system. You can use this
                                 to perform tasks such as adding users, adding devices, running backups and restores. Note For 12.5(1)SU1 and later, this guide is expanded to include sections that were previously in the Changing the IP Address, Hostname and Domain , Cisco Unified Reporting Administration Guide and Cisco Unified Serviceability Administration Guide . Administration Guide 12.5(1) Administration Guide 12.5(1)SU1 Administration Guide 12.5(1)SU3 Administration Guide 12.5(1)SU4 Administration Guide 12.5(1)SU6 Administration Guide 12.5(1)SU7 Note 12.5(1)SU6-SU7 is now a consolidated guide. | Note | For 12.5(1)SU1 and later, this guide is expanded to include sections that were previously in the Changing the IP Address, Hostname and Domain , Cisco Unified Reporting Administration Guide and Cisco Unified Serviceability Administration Guide . | Note | 12.5(1)SU6-SU7 is now a consolidated guide. |
| Note | For 12.5(1)SU1 and later, this guide is expanded to include sections that were previously in the Changing the IP Address, Hostname and Domain , Cisco Unified Reporting Administration Guide and Cisco Unified Serviceability Administration Guide . |
| Note | 12.5(1)SU6-SU7 is now a consolidated guide. |
| Security Guide | Use this guide to configure authentication and encryption for Cisco Unified Communications Manager, Cisco Unified IP Phones,
                                 Cisco Unified Survivable Remote Site Telephony (Unified SRST) references, Media Gateway Control Protocol (MGCP) gateways,
                                 and Cisco Unity and Cisco Unity Connection voice-messaging ports |
| SAML SSO Deployment Guide | Use this guide to learn key concepts, terminology, and high-level information that you need to configure and enable the SAML-based
                                 SSO solution across a defined set of Cisco collaboration applications. |
| Prime Collaboration Deployment Administration Guide | Use Cisco Prime Collaboration Deployment to migrate existing Unified Communication server clusters to new clusters. It also
                                 describes how to perform operations on existing clusters such as fresh installs, upgrades, migrations, installs, upgrades,
                                 and IP address or hostname changes. Prime Collaboration Deployment Administration 12.5(1) Prime Collaboration Deployment Administration 12.6(1) |
| Bulk Administration Guide | Use the Bulk Administration Tool to add, update, or delete a large numbers of users, devices, or ports in Cisco Unified Communications
                                 Manager. Bulk Administration 12.5(1)SU2 Bulk Administration 12.5(1)SU4 Bulk Administration 12.5(1)SU6 |
| Cisco Unified Serviceability Adminstration Guide | Use Cisco Unified Serviceability to configure alarms, traces, and SNMP for Cisco Unified Communications Manager and the IM
                                 and Presence Service. This document also describes how to activate, start, and stop feature and network services Serviceability Administration Guide 12.5(1) Serviceability Administration Guide 12.5(1)SU1 |
| Real-Time Monitoring Tool Administration Guide | Use this guide to install and use the Cisco Unified Real-Time Monitoring Tool to monitor the real-time behavior of system
                                 components for Cisco Unified Communications Manager and IM and Presence Service. Real-Time Monitoring Tool Administration Guide 12.5(1) Real-Time Monitoring Tool Administration Guide 12.5(1)SU3 Real-Time Monitoring Tool Administration Guide 12.5(1)SU4 |
| Changing the IP Address and Hostname | Use this guide to change the IP address, hostname, or domain for Cisco Unified Communications Manager and IM and Presence
                                 Service. Note For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Administration Guide for Cisco Unified Communications Manager . | Note | For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Administration Guide for Cisco Unified Communications Manager . |
| Note | For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Administration Guide for Cisco Unified Communications Manager . |
| Cisco Unified CDR Analysis and Reporting Administration Guide | Use this guide to configure and use Cisco Unified Communications Manager CDR Analysis and Reporting (CAR), to create user,
                                 system, device, and billing report. Note For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Call Reporting and Billing Administration Guide thereby deprecating this book. | Note | For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Call Reporting and Billing Administration Guide thereby deprecating this book. |
| Note | For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Call Reporting and Billing Administration Guide thereby deprecating this book. |
| Call Detail Records Administration Guide | Refer to this guide for examples and descriptions of CDR and CMR records in CDR Analysis and Reporting. Note For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Call Reporting and Billing Administration Guide thereby deprecating this book. | Note | For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Call Reporting and Billing Administration Guide thereby deprecating this book. |
| Note | For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Call Reporting and Billing Administration Guide thereby deprecating this book. |
| Command Line Interface Reference Guide | Refer to this guide for the Command Line Interface (CLI) commands that are available for a Cisco Unified Communications Solution |
| Dial Plan Deployment Guide | Use this guide to deploy a dial plan. This guide applies to all releases of Cisco Unified Communications Manager. |
| Dialed Number Analyzer | Use the Dialed Number Analyzer to test and diagnose a deployed Cisco Unified Communications Manager dial plan configuration. |
| Managed Services Guide | Use this guide to monitor and maintain service provider networks, including the monitoring of system health, SNMP traps and
                                 syslog messages, MIBs, Cisco Unified Serviceability alerts and alarms, CiscoLog messages, and Cisco Unified Real-Time Monitoring
                                 Tool traces, perfmons, and alerts. |
| Call Reporting and Billing Administration Guide | For 12.5(1)SU1 and later, this guide replaces both the CDR Analysis and Reporting Administration Guide and the Call Detail Records Adminstration Guide . This guide contains configuration information to set up call reporting and billing via the CDR Analysis and Reporting system
                                 as well as a description of the CDR and CMR contents. |
| End User Guides |
| Self Care Portal User Guide | Refer your end users to this user guide for procedures on how to use the Cisco Unified Communications Self Care Portal to
                                 customize user options such as speed dials, conference settings, and IM and Presence status on their Cisco Unified IP Phones. |
| Manager Assistant User Guide | Use this guide to configure the Cisco Unified Communications Manager Assistant (Manager Assistant). |
| Troubleshooting Guides |
| Troubleshooting Guide | Use this guide to troubleshoot and resolve Cisco Unified Communications Manager system and configuration problems. |

| Note | For 12.5(1)SU1 and later, this guide is restructured and streamlined to be a post-install basic setup. Basic security and
                                          SSO configurations are added while advanced call processing is moved to the Feature Configuration Guide . This streamlined guide forms the prerequisite to deploying an advanced call control solution. |
|---|---|

| Note | 12.5(1)SU4-SU7 is now a consolidated guide. |
|---|---|

| Note | For 12.5(1)SU1 and later, the guide is expanded with advanced call processing features that were in the System Configuration
                                          Guide previously. In addition, the Cisco Headsets and Video Endpoints Management features are added. |
|---|---|

| Note | For 12.5(1)SU1 and later, this guide is expanded to include sections that were previously in the Changing the IP Address, Hostname and Domain , Cisco Unified Reporting Administration Guide and Cisco Unified Serviceability Administration Guide . |
|---|---|

| Note | 12.5(1)SU6-SU7 is now a consolidated guide. |
|---|---|

| Note | For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Administration Guide for Cisco Unified Communications Manager . |
|---|---|

| Note | For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Call Reporting and Billing Administration Guide thereby deprecating this book. |
|---|---|

| Note | For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Call Reporting and Billing Administration Guide thereby deprecating this book. |
|---|---|

| Document | Description |
|---|---|
| Compatibility Matrix | Provides detailed information about upgrade paths and compatible devices and applications for Cisco Unified Communications
                                 Manager and IM and Presence Service. |
| Release Notes for Cisco Unified Communications Manager and the IM and Presence Service | Describes release-specific information such as system requirements, new features, changed information, documentation updates,
                                 and open caveats for the latest release of Cisco Unified Communications Manager and IM and Presence Service. |
| Readme Files | The OVA Readme contains information on deploying the 12.5 OVA template. The SU Readme files contain information on bug fixes and updates that are included in the SU release. |
| Release Notes for Prime Collaboration Deployment | Release-specific information for the latest release of Cisco Prime Collaboration Deployment. Release Notes for Prime Collaboration Deployment 12.5(1) Release Notes for Prime Collaboration Deployment 12.6(1) |
| Install and Upgrade Guides |
| Installation Guide | Use this guide to install Cisco Unified Communications Manager and IM and Presence Service on the publisher database and subscriber
                                 nodes. |
| Upgrade and Migration Guide | Use this guide to upgrade to the latest release of Cisco Unified Communications Manager and IM and Presence Service. |
| Configuration Guides |
| Configuration and Administration for IM and Presence Service | Use this guide to configure and administer the IM and Presence Service. Configuration and Adminisration Guide 12.5(1) Configuration and Administration Guide 12.5(1)SU1 Configuration and Administration Guide 12.5(1)SU2 Configuration and Administration Guide 12.5(1)SU3 Configuration and Administration Guide 12.5(1)SU4 Configuration and Administration Guide 12.5(1)SU7 Note 12.5(1)SU4-SU7 is now a consolidated guide. | Note | 12.5(1)SU4-SU7 is now a consolidated guide. |
| Note | 12.5(1)SU4-SU7 is now a consolidated guide. |
| Database Setup Guide | Use this guide to configure an external database to store information synchronized from the IM and Presence Service. Database Setup Guide 12.5(1) Database Setup Guide 12.5(1)SU1 |
| Instant Messaging Compliance Guide | Use this guide to configure the Instant Messaging Compliance feature on the IM and Presence Service. |
| Interdomain Federation Guide | Use this guide to configure IM and Presence Service for interdomain federation over the SIP protocol with Microsoft Lync/OCS,
                                 and over the XMPP protocol with IBM Sametime, Googletalk, Webex Connect, and another IM and Presence Service enterprise. Interdomain Federation Guide 12.5(1)SU3 |
| Partitioned Intradomain Federation Guide | Use this guide to configure Partitioned Intradomain Federation between IM and Presence Service and Microsoft Lync/OCS. |
| MS Outlook Calendar Integration | Use this guide to integrate IM and Presence Service with Microsoft Exchange Calendar 2003, 2007, or 2010. MS Outlook Calendar Integration 12.5(1) MS Outlook Calendar Integration 12.5(1)SU2 |
| Push Notifications Deployment for Cisco Jabber on iPhone and iPad | This document describes how to configure Push Notifications for Cisco Jabber on iPhone and iPad with Cisco Unified Communications
                                 Manager and the IM and Presence Service. |
| Remote Call Control with Microsoft Lync Server Guide | Use this guide to integrate IM and Presence Service with Microsoft Lync Server for Remote Call Control (RCC). |
| Programming Guides |
| Cisco Unified TAPI Developers Guide | Describes the Cisco TAPI Service Provider (TSP), which allows developers to create customized IP telephony applications for
                                 Cisco users. Cisco conforms as closely as possible to the JTAPI specification while providing extensions that enhance JTAPI
                                 and expose the advanced features of Cisco Unified Communications Manager to applications. |
| Maintain and Operate Guides |
| Security Guide | Use this guide to configure authentication and encryption for Cisco Unified Communications Manager, Cisco Unified IP Phones,
                                 Cisco Unified Survivable Remote Site Telephony (Unified SRST) references, Media Gateway Control Protocol (MGCP) gateways,
                                 and Cisco Unity and Cisco Unity Connection voice-messaging ports. |
| SAML SSO Deployment Guide | Use this guide to learn key concepts, terminology, and high-level information that you need to configure and enable the SAML-based
                                 SSO solution across a defined set of Cisco collaboration applications. |
| Prime Collaboration Deployment Administration Guide | Use Cisco Prime Collaboration Deployment to migrate existing Unified Communication server clusters to new clusters. It also
                                 describes how to perform operations on existing clusters such as fresh installs, upgrades, migrations, installs, upgrades,
                                 and IP address or hostname changes. Prime Collaboration Deployment Administration 12.5(1) Prime Collaboration Deployment Administration 12.6(1) |
| Changing the IP Address and Hostname | Use this guide to change the IP address, hostname, or domain for Cisco Unified Communications Manager and IM and Presence
                                 Service. Note For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Administration Guide for Cisco Unified Communications Manager . | Note | For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Administration Guide for Cisco Unified Communications Manager . |
| Note | For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Administration Guide for Cisco Unified Communications Manager . |
| Cisco Unified Serviceability Administration Guide | Use Cisco Unified Serviceability to configure alarms, traces, and SNMP for Cisco Unified Communications Manager and the IM
                                 and Presence Service. This document also describes how to activate, start, and stop feature and network services. Serviceability Administration 12.5(1) Serviceability Administration 12.5(1)SU1 |
| Cisco Unified Real-Time Monitoring Tool Administration Guide | Use this guide to install and use the Cisco Unified Real-Time Monitoring Tool to monitor the real-time behavior of system
                                 components for Cisco Unified Communications Manager and IM and Presence Service. Real-Time Monitoring Tool Administration Guide 12.5(1) Real-Time Monitoring Tool Administration Guide 12.5(1)SU3 Real-Time Monitoring Tool Administration Guide 12.5(1)SU4 |
| Managed Services Guide | Use this guide to monitor and maintain service provider networks, including the monitoring of system health, SNMP traps and
                                 syslog messages, MIBs, Cisco Unified Serviceability alerts and alarms, CiscoLog messages, and Cisco Unified Real-Time Monitoring
                                 Tool traces, perfmons, and alerts. |
| Command Line Interface Reference Guide | Refer to this guide for the Command Line Interface (CLI) commands that are available for a Cisco Unified Communications Solution. |
| Jabber for Everyone Quick Start Guide | Jabber for everyone makes Cisco Jabber presence and instant messaging (IM) available at a small end user cost for customers
                                 who have deployed Cisco Unified Communications Manager for all or part of their organization. This document describes the necessary steps required for deployment of Cisco Jabber. This is a quick start guide and will
                                 not cover any of the advanced features supported by Cisco Jabber. |

| Note | 12.5(1)SU4-SU7 is now a consolidated guide. |
|---|---|

| Note | For 12.5(1)SU1 and later, this book is deprecated. Existing content is moved to the Administration Guide for Cisco Unified Communications Manager . |
|---|---|