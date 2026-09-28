---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-217871-troubleshoot-expressway-connector-host-h-htm-211202cd5a
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217871-troubleshoot-expressway-connector-host-h.html
retrieved_at: 2026-08-16T15:44:01.398781+00:00
---

Troubleshoot Expressway Connector with Exchange - Error Code 401

# Troubleshoot Expressway Connector with Exchange - Error Code 401

### Download Options

Updated: May 5, 2022

Document ID: 217871

Contents

## Contents

## Introduction

This document describes identification and remediation of Expressway Connector with the error status Exchange server HTTP error code 401 from the GUI.

## Prerequisites

### Requirements

- Webex Control Hub Organization.

- Hybrid Calendar with Exchange service

- Expressway Connector (X12.5 at a minimum for new deployments)

https://help.webex.com/en-us/article/ruyceab

### Components Used

The information in this document is based on these software and hardware versions:

- Hybrid Calendar activated. In this guide, use Hybrid Calendar with Exchange.

- Exchange Server 2019 Standard.

- Expressway-C X14.0.5.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Symptom

### Expressway-C GUI

Navigate to Applications > Hybrid Services > Calendar Service > Calendar Connector Status . The Collaboration On-Premises displays message status error: Exchange server http error code 401 .

### Troubleshoot

The loggingsnapshot.txt file is needed to locate the timestamp of the error from the Expressway server. If no logs are collected, Diagnostic Logs are needed while the issue is replicated.

With the logs collected, extract the files and locate loggingsnapshot.txt file.

diagnostic_log_ccnp-expressway-hybrid1_2022-02-21_16 03 39.tar.gz

Search for this output:

```
2022-02-21T10:00:15.018-06:00 localhost UTCTime="2022-02-21 16:00:15,017" Module="hybridservices.c_cal" Level="ERROR" Thread="ews-recovery-2" TrackingId="" Detail="checkServiceEntityConnectivity() threw ServiceRequest exception. Root cause exception: microsoft.exchange.webservices.data.HttpErrorException: The remote server returned an error: (401)Unauthorized "
```

(401)Unauthorized means the impersonation account password is invalid, possibly expired, or changed.

### Confirm Imprersonation Account

Verify that the impersonation account is able to access the user interface in Outlook on the web (formerly known as Outlook Web App). Confirm that the password is expired.

OWA URL:

```
https://<IPv4_FQDN_MXS>/owa
```

## Solution

Change the password of the account and update the Calendar Connector configuration to bring the Hybrid Calendar back to Operational. Make the change from the OWA portal or update the password from Active Directory if the account is synchronized from there (out of scpe for this document).

### Reset Mailbox Password via Exchange Admin Center (EAC)

In order to have this option available these commands needs to be run from Exchange Management Shell.

- Add-Pssnapin microsoft* - Install-CannedRbacRoles - Install-CannedRbacRoleAssignments

Enable the Reset Password option in the Exchange Admin Center.

1. Log in to Exchange Admin Center, navigate to Permissions>Organization Management , and click Edit . 2. In the Organization Management page, click + option under the Roles section (to add a new role). 3. Select the Reset Password from the provided list, click the Add option, and then click Save . 4. When the changes are saved, sign out from the Exchange Admin Center and log in again.

To confirm if the role is properly activated, run the command:

- Get-ManagementRole -id "Reset Password" | fl

Select a user mailbox, click Edit to view its properties, and find the Reset Password option.

### Reset Mailbox Password via Exchange Management Shell

It is possible to reset a password via CLI, however, the old password is required to run the command:

```
Set-Mailbox -Identity " User " -OldPassword (ConvertTo-SecureString -string " OldPassword " -AsPlainText -Force) -NewPassword (ConvertTo-SecureString -string " NewPassword " -AsPlainText -Force)
```

that is:

```
Set-Mailbox -Identity " e mail address" -OldPassword (ConvertTo-SecureString -string "Webex4Ever" -AsPlainText -Force) -NewPassword (ConvertTo-SecureString -string "Webex4Ever&Ever" -AsPlainText -Force)
```

### Validate the new Password from OWA

The impersonation account is now able to access the user interface in Outlook on the web (formerly known as Outlook Web App) with the updated credentials.

### Update the Calendar Connector configuration

From Applications > Hybrid Services > Calendar Service > Microsoft Exchange Configuration > Credentials ; update the Service Account Password with the newest password.

Save the configuration at the bottom of the page.

Restart (Disable/Enable) the Calendar Connector to finish the process.

The Calendar Connector service is back to Operational and Users are fully Activated.

## Common Issues

### Unable to add Reset Password Roles to Organization Management.

The delegation permissions have not been applied correctly to the Role Group. R un this command from Exchange server CMD.

```
Setup /p
```

Restart the Exchange server and attempt Reset Password again.

## References

Deployment Guide for Cisco Webex Hybrid Calendar Service

Supported Versions of Expressway for Webex Hybrid Services Connectors

Resource Groups for Cisco Webex Hybrid Services

Upgrade the Connector Host Expressway used for your Hybrid Services

Hybrid Calendar Service Release Notes

Automatic Upgrades for Hybrid Services Resources

### Revision History

1.0

12-May-2022

Initial Release

### Contributed by Cisco Engineers

Josue Vizcaino

Cisco TAC Engineer

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 12-May-2022 | Initial Release |