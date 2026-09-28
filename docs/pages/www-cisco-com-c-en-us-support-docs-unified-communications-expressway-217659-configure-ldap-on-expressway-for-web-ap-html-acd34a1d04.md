---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-217659-configure-ldap-on-expressway-for-web-ap-html-acd34a1d04
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217659-configure-ldap-on-expressway-for-web-ap.html
retrieved_at: 2026-08-16T15:42:07.860916+00:00
---

Configure LDAP on Expressway for Web, API and CLI Access

# Configure LDAP on Expressway for Web, API and CLI Access

### Download Options

Updated: January 26, 2022

Document ID: 217659

Contents

## Contents

## Introduction

This document describes the steps needed to enable Lightweight Directory Access Protocol (LDAP) on Expressway server and how to enable Administrator Groups to access via Web, Application Programming Interface (API) and Command Line Interface (CLI) to Expressway with your domain users.

Contributed by Jefferson Madriz and Elias Sevilla, Cisco TAC Engineers.

## Prerequisites

### Requirements

- Basic knowledge on Expressway.

- Expressway basic configuration already done.

- Active Directory (AD) already configured.

- Firewall rules ready, to allow communication between Expressway and AD server.

### Components Used

- Active Directory installed on Window Server 2016.

- Expressway-C server on version X14.0.3.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

### LDAP Configuration

The LDAP configuration page Users > LDAP configuration is used to configure an LDAP connection to a remote directory service for administrator account authentication.

- Remote account authentication: This section allows you to enable or disable the use of LDAP for remote account authentication.

- Local only: Credentials are verified against a local database stored on the system. - Remote only: Credentials are verified against an external credentials directory. - Both: Credentials are verified first against a local database stored on the system, and then if there's no match with the account then the external credentials directory is used instead.

- LDAP server configuration: this section specifies the connection details to the LDAP server.

FQDN address resolution:

- SRV record: Domain Name Service (DNS) Service Record (SRV) lookup.

- Address record: DNS A or AAAA record lookup.

- IP address: entered directly as an IP address.

Note : If you use SRV records, ensure that _ldap._tcp. records use the standard LDAP port 389. The Expressway does not support other port numbers for LDAP.

Host name and Domain:

- SRV record: only the Domain portion of the server address is required.

- Address record: enter the Host name and Domain. These are then combined to provide the full server address for the DNS address record lookup.

- IP address: the Server address is entered directly as an IP address.

Port:

- The IP port to use on the LDAP server.

Encryption:

- TLS: uses Transport Layer Security (TLS) encryption for the connection to the LDAP server.

- Off: no encryption is used.

- Authentication configuration: this section specifies the Expressway's authentication credentials to use to bind to the LDAP server.

Bind DN: The Distinguished Name (DN), case insensitive, used by the Expressway to bind to the LDAP server. It is important to specify the DN in the order cn=, then ou=, then dc=

Note : The bind account is usually a read-only account with no special privileges.

Bind password: The password (case sensitive) used by the Expressway to bind to the LDAP server.

SASL: The Simple Authentication and Security Layer (SASL) mechanism to use to bind to the LDAP server

- None: no mechanism is used.

- DIGEST-MD5: the DIGEST-MD5 mechanism is used.

Bind username: Username of the account that the Expressway uses to log in to the LDAP server (case sensitive).

- Directory configuration: This section specifies the base distinguished names to use to search for account and group names.

Base DN for accounts: The Organizational Unit (OU) and Domain Controller (DC) definition of the Distinguished Name where a search for user accounts starts in the database structure (case insensitive).

The Base DN for accounts and groups must be at or under the DC level (include all dc= values and ou= values if necessary). LDAP authentication does not look into sub DC accounts, only lower OU and Common Nane (CN) levels.

Base DN for groups: The OU and DC definition of the Distinguished Name where a search for groups must start in the database structure (case insensitive).

If no Base DN for groups is specified, then the Base DN for accounts is used for both groups and accounts.

Nested subgroup search depth: Used to limit the depth of groups for the LDAP search.

Skip looking up all the members: Used to disable or enable member lookup of an administrator group while the authentication search process is made. The default is Yes - skip the member lookup .

### How to Find Base DN

On AD server, open Command Prompt (CMD) as administrator and run the command: dsquery user -name <Known username> .

### LDAP Configuration Example

Administrator authentication source is set to Both and SASL is set to None in this example.

Verify LDAP Status

Validate the LDAP Server Connection Status:

- Available : No error messages are displayed

- Failed : Error messages are displayed. LDAP Error Messages

### Administrator Groups Configuration

The Administrator groups page Users > Administrator groups lists all the administrator groups that have been configured on the Expressway, and lets you add, edit and delete groups.

Note : Administrator groups only apply if Remote Account Authentication Using LDAP is enabled.

When you log in to the Expressway web interface, your credentials are authenticated against the remote directory service and you are assigned the access rights associated with the group to which you belong.

### Administrator Groups Configuration Options on Expressway

Name: The name of the administrator group. The group names defined in the Expressway must match the group names that have been set up in the remote directory service to manage administrator access to this Expressway.

Access level:

- Read-write: Allows all configuration information to be viewed and changed. This provides the same rights as the default admin account.

- Read-only: Allows status and configuration information to be viewed only and not changed. Some pages, such as the Upgrade page, are blocked to read-only accounts.

- Auditor: Allows access to the Event Log, Configuration Log, Network Log, Alarms and Overview pages only .

- None: No access is allowed

Web access: Determines whether members of this group are allowed to log in to the system with the web interface.

API access: Determines whether members of this group are allowed to access the system's status and configuration with the API.

CLI access: Determines whether members of this group are allowed to access the system via CLI.

State: Indicates if the group is enabled or disabled.

### Administrator Group Configuration on AD

1. Create a new Object Gruop , on the folder you like to store the users.

2. Assign a name the the Gruop Name.

Assign the group configured to the user or users that needs to access Expressways via Web, API or CLI. In this case the user is testuser.

1. Open the user properties, navigate to the Member Of tab,Select Add

2. Search for the Group Name created before .

3. Then select OK .

At this point user is memeber of Domain Users and ExpresswayAdmin .

### Administrator Group Configuration on Expressway

Once configuration is done, on Expressway navigate to Users > Administrator groups , select New

Name : must match with Group name configure and associated to the LDAP user that needs to access the Expressway. In this example the Group name is ExpresswayAdmin , so the new Administrator Group name is ExpresswayAdmin .

This group has all permissions and access available.

Select Save .

## Verify

Log out and try to access via Web with the LDAP user that has the Administrator Group associated. In this example the user created is testuser.

This can be confirmed via Status > Event log :

### Revision History

1.0

26-Jan-2022

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 26-Jan-2022 | Initial Release |