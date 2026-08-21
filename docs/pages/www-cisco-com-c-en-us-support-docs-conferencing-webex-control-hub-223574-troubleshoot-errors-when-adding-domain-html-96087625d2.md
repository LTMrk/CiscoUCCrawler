---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-control-hub-223574-troubleshoot-errors-when-adding-domain-html-96087625d2
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-control-hub/223574-troubleshoot-errors-when-adding-domain.html
retrieved_at: 2026-08-21T06:32:17.937600+00:00
---

Troubleshoot Errors When Adding Domain to the Webex Control Hub

# Troubleshoot Errors When Adding Domain to the Webex Control Hub

### Download Options

Updated: October 24, 2025

Document ID: 223574

Contents

## Contents

## Introduction

This document describes fixing an error when adding a domain to the Webex Control Hub using the Add with Azure AD option.

## Prerequisites

### Webex Control Hub EntraID Tenant

You must have the full administrator privileges on the Control Hub and the Global Admin privileges on the EntraID. If you are a partner admin, you need to use a full admin account in the customer org (a customer full admin account).

### Issue

If you are an admin and you attempt to add a domain on the Control Hub using an option Add with Azure AD , this produces an error of "tenantid is required".

## Steps for Admin to Perform

- Log in to admin.webex.com

- Go to Organization settings .

- Go to Domains .

- Click Add with Azure AD .

### Debug Information in the Control Hub

Referrer: Control Hub notification toaster-links Browser URL: https://admin.webex.com/settings Control Hub Build: 20250724-39e9749 View Org ID: *************************Org ID Logged-in User ID: User ID Logged-in User Org ID: Org ID Logged-in User Clock UTC: Wed, 30 Jul 2025 21:50:19 GMT Customer Type: Pending

Status: 401 Status Text: Unauthorized URL: https://identity-b-us.webex.com/extIntegration/azureAD/OrgID/v1/Domains Tracking ID: ATLAS_1c91ac5b-48fa-484b-96b6-ee16cf1fd7c1_67 Error: { "error": { "key": "401", "message": [ { "code": "701018", "description": "Request unauthorized. client-request-id: 1cc7a849-cf30-4105-970e-4efbff9c5aa8" } ] }, "trackingId": "ATLAS_1c91ac5b-48fa-484b-96b6-ee16cf1fd7c1_67" }

Message: Error getting verified domain. The request was unauthorized. Please sign out and try again. TrackingID: ATLAS_1c91ac5b-48fa-484b-96b6-ee16cf1fd7c1_67

## Other Possible Error

Referrer: Control Hub notification toaster-links Browser URL: https://admin.webex.com/settings?type=azure-ad-domain&admin_consent=True&tenant=bae22791-5be6-4d1c-beb8-c4a796921216&orgId=4dc975b6-e02f-476a-9aa3-06ab8e27903c Control Hub Build: 20250620-fce73c1 View Org ID: Org ID Logged-in User ID: User ID Logged-in User Org ID: Org ID Logged-in User Clock UTC: Mon, 23 Jun 2025 17:44:37 GMT Customer Type: Pending

Status: 400 Status Text: Bad Request URL: https://identity-b-us.webex.com/extIntegration/azureAD/OrgID/v1/Domains Tracking ID: ATLAS_84dd5f26-6e16-44e1-8ec0-a91cd9907693_73 Error: { "error": { "key": "400", "message": [ { "code": "100013", "description": "tenantId is required" } ] }, "trackingId": "ATLAS_84dd5f26-6e16-44e1-8ec0-a91cd9907693_73" }

Message: Error getting verified domain. TrackingID: ATLAS_84dd5f26-6e16-44e1-8ec0-a91cd9907693_73

## Troubleshooting

View the HAR capture or available debug information to view this information:

Failed to get domains from Azure AD, org 'OrgID'.

### Keywords to Note in the Debug Information

- Error getting verified domain. The request was unauthorized. Please sign out and try again

- tenantId is required

### Root Cause

Since the Webex Control hub does not have access to the Entra ID, it is failing to get the domain from the Entra and hence needs at least an authentication from the EntraID Admin. Otherwise, having an Azure AD wizard App in place which has an existing handshake to share the EntraID tenant ID with Webex can solve the problem.

### Solution

Set up the Entra ID (Azure AD) Wizard App in Control Hub.

This allows the Control Hub to verify the domain with Azure AD.

### Revision History

2.0

24-Oct-2025

Added a sentence in the Prerequisites section.

1.0

01-Aug-2025

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 24-Oct-2025 | Added a sentence in the Prerequisites section. |
| 1.0 | 01-Aug-2025 | Initial Release |