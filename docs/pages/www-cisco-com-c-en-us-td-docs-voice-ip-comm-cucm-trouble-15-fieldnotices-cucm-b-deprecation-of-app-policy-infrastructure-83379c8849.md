---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-trouble-15-fieldnotices-cucm-b-deprecation-of-app-policy-infrastructure-83379c8849
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/trouble/15/fieldNotices/cucm_b_deprecation-of-app-policy-infrastructure_cum.html
retrieved_at: 2026-08-16T17:50:45.144229+00:00
---

Deprecation of Application Policy Infrastructure Controller Enterprise Module (APIC-EM) Integration with Cisco Unified Communications Manager

# Deprecation of Application Policy Infrastructure Controller Enterprise Module (APIC-EM) Integration with Cisco Unified Communications Manager

### Download Options

Updated: December 19, 2025

# Deprecation of Application Policy Infrastructure Controller Enterprise Module (APIC-EM) Integration with Cisco Unified Communications
            Manager

## Overview

The Cisco APIC-EM (Application Policy Infrastructure Controller Enterprise Module) provides centralized access to all fabric
                  information, optimizes the application lifecycle for scale and performance, and supports flexible application provisioning
                  across physical and virtual resources. It enables a UC communication controller, such as Cisco Unified Communications Manager
                  (Unified Communications Manager), to apply QoS policies to media flows between UC endpoints.

When setting up a call, Unified Communications Manager uses APIC-EM’s northbound interface to create a flow with the appropriate
                  media type. APIC-EM then uses this information and its configured DSCP value for each media type to instruct all underlying
                  network routers to overwrite the DSCP value for packet flows from one IP port to another. This allows real-time media flows
                  to have a higher priority than other network traffic, thereby providing improved media quality for calls established through
                  Unified CM.

With this approach, there is no need for all endpoints to mark DSCP for their media packets. All QoS settings are managed
                  in one place. The request for setting comes from a trusted application, such as Unified Communications Manager, and the network
                  manager can trust that the settings will be applied to all devices.

APIC-EM is end of support on February 29, 2024.

THIS ADVISORY IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY
                  OF MERCHANTABILITY. YOUR USE OF THE INFORMATION OR MATERIALS LINKED FROM THE ADVISORY IS AT YOUR OWN RISK. CISCO RESERVES
                  THE RIGHT TO CHANGE OR UPDATE THIS ADVISORY AT ANY TIME.

## Products Affected

Products Affected

Version

Cisco Unified Communications Manager

14

Cisco Unified Communications Manager

15

## Problem Description

The following feature is deprecated and is not supported by Cisco Unified Communications Manager (Unified Communications Manager)
                  for the version mentioned above:

Application Policy Infrastructure Controller Enterprise Module (APIC-EM) Integration

## Background

Cisco announced the end-of-life for the Cisco APIC-EM Hardware Appliance.

End-of-Sale and End-of-Life Announcement for the Cisco APIC-EM Hardware Appliance

Cisco Application Policy Infrastructure Controller Enterprise Module (APIC-EM) Apps: Network Plug and Play (PnP), Easy QoS,
                           Path Trace, Cisco Active Advisor (CAA), Identity Verification Engine (IVE), IWAN Application, Wide Area Bonjour, Remote Troubleshooter
                           and Network Visibility Product Bulletin

## Problem / Symptom

Integration between the Application Policy Infrastructure Controller Enterprise Module (APIC-EM) and Unified Communication
                  Manager will not work.

## Product Migration Options

Customers are encouraged to use Unified Communication Manager-based Service Parameter–based DSCP QoS management instead of
                  APIC-EM.

## Opening a Case with TAC

If you require further assistance, or if you have any further questions regarding this field notice, contact Cisco Systems Technical Assistance Center (TAC) by one of the following methods:

Open a Service Request on cisco.com

By Email

By Telephone

| Products Affected | Version |
|---|---|
| Cisco Unified Communications Manager | 14 |
| Cisco Unified Communications Manager | 15 |