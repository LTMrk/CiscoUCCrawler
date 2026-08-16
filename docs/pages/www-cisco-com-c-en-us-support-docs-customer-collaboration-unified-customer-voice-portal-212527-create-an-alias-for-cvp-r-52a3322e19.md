---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-customer-voice-portal-212527-create-an-alias-for-cvp-r-52a3322e19
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-customer-voice-portal/212527-create-an-alias-for-cvp-reporting-server.html
retrieved_at: 2026-08-16T19:23:12.365090+00:00
---

Create an Alias for CVP Reporting Server DB Instance Name

# Create an Alias for CVP Reporting Server DB Instance Name

Updated: December 5, 2017

Document ID: 212527

Contents

## Contents

## Introduction

This document describes how to create an alias for Cisco Customer  Voice Portal (CVP) reporting server Data Base (DB) instance name, so different reporting server have different alias names.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Unified Customer Voice Portal (CVP)

### Components Used

The information in this document is based on these software and hardware versions:

- CVP 10.X

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

In all CVP Reporting Server Installtion, the the database instance is hardcoded to cvp

Step 1. Create an entry in the %ONCONFIG% file (onconfig.cvp) for DBSERVERALIASES. Something like CVP_1, CVP_2, CVP_3, etc. Rules to follow while creating the Aliases:

a. DBSERVERALIASES must begin with a lowercase letter and can contain other lowercase letters, digits, and underscores. b. DBSERVERALIASES must not include uppercase characters, a field delimiter (space or tab), or a new line character. c. Other characters from the basic ASCII code set are not necessarily reliable. d. For example, a hyphen or minus sign can create problems and a colon might not work reliably. e. The @ character is reserved to separate the database from the server (as in dbase@server).

Step 2. Go to C://Informix/db, edit sqlhost file.  Add <instance name> <PROTOCOL> <hostname> <aliased instance name>

Ex: cvp_1 olsoctcp CVPRTPT cvp_1

Step 3. Edit the %WIN_PATH%/system32/etc/drivers/services and add an entry for that alias (copy the tcp entry for IDS)

Step 4. Create a registry entry under Informix/sqlhosts to match that alias name. Make sure the service name should be same as that of the alias name.

Step 5. Go to Services and Restart the Informix IDS service . After successful service restart verify the DB instances are reflecting as created.

### Revision History

1.0

05-Dec-2017

Initial Release

### Contributed by Cisco Engineers

Ramiro Amaya

Cisco TAC Engineer

Raghavan Ranganathan

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Customer Voice Portal

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 05-Dec-2017 | Initial Release |