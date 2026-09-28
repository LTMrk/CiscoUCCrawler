---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-14su2-english-administration-guide-cer0-b-cisco-emergency-responder-admi-495cd59c16
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/14su2/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-14su2/cer0_m_cisco-emergency-responder-api-documentation.html
retrieved_at: 2026-08-20T23:53:37.435569+00:00
---

Cisco Emergency Responder Administration Guide for Release 14 and SUs

# Cisco Emergency Responder Administration Guide for Release 14 and SUs

Updated: January 9, 2025

Chapter: Cisco Emergency Responder API Documentation

## Chapter: Cisco Emergency Responder API Documentation

- Cisco Emergency Responder API Documentation

- Role Permissions for Different API

# Cisco Emergency Responder API Documentation

## API Configuration Overview

Cisco Emergency Responder offers a suite of Application Programming Interface (APIs) through which client applications can
                           be integrated to access the server data and managing functionalities.

These APIs provide users the flexibility to manage their network or their customers’ networks by providing services and make
                           them available to their end users. Partners can easily integrate these APIs with their internal tools, systems, and applications.
                           Using industry-standard authentication and role-based authorization, these APIs provide a trusted scalable platform to support
                           multiple deployment models.

APIs are introduced to better manage users and their roles remotely, and ELIN/ERL Management. Also, to ease interoperability
                           with Cisco Unified Communications Manager. For more information on the APIs and their configuration, see the following:

Release 14 and SUs— Cisco Emergency Responder (CER) API Documentation

### Role Permissions for Different API

Users obtain Cisco Emergency Responder system API access privileges via the roles that are associated to the access groups
                                 of which the user is a member. Each role contains a set of permissions that is attached to a specific resource or application,
                                 such as Access Points or Audit Log Configuration.

For a user who has Role Permissions as "ERL", the role may contain permission that allows the user to view or edit the Conventional
                                 ERL using APIs available in the application. In this case, the ERL can be created, updated, and deleted using the corresponding
                                 APIs.

Following table lists all the available resources in Cisco Emergency Responder API documentation and their access privileges
                                 information:

Resource Permissions

Access Criteria

Access Point

Access to CER System Administrator and access to Access Points tab

Add Subscriber

Access to CER System Administrator and access to Add Subscriber

ALI Formatting Tool

Access to CER System Administrator and access to ALI Formatting Tool

All Logs

Access to CER Serviceability and able to see all logs of CER

Audit Log Configuration

Access to CER Serviceability and change Audit Log Configuration

Call History

Access to CER System Administrator and access to Call History

Call Manager Details

Access to CER System Administrator and access to Call Manager Details

CER Groups in Cluster

Access to CER System Administrator and access to CER Groups in Cluster

Cluster DB Host setting

Access to admin utility page and Update Cluster DB Host Details

Control Centre

Access to CER Serviceability page and access control centre

CPU & Memory Usage

Access to CER Serviceability page and access to CPU And Memory Usage

Device SNMP Settings

Access to CER System Administrator and access to Device SNMP Settings

Disk Usage

Access to CER Serviceability page and access to Disk Usage

ERL

Access to CER System Administrator and access to conventional ERL

ERL Audit Trail

Access to CER System Administrator and access to ERL Audit Trail

ERL Debug Tool

Access to CER System Administrator and access to ERL Debug Tool

ERL Migration

Access to CER System Administrator and access to ERL Migration

Event Viewer

Access to CER Serviceability page and access to Event Viewer

File Management Utility

Access to CER System Administrator and access to File Management Utility

Functional role

Access to create, read, update, delete Role details

National E911 Service Provider ERL

Access to CER System Administrator and access to National E911 Service Provider ERL

IP Subnet

Access to CER System Administrator and access to IP Subnet

License Management

Access to CER System Administrator and access to License Management

Mail Alert Configurations

Access to CER System Administrator and access to Mail Alert Configurations

Manually Configured Phones

Access to CER System Administrator and access to Manually Configured Phones

Change CCM Version

Access to admin utility page and Change CCM version

Off-Premises ERL

Access to CER System Administrator and access to Off-Premises ERL

OnsiteContact

Access to CER System Administrator and access to OnsiteContact

Pager and Email Alert Configurations

Access to CER System Administrator and access to Pager and Email Alert Configurations

Phone Search

Access to CER User and access to Phone search

Processes

Access to CER Serviceability page and access to Processes

PS ALI Convert

Access to CER System Administrator and access to PS ALI Convert

PS ALI Export

Access to CER System Administrator and access to PS ALI Export

Purge

Access to CER System Administrator and access to Purge

Run Tracking

Access to CER System Administrator and access to Run Tracking

Saml Sso

Access to CER System Administrator and access to Saml Sso

Tracking Schedule

Access to CER System Administrator and access to Schedule

Server

Access to CER System Administrator and access to Server settings

Server Group

Access to CER System Administrator and access to Server Group

MIB2 system group configuration

Access to CER Serviceability page and access to system group configuration

SNMP V1/V2c configuration

Access to CER Serviceability page and access to SNMP V1/V2c configuration

SNMP v3 configuration

Access to CER Serviceability page and access to SNMP v3 configuration

LAN Switches

Access to CER Serviceability page and access to LAN Switches

Switch Port

Access to CER System Administrator and access to Switch Port

Synthetic Phone

Access to CER System Administrator and access to Synthetic Phone

Telephony

Access to CER System Administrator and access to Telephony

Unlocated Phones

Access to CER System Administrator and access to Unlocated Phones

Application User

Access to CER System Administrator and access to User management

User Setting

Access to create, read, update, delete User details

User Call History

Access to CER User and access to User Call History

User Group

Access to create, read, update, delete User Group details

National E911 Service Provider VUI Settings

Access to CER System Administrator and access to National E911 Service Provider VUI Settings

Web Alert

Access to CER User and access to Web Alert

| Resource Permissions | Access Criteria |
|---|---|
| Access Point | Access to CER System Administrator and access to Access Points tab |
| Add Subscriber | Access to CER System Administrator and access to Add Subscriber |
| ALI Formatting Tool | Access to CER System Administrator and access to ALI Formatting Tool |
| All Logs | Access to CER Serviceability and able to see all logs of CER |
| Audit Log Configuration | Access to CER Serviceability and change Audit Log Configuration |
| Call History | Access to CER System Administrator and access to Call History |
| Call Manager Details | Access to CER System Administrator and access to Call Manager Details |
| CER Groups in Cluster | Access to CER System Administrator and access to CER Groups in Cluster |
| Cluster DB Host setting | Access to admin utility page and Update Cluster DB Host Details |
| Control Centre | Access to CER Serviceability page and access control centre |
| CPU & Memory Usage | Access to CER Serviceability page and access to CPU And Memory Usage |
| Device SNMP Settings | Access to CER System Administrator and access to Device SNMP Settings |
| Disk Usage | Access to CER Serviceability page and access to Disk Usage |
| ERL | Access to CER System Administrator and access to conventional ERL |
| ERL Audit Trail | Access to CER System Administrator and access to ERL Audit Trail |
| ERL Debug Tool | Access to CER System Administrator and access to ERL Debug Tool |
| ERL Migration | Access to CER System Administrator and access to ERL Migration |
| Event Viewer | Access to CER Serviceability page and access to Event Viewer |
| File Management Utility | Access to CER System Administrator and access to File Management Utility |
| Functional role | Access to create, read, update, delete Role details |
| National E911 Service Provider ERL | Access to CER System Administrator and access to National E911 Service Provider ERL |
| IP Subnet | Access to CER System Administrator and access to IP Subnet |
| License Management | Access to CER System Administrator and access to License Management |
| Mail Alert Configurations | Access to CER System Administrator and access to Mail Alert Configurations |
| Manually Configured Phones | Access to CER System Administrator and access to Manually Configured Phones |
| Change CCM Version | Access to admin utility page and Change CCM version |
| Off-Premises ERL | Access to CER System Administrator and access to Off-Premises ERL |
| OnsiteContact | Access to CER System Administrator and access to OnsiteContact |
| Pager and Email Alert Configurations | Access to CER System Administrator and access to Pager and Email Alert Configurations |
| Phone Search | Access to CER User and access to Phone search |
| Processes | Access to CER Serviceability page and access to Processes |
| PS ALI Convert | Access to CER System Administrator and access to PS ALI Convert |
| PS ALI Export | Access to CER System Administrator and access to PS ALI Export |
| Purge | Access to CER System Administrator and access to Purge |
| Run Tracking | Access to CER System Administrator and access to Run Tracking |
| Saml Sso | Access to CER System Administrator and access to Saml Sso |
| Tracking Schedule | Access to CER System Administrator and access to Schedule |
| Server | Access to CER System Administrator and access to Server settings |
| Server Group | Access to CER System Administrator and access to Server Group |
| MIB2 system group configuration | Access to CER Serviceability page and access to system group configuration |
| SNMP V1/V2c configuration | Access to CER Serviceability page and access to SNMP V1/V2c configuration |
| SNMP v3 configuration | Access to CER Serviceability page and access to SNMP v3 configuration |
| LAN Switches | Access to CER Serviceability page and access to LAN Switches |
| Switch Port | Access to CER System Administrator and access to Switch Port |
| Synthetic Phone | Access to CER System Administrator and access to Synthetic Phone |
| Telephony | Access to CER System Administrator and access to Telephony |
| Unlocated Phones | Access to CER System Administrator and access to Unlocated Phones |
| Application User | Access to CER System Administrator and access to User management |
| User Setting | Access to create, read, update, delete User details |
| User Call History | Access to CER User and access to User Call History |
| User Group | Access to create, read, update, delete User Group details |
| National E911 Service Provider VUI Settings | Access to CER System Administrator and access to National E911 Service Provider VUI Settings |
| Web Alert | Access to CER User and access to Web Alert |