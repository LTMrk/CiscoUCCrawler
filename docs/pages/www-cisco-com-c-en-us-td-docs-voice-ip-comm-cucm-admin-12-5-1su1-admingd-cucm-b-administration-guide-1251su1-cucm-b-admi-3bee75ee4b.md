---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su1-admingd-cucm-b-administration-guide-1251su1-cucm-b-admi-3bee75ee4b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU1/adminGd/cucm_b_administration-guide-1251SU1/cucm_b_administration-guide-1251SU1_chapter_0100100.html
retrieved_at: 2026-08-21T08:33:08.527693+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

# Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

Updated: April 8, 2025

Chapter: Serviceability Connector

## Chapter: Serviceability Connector

# Serviceability Connector

## Serviceability Connector Overview

You can ease the collection of logs with the Webex Serviceability service. The service
                           automates the tasks of finding, retrieving, and storing diagnostic logs and information.

This capability uses the Serviceability Connector deployed on your premises.
                           Serviceability Connector runs on a dedicated host in your network ('connector host').
                           You can install the connector on either of these components:

Enterprise Compute Platform (ECP)—Recommended

ECP uses Docker containers to isolate, secure, and manage its services. The host
                                 and the Serviceability Connector application install from the cloud. You don’t
                                 need to manually upgrade them to stay current and secure.

Important

We recommend use of ECP. Our future development will focus on this platform.
                                             Some new features won't be available if you install the Serviceability
                                             Connector on an Expressway.

Cisco Expressway

You can use the Servicability Connector for these purposes:

Automated log and system information retrieval for service requests

Log collection of your Unified CM clusters in a Cloud-Connected UC deployment

You can use the same Serviceability Connector for both use cases.

## Benefits of Using Serviceability Service

The service offers these benefits:

Speeds up the collection of logs. TAC engineers can retrieve relevant logs as
                                 they perform the diagnosis of the problem. They can avoid the delays of
                                 requesting extra logs and waiting for their manual collection and delivery. This
                                 automation can take days off your problem resolution time.

Works with TAC’s Collaboration Solution Analyser and its database of diagnostic
                                 signatures. The system automatically analyses logs, identifies known issues, and
                                 recommends known fixes or workarounds.

## Differences to Other Hybrid Services

You deploy and manage Serviceability Connectors through Control Hub like other Expressway-based
                           Hybrid Services, such as Hybrid Calendar Service and Hybrid Call Service. But, there are
                           important differences.

This service doesn’t have features for users. The TAC is the predominant user of this service.
                           While it can benefit organizations that use other Hybrid Services, organizations that
                           don’t use other Hybrid Services are its common users.

If you already have your organization configured in Control Hub, you can enable the service
                           through your existing organization administrator account.

The Serviceability Connector has a different load profile from connectors that provide features
                           directly to users. The connector is always available, so that TAC can collect data when
                           necessary. But, it doesn’t have a steady load over time. The TAC representatives
                           manually initiate data collection. They negotiate an appropriate time for the collection
                           to minimize the impact on other services provided by the same infrastructure.

## Short Description of How it Works

Your administrators work with Cisco TAC to deploy Serviceability service. See Deployment Architecture for TAC Case .

TAC learns of a problem with one of your Cisco devices (when you open a case).

TAC representative uses the Collaborations Solution Analyzer (CSA) web interface to request Serviceability Connector to collect
                                 data from relevant devices.

Your Serviceability Connector translates the request into API commands to collect
                                 the requested data from the managed devices.

Your Serviceability Connector collects, encrypts, and uploads that data over an encrypted link to Customer eXperience Drive
                                 (CXD), and associates the data with your Service Request.

The data is analyzed against the TAC database of more than 1000 diagnostic
                                 signatures.

The TAC representative reviews the results, checking the original logs if necessary.

## Deployment Architecture for TAC Case

Element

Description

Managed devices

Includes any devices that you want to supply logs from to Serviceability Service. You can add up to 150 locally managed devices
                                       with one Serviceability connector. You can import information from HCM-F (Hosted Collaboration Mediation Fulfillment) about
                                       HCS customers' managed devices and clusters (with larger numbers of devices, see https://help.webex.com/en-us/142g9e/Limits-and-Bounds-of-Serviceability-Service ).

The service currently works with the following devices:

Hosted Collaboration Mediation Fulfillment (HCM-F)

Cisco Unified Communications Manager

Cisco Unified CM IM and Presence Service

Cisco Expressway Series

Cisco TelePresence Video Communication Server (VCS)

Cisco Unified Contact Center Express (UCCX)

Cisco Unified Border Element (CUBE)

Cisco BroadWorks Application Server (AS)

Cisco BroadWorks Profile Server (PS)

Cisco BroadWorks Messaging Server (UMS)

Cisco BroadWorks Execution Server (XS)

Cisco Broadworks Xtended Services Platform (XSP)

Your administrator

Uses Control Hub to register a connector host and enable
                                       Serviceability Service. The URL is https://admin.webex.com and you need your “organization
                                       administrator” credentials.

Connector host

An Enterprise Compute Platform (ECP) or Expressway that hosts the
                                       Management connector and the Serviceability Connector.

Management Connector (on ECP or Expressway) and the
                                             corresponding Management Service (in Webex) manage your
                                             registration. They persist the connection, update connectors
                                             when required, and report status and alarms.

Serviceability Connector —A small application that the
                                             connector host (ECP or Expressway) downloads from Webex
                                             after you enable your organization for Serviceability
                                             service.

Proxy

(Optional) If you change the proxy configuration after starting
                                       Serviceability Connector, then also restart the Serviceability
                                       Connector.

Webex cloud

Hosts Webex, Webex calling, Webex meetings, and Webex Hybrid
                                       Services.

Technical Assistance Center

Contains:

TAC representative using CSA to communicate with your
                                             Serviceability Connectors through Webex cloud.

TAC case management system with your case and associated logs
                                             that Serviceability Connector collected and uploaded to
                                             Customer eXperience Drive.

## TAC Support for Serviceability Connector

For more details on Serviceability Connector, see https://www.cisco.com/go/serviceability or contact your TAC representative.

| Important | We recommend use of ECP. Our future development will focus on this platform.
                                             Some new features won't be available if you install the Serviceability
                                             Connector on an Expressway. |
|---|---|

| Element | Description |
|---|---|
| Managed devices | Includes any devices that you want to supply logs from to Serviceability Service. You can add up to 150 locally managed devices
                                       with one Serviceability connector. You can import information from HCM-F (Hosted Collaboration Mediation Fulfillment) about
                                       HCS customers' managed devices and clusters (with larger numbers of devices, see https://help.webex.com/en-us/142g9e/Limits-and-Bounds-of-Serviceability-Service ). The service currently works with the following devices: Hosted Collaboration Mediation Fulfillment (HCM-F) Cisco Unified Communications Manager Cisco Unified CM IM and Presence Service Cisco Expressway Series Cisco TelePresence Video Communication Server (VCS) Cisco Unified Contact Center Express (UCCX) Cisco Unified Border Element (CUBE) Cisco BroadWorks Application Server (AS) Cisco BroadWorks Profile Server (PS) Cisco BroadWorks Messaging Server (UMS) Cisco BroadWorks Execution Server (XS) Cisco Broadworks Xtended Services Platform (XSP) |
| Your administrator | Uses Control Hub to register a connector host and enable
                                       Serviceability Service. The URL is https://admin.webex.com and you need your “organization
                                       administrator” credentials. |
| Connector host | An Enterprise Compute Platform (ECP) or Expressway that hosts the
                                       Management connector and the Serviceability Connector. Management Connector (on ECP or Expressway) and the
                                             corresponding Management Service (in Webex) manage your
                                             registration. They persist the connection, update connectors
                                             when required, and report status and alarms. Serviceability Connector —A small application that the
                                             connector host (ECP or Expressway) downloads from Webex
                                             after you enable your organization for Serviceability
                                             service. |
| Proxy | (Optional) If you change the proxy configuration after starting
                                       Serviceability Connector, then also restart the Serviceability
                                       Connector. |
| Webex cloud | Hosts Webex, Webex calling, Webex meetings, and Webex Hybrid
                                       Services. |
| Technical Assistance Center | Contains: TAC representative using CSA to communicate with your
                                             Serviceability Connectors through Webex cloud. TAC case management system with your case and associated logs
                                             that Serviceability Connector collected and uploaded to
                                             Customer eXperience Drive. |