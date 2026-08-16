---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-release-gui-b6cbae04e0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/release/guide/rcct_b_cce-solution-rns-12-6/ccvp_m_1261-cisco-unified-customer-voice-portal.html
retrieved_at: 2026-08-16T19:38:09.175019+00:00
---

Release Notes for Cisco Contact Center Enterprise Solutions Release 12.6(1)

# Release Notes for Cisco Contact Center Enterprise Solutions Release 12.6(1)

Updated: May 14, 2021

Chapter: Cisco Unified Customer Voice Portal

## Chapter: Cisco Unified Customer Voice Portal

# Cisco Unified Customer Voice Portal

## New Features

### Edge Chromium Browser Support

This release supports Edge Chromium (Microsoft Edge). For information about supported versions, see the Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

### Virtual Agent–Voice: Onboarding for OEM Customers

Virtual Agent–Voice (VAV), was formerly referred to as Customer Virtual Assistant (CVA) in 12.5(1) release. This feature now
                              provides enhanced onboarding experience to OEM customers (customers who use Cisco's contract, billing, and support for Google's
                              speech services) via Webex Control Hub. OEM customers can use Cisco services coupled with Google’s cloud-based AI-enabled
                              speech services.

For details on how to configure VAV onboarding for OEM customers, see the Virtual Agent–Voice chapter in the following documents:

Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

### Virtual Agent–Voice for Dialogflow CX

Virtual Agent–Voice for Dialogflow CX leverages Google's Dialogflow CX service that allows designing virtual voice agents
                                 and creating and connecting complex IVR call flows.

Using Google Dialogflow CX, multiple agents can be created under the same Project ID and can be accessed and managed for different
                                 lines of business with a single Google account. For more information, refer to the Google Dialogflow CX documentation at https://cloud.google.com/dialogflow/cx/docs .

Cisco Unified Call Studio's DialogflowCX element is used to engage Google's Dialogflow CX service. For more information, refer
                                 to the DialogflowCX Element chapter in the Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1) guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-programming-reference-guides-list.html .

To use Virtual Agent–Voice for Dialogflow CX on 12.6(1), Assessment to Quality (A2Q) process for Contact Center AI (CCAI)
                                 must be completed.

For details on how to configure Google Dialogflow CX for OEM customers, see the Virtual Agent–Voice for Dialogflow CX chapter in the following documents:

Cisco Unified Contact Center Enterprise Features Guide, Release 12.6(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html

Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

The following table lists the minimum version of components required in Unified CCE solution for this feature.

Component

Version

CVP

VVB

Call Studio

Cloud Connect

CCE Components

ICM

Packaged CCE provides this feature only from release 12.6(1).

## Removed and Unsupported Features

The features listed in the following table are no longer available.

Deprecated Feature

Announced in Release

Replacement

Notes

Internet Explorer 11

Not applicable 1

Edge Chromium (Microsoft Edge)

None.

## Important Notes

### OpenJDK Java Runtime Environment Update

The 12.6(1) release installs OpenJDK JRE in the CVP installations if the existing installation has Oracle JRE.

For more information, refer to the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.6(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html .

For more information on JRE minor update, refer to the Java Runtime Environment Minor Update section in the Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

For information about supported versions, see the Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

### Password Hashing

This release uses salted SHA-256 hashing on user passwords in OAMP, NOAMP, and Serviceability CLI interfaces. The usage of
                              this scheme requires the user to log in once to OAMP, NOAMP, and Serviceability CLI after upgrading to 12.6(1).

| Component | Version |
|---|---|
| CVP | 12.6(1) ES-08 |
| VVB | 12.6(1) ES-03 |
| Call Studio | 12.6(1) Patch |
| Cloud Connect | 12.6(1) |
| CCE Components | 12.5(1) and higher |
| ICM | 12.5(1) and higher |

| Note | Packaged CCE provides this feature only from release 12.6(1). |
|---|---|

| Deprecated Feature | Announced in Release | Replacement | Notes |
|---|---|---|---|
| Internet Explorer 11 | Not applicable 1 | Edge Chromium (Microsoft Edge) | None. |