---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-rel-notes-12-5-1-su3-cucm-b-release-notes-for-cucm-imp-1251su3-cucm-m-a-0270c67e1c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/rel_notes/12_5_1/SU3/cucm_b_release-notes-for-cucm-imp-1251su3/cucm_m_about-this-release.html
retrieved_at: 2026-08-21T01:30:21.752683+00:00
---

Release Notes for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU3

# Release Notes for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU3

## Results

Updated: August 13, 2020

Chapter: About this Release

## Chapter: About this Release

# About this Release

## About Release Notes

This release describes new features, restrictions, and caveats for Cisco Unified Communications Manager (Unified Communications Manager) and Cisco Unified Communications Manager IM and Presence Service (IM and Presence Service) . The release notes are updated for every maintenance release but not for patches or hot fixes.

## Supported Versions

The following software versions apply to Release 12.5(1)SU3:

Unified Communications Manager: 12.5.1.13900-152

IM and Presence Service: 12.5.1.13900-17

### Version Compatibility Between Unified CM and the IM and Presence Service

Version compatibility depends on the IM and Presence Service deployment type. The following table outlines the options and
                                 whether a release mismatch is supported between the telephony deployment and the IM and Presence Service deployment. A release
                                 mismatch, if it is supported, would let you deploy your Unified Communications Manager telephony deployment and your IM and
                                 Presence Service deployment using different releases.

For Release 12.5(1)SU7a, a Unified Communications Manager ES with a build number of 12.5.1.181xx would be considered part
                                             of the 12.5(1)SU7a (12.5.1.18100-x) release.

Deployment Type

Release Mismatch

Description

Standard Deployment of IM and Presence Service

Not supported

Unified Communications Manager and the IM and Presence Service are in the same cluster and must run the same release—a release
                                             mismatch is not supported.

Centralized Deployment of IM and Presence Service

Supported

The IM and Presence Service deployment and the telephony deployment are in different clusters and can run different releases—a
                                             release mismatch is supported.

## Documentation for this Release

For a complete list of the documentation that is available for this release, see the Documentation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1) .

### Documentation Restructure 12.5(1)SU1 and Later

Following is a summary of the documentation restructure effort that was a part of 12.5(1)SU1. For this release and later releases,
                                 many Unified Communications Manager documents were restructured in order to improve usability and to streamline the documentation
                                 set. As part of this effort, one new guide is added, three existing guides are reworked, and five existing guides are deprecated.
                                 This overall effort reduces the size of the Unified Communications Manager documentation suite by four guides.

Restructured Documents

Deprecated Documents

Restructured Documents (Existing) :

New Documents :

Call Reporting and Billing Administration Guide

The following documents are deprecated for 12.5(1)SU1 and later:

Cisco Unified CDR Analysis and Reporting Administration Guide —Material moved to call reporting and billing documentation

Call Detail Records Administration Guide —Material moved to call reporting and billing documentation

Cisco Unified Reporting Administration Guide —Material is now with administration Guide

Cisco Unified Serviceability Administration Guide —Most sections are now in the Administration Guide. CDR Repository Manager and billing server sections are with call reporting
                                                   and billing documentation

Changing the IP Address, Hostname and Domain —Material moved to the Administration Guide

#### System Configuration Guide (Restructured)

As of 12.5(1)SU1, the System Configuration Guide is shortened and streamlined to create a complete post-install system setup. Basic security and SSO configurations are added
                                 to fill out the basic setup, while advanced call processing features are moved to the Feature Configuration Guide . This new guide forms the Unified Communications Manager prerequisite for deploying an advanced Cisco call processing solution.

#### Administration Guide (Restructured)

As of 12.5(1)SU1, the Administration Guide for Cisco Unified Communications Manager is expanded to include consolidated administration information from the Changing the IP Address, Hostname and Domain document, the Cisco Unified Reporting Administration Guide document and many sections from the existing Cisco Unified Serviceability Administration Guide documentation, all of which are deprecated for 12.5(1)SU1 and later.

In addition to the above updates, an overview of troubleshooting information has been inserted into the Administration Guide .

#### Call Reporting and Billing Administration Guide (New document)

This new document simplifies call reporting and billing administration documentation, consolidating existing material from
                                 the documents Cisco Unified CDR Analysis and Reporting Administration Guide and the Call Detail Records Administration Guide , both of which are now deprecated. It also adds CDR Repository and billing server information that was available previously
                                 with the Serviceability documentation. The new guide simplifies the overall structure and provides a clearer setup process:

#### Feature Configuration Guide (Restructured)

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

Headsets Management

Headset Services

Video Endpoints Management

#### Security Guide (Restructured)

The Security Guide is restructured for Release 12.5(1)SU3. The new guide is streamlined and enhanced to make it easy to configure
                                 and deploy security for Unified Communications Manager and registered endpoints. The new guide is split into three sections:

Basic Security —Contains information on how to configure basic security on Unified Communications Manager and on registered endpoints.

User Security —Contains information on how to manage identity, authentication, and user access.

Advanced Security Features —Contains information on how to deploy advanced security features such as FIPS Mode, Enhanced Security Mode, and V.150.

The book also includes enhanced information with new topics on subjects like Security Hardening and Identity Management that
                                 help you make security decisions for your deployment.

#### Push Notifications Deployment for Cisco Jabber on iPhone and iPad (Revised)

This document describes how to configure Push Notifications for Cisco Jabber on iPhone and iPad with Cisco Unified Communications
                                 Manager and the IM and Presence Service. The guide is updated to include Push Notifications support for Cisco Jabber and Cisco
                                 Webex clients that run on both Android devices and iOS devices.

### Open Source Documentation

This guide details the latest licenses and notices for the open source software used in Unified Communications Manager.

For more information on the open source softwares used, see https://www.cisco.com/c/dam/en_us/about/doing_business/open_source/docs/UnifiedCommunicationsManagerOpenSourceGuide1251SU3v10.pdf .

## Installation Procedures

For information on how to install your system, see the Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1) .

## Upgrade Procedures

For information on how to upgrade to this release, see the Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service, Release 12.5(1) .

### Meltdown Vulnerabilities During Upgrade

This release of Unified Communications Manager, Cisco IM and Presence Service, Cisco Emergency Responder, and Cisco Prime
                              Collaboration Deployment contain software patches to address the Meltdown and Spectre microprocessor vulnerabilities.

Before you upgrade to Release 12.5(1) or above, we recommend that you work with your channel partner or account team to use
                              the Cisco Collaboration Sizing Tool to compare your current deployment to an upgraded 12.5(1)SU3 deployment. If required,
                              change VM resources to ensure that your upgraded deployment provides the best performance.

## HAProxy—System Architecture Improvements for Web Traffic

HAProxy is a fast and reliable solution that offers high availability, load balancing, and proxy capabilities for HTTP-based
                           applications. With this release, HAProxy frontends all the incoming web traffic into Unified Communication Manager and IM
                           and Presence Service.

The HAProxy implementation has resulted in the following improvements:

For about 10,000 client logins into Unified Communications Manager, there is an average of 30-40% improvement in the total
                                 time taken for clients to log in to the system.

On an average, for 15,000 IM and Presence Service users, there is a 25-30% improvement in the total time taken for clients
                                 to log in to the system.

The time taken to download the configuration files (includes phones and headset configuration file) for 10,000 devices has
                                 seen an average of 20-25% improvement.

New Performance counters are introduced in Real Time Monitoring Tool (RTMT) for better troubleshooting and monitoring.

Improved Tomcat stability through offloading of crypto functionality.

HAProxy Considerations

Whenever the total CPU utilization crosses the 90% mark, HAProxy may trigger a service alarm along with the other services.

Restart of the Cisco Tomcat service will internally restart the HAProxy service.

| Note | Any respin or ES that is produced between Cisco.com releases is considered part of the previous release. For example, a Unified Communications Manager ES with a build number
                                          of 12.5.1.18[0-2]xx would be considered part of the 12.5(1)SU7 (12.5.1.17900-x) release. For Release 12.5(1)SU7a, a Unified Communications Manager ES with a build number of 12.5.1.181xx would be considered part
                                             of the 12.5(1)SU7a (12.5.1.18100-x) release. |
|---|---|

| Deployment Type | Release Mismatch | Description |
|---|---|---|
| Standard Deployment of IM and Presence Service | Not supported | Unified Communications Manager and the IM and Presence Service are in the same cluster and must run the same release—a release
                                             mismatch is not supported. |
| Centralized Deployment of IM and Presence Service | Supported | The IM and Presence Service deployment and the telephony deployment are in different clusters and can run different releases—a
                                             release mismatch is supported. Note The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                                      This non-telephony node must run the same release as the IM and Presence Service. Note Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onward. | Note | The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                                      This non-telephony node must run the same release as the IM and Presence Service. | Note | Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onward. |
| Note | The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                                      This non-telephony node must run the same release as the IM and Presence Service. |
| Note | Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onward. |

| Note | The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                                      This non-telephony node must run the same release as the IM and Presence Service. |
|---|---|

| Note | Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onward. |
|---|---|

| Restructured Documents | Deprecated Documents |
|---|---|
| Restructured Documents (Existing) : New Documents : Call Reporting and Billing Administration Guide | The following documents are deprecated for 12.5(1)SU1 and later: Cisco Unified CDR Analysis and Reporting Administration Guide —Material moved to call reporting and billing documentation Call Detail Records Administration Guide —Material moved to call reporting and billing documentation Cisco Unified Reporting Administration Guide —Material is now with administration Guide Cisco Unified Serviceability Administration Guide —Most sections are now in the Administration Guide. CDR Repository Manager and billing server sections are with call reporting
                                                   and billing documentation Changing the IP Address, Hostname and Domain —Material moved to the Administration Guide |