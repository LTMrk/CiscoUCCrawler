---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-app-221174-configure-an-additional-tenant-to-hybrid-html-9f4a48cb42
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-app/221174-configure-an-additional-tenant-to-hybrid.html
retrieved_at: 2026-08-16T22:03:21.881220+00:00
---

Configure an Additional Tenant to Hybrid Calendar with Office 365

# Configure an Additional Tenant to Hybrid Calendar with Office 365

### Download Options

Updated: November 3, 2023

Document ID: 221174

Contents

## Contents

## Introduction

This document describes how to add a new tenant to an existing Hybrid Calendar deployment with Microsoft 365.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- A Microsoft 365 tenant with Exchange online accounts for users.

- A Webex Organization

Users must have activated Webex accounts, with email addresses that are exact matches in Exchange online (Primary Email Address).

### Components Used

The information in this document is based on these software and hardware versions:

- Control Hub build: 20231031-6eac2ad

- Office 365 E3 licensing

- Google Chrome 115.0.5790.170 x64

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background

Hybrid Calendar with Office 365 now provides the capability to add additional tenants to an existing Hybrid Calendar integration with Office 365.

## Deployment

### Control Hub

To add a new tenant to an existing Hybrid Calendar with Hybrid Calendar with Office 365, navigate to admin.webex.com > Services > Hybrid . On the Hybrid Calendar with Office 365 card, click Edit settings .

Edit settings

On the Integration tab click on Add tenant .

Add tenant

Since the Commercial version of Webex only supports the Worldwide instance of Office 365, click on Authorize to continue.

Authorize

Use an account that can authorize multi-tenant apps (like Global Administrator or Privileged Role Administrator) to grant permission for the setup process.

Admin Sign-In

Accept the read permissions requested for the tenant.

Admin consent

Type an email address to test the connection with Microsoft 365 for the new tenant. Check the box to indicate that your organization needs to be able to schedule meetings from Workspaces if required and click Test .

Test account

When the connection is successful click on Next > Done to exit the wizard. When a connection is not created, verify that the user name you are using has a license on the Microsoft account and try these steps again.

Successful

## Validation

### Control Hub

Navigate to admin.webex.com > Services > Hybrid . On the Hybrid Calendar with Office 365 card, click Edit settings .

Validation

The new tenant with the tenant ID and status is now configured.

New Tenant

## Question & Answers

### Can I have multiple Webex Organizations connected to a single Office 365 tenant?

Yes, this is supported.

### How many different Office 365 tenants are supported in the Cloud-based Calendar?

Currently, it is unlimited.

## Related Information

- Hybrid Calendar Service with Office 365 integration reference

- Deploy cloud-based Hybrid Calendar for Office 365 - Add an additional tenant to Hybrid Calendar with Office 365

- Cisco Technical Support & Downloads

### Revision History

1.0

03-Nov-2023

Initial Release

### Contributed by Cisco Engineers

Josue Jonathan Vizcaino Huape

Cisco Team Captain

### This Document Applies to These Products

- Webex App

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 03-Nov-2023 | Initial Release |