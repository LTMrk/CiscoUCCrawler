---
doc_id: developer-cisco-com-docs-cisco-emergency-responder-configuration-api-v15su1-230a1cedd8
source_url: https://developer.cisco.com/docs/cisco-emergency-responder-configuration-api-v15su1/
retrieved_at: 2026-08-24T22:11:43.209544+00:00
---

# Cisco Emergency Responder Configuration API v15su1

The Cisco Emergency Responder Configuration API supports create/read/update/delete access to several CER objects, including:

CER user/group management

Emergency Response Location (ERL) management for:

Manual/unlocated phones

Switch ports

Wireless access points

IP subnets

CUCM connection settings

IP Subnet API

These capabilities enable integration of CER configuration management into customer-developed or third-party automation scripts, tools, and solutions.

Explore the API reference for details.

## About the Product - Cisco Emergency Responder (CER)

Cisco Emergency Responder (CER) enhances the existing emergency 9-1-1 functionality offered by Cisco Unified Communications Manager. It assures that Cisco Unified Communications Manager will send emergency calls to the appropriate Public Safety Answering Point (PSAP) for the caller's location, and that the PSAP can identify the caller's location and return the call if necessary. In addition, the system automatically tracks and updates equipment moves and changes. Deploying this capability helps ensure more effective compliance with legal or regulatory obligations, reducing the risk of liability related to emergency calls as a result.

To learn more about CER, see the Cisco Emergency Responder product page.

Note: The CER Configuration API is available in CER versions 14+

The CER Configuration API is based on the REST pattern, supporting read and write operations via HTTP GET , POST , PUT and DELETE methods.

## Use Cases

- Automation of phone ERL-ELIN mapping/configuration based on triggers in other software; for example when adding new end-users/phones to the system, applications can configure CER services automatically.

- Building reporting/auditing tools providing insight into enterprise E911 readiness; for example by retrieving CER configurations, comparing to installed/active phones in the network, and identifying and/or automatically correcting phones without coverage.

- Automate management of CER admin user and role assignment; for example via integration with third-party employee management solutions.  Reporting/auditing/verification of CER admin user access.

- Making branch/site build-outs faster and reducing error by automating CER/CUCM connection configuration.

- Automating bulk CER configuration; for example during system migration, installation, or phone equipment upgrades.

## API Capabilities

The CER Configuration API is itended to enable automate management of basic, frequently modified CER configurations.  However, it does not support all configurations that are possible via the standard Administrative web pages and tools.

Operations not available via the API include:

- User/Group Credential Policy and Enhanced Security Mode Credential Policy

- Management of Off-Premise / Intrado ERLs

- ERL Migration

- ERL assignment for synthetic phones

- CUCM AXL connectivity testing

# Technical Overview

CER Configuration Architecture

Note: The CER Configuration API service is automatically enabled on the Publisher (only) in a CER cluster.

The CER Configuration API provides applications with create/read/update/delete capabilities in several CER configuration areas:

## User Management

User Management involves managing users, user groups and roles associated with the CER Product. Users obtain Cisco Emergency Responder system and API access privileges via the roles that are associated to the access groups of which the user is a member. Each role contains a set of permissions that is attached to a specific resource or application, such as Access Points or Audit Log.

## CUCM Cluster Management

Refers to the Cisco Unified Communication Manager configuration in CER. This configuration establishes the target CUCM cluster(s) for which CER will provide E911 services, and identifies the CUCM CTI/AXL application user accounts for use by the CER connection.

## ERL - ELIN Management

ERL refers to “Emergency Response Location” a specific physical area within which a 911 caller can be located by response personnel in a timely fashion.
ELIN refers to “Emergency Line Identification Number” also called “pseudo-ANI”, the PSTN-routable number sent as the CPN for all 911 calls from an ERL.

## IPSubnet

Refers to the IPSubnet configuration in CER. This configuration API helps in adding, deleting and Updating IPSubnets in Cisco Emergency Responder. This IPSubnet API is supported for CER Versions >= 14SU3.

## REST Capabilities

The CER Configuration API supports read and write operations using HTTP GET , POST , PUT , and DELETE methods.

No HTTP body is expected for GET requests. Other HTTP methods ( POST / PUT / DELETE ) may require a message body in appropriate format.

Note: All requests should be made using HTTPS/TLS v1.3+

## Request/Response Data Content-Types

The CER Configuration API can accept and return data in several formats, depending on the Content-Type and Accept headers present in the application HTTP request:

Supported Content-Types

## High Request Rate Performance

Currently there are no enforced API rate throttling mechanisms implemented for the CER Configuration API. Applications should take care to avoid making a high number of requests in a short period of time, and plan to cache frequently accessed data.

It is highly recommended that scenarios involving high application CER Configuration API request rates be fully tested while monitoring CER platform performance metrics before deploying to production sites.

## Cisco Emergency Responder (Read-Only) API

CER also supports a separate read-only API for retrieving additional CER configuration details.  This API is supported for CER versions <= v14.

For more information, refer to the CER API Documentation .

Next

| Format | Mime Type |
|---|---|
| Text | text/plain (response only) |
| XML | application/xml |
| JSON | application/json |