---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-rel-notes-14-0-1-cucm-b-release-notes-for-cucm-imp-14-0-1-cucm-m-import-46129e5301
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/rel_notes/14_0_1/cucm_b_release-notes-for-cucm-imp-14_0_1/cucm_m_important-notes.html
retrieved_at: 2026-08-16T23:51:13.640252+00:00
---

Release Notes for Cisco Unified Communications Manager and the IM and Presence Service, Release 14

# Release Notes for Cisco Unified Communications Manager and the IM and Presence Service, Release 14

## Results

Updated: October 22, 2024

Chapter: Important Notes

## Chapter: Important Notes

# Important Notes

## Simplifying Release Number Scheme

From Release 14 onwards, Cisco Unified Communications Manager has adopted the single number release plan. There will be no
                              (dot) releases like (dot five) in the past release versions. Service Update releases will be published on top of the main
                              major release 14 through the regular Software Maintenance cycle.

## Important Note for Features Supported in Release 12.5(1)SU4

Unified Communications Manager supported the following features in Release 12.5(1)SU4:

Serviceability Enhancement for Cisco Jabber/Webex App over Mobile and Remote Access Registrations

SSO Redirect URI for Webex App

BAT Support for Cisco VG420 Analog Voice Gateway

These features are not supported in Release 14, but will be available in 14 SU1 Release. Hence, users on the 12.5(1)SU4 Unified
                              Communications Manager version loses the above mentioned features when they upgrade Unified Communications Manager to Release
                              14.

## Centralized Certificate Monitoring and Management

Webex Cloud-Connected UC (CCUC) is a suite of Cisco Webex cloud services with a single global view to manage on-premises UC
                           and Unified CM cloud services.

CCUC provides a centralized cloud-based tool for analytics, upgrades, and troubleshooting and allows you to leverage the benefits
                           of the Cisco Webex cloud, while keeping critical calling workload on your premises.

You can subscribe to the UC management Services on Control Hub. CCUC helps manage multiple clusters, for both Unified CM and
                           Unified CM Cloud deployments.

As of Release 14, Certificate Monitoring and Management is a cloud-based service which provides a way to collect all certificate
                           information from on-premise UC Infrastructure and manage certificates from Control Hub user interface.

## New Cisco Gateway Support

New releases of Unified Communications Manager have introduced support for the following Cisco gateways:

Cisco VG400 Analog Voice Gateway

Cisco VG410 Analog Voice Gateway (Using only the Gateway Configuration window from Cisco Unified Communications Manager Administration Graphical User Interface)

Cisco VG420 Analog Voice Gateway

Cisco VG450 Analog Voice Gateway

Cisco 4461 Integrated Services Router

The following table lists supported gateway models and the initial release, by release category, where support was introduced.
                              Within each release category (for example, 11.5(x) and 12.5(x)), support for the gateway model is added as of the specified
                              release, along with later releases in that category. For these releases, you can select the gateway in the Gateway Configuration window of Unified Communications Manager.

Gateway Model

11.5(x) Releases

12.5(x) Releases

14(x) Releases

Cisco VG 202, 202 XM, 204, 204 XM, 310, 320, 350 Analog Voice Gateway

11.5(1) and later

12.5(1) and later

14 and later

Cisco VG400 Analog Voice Gateway

11.5(1)SU7 and later

12.5(1) and later

14 and later

Cisco VG410 Analog Voice Gateway

Not supported

Not supported

14SU3 and later

Cisco VG420 Analog Voice Gateway

Not supported

12.5(1)SU4 and later

14SU1 and later

Cisco VG450 Analog Voice Gateway

11.5(1)SU6 and later

12.5(1) and later

14 and later

Cisco 4321, 4331 4351, 4431, 4451 Integrated Services Router

11.5(1) and later

12.5(1) and later

14 and later

Cisco 4461 Integrated Services Router

11.5(1)SU6 and later

12.5(1) and later

14 and later

Cisco Catalyst 8300 Series Edge Platforms

—

12.5(1)SU4 and later

14 and later

### Cisco Analog Telephone Adapters

Cisco Analog Telephone Adapters connect analog devices, such as an analog phone or fax machine, to your network. These devices
                              can be configured via the Phone Configuration window. The following table highlights model support for the ATA series.

ATA Adapter

11.5(x) Releases

12.5(x) Releases

14(x) Releases

Cisco ATA 190 Analog Telephone Adapter

11.5(1) and later

12.5(1) and later

14 and later

Cisco ATA 191 Analog Telephone Adapter

11.5(1)SU4 and later

12.5(1) and later

14 and later

| Gateway Model | 11.5(x) Releases | 12.5(x) Releases | 14(x) Releases |
|---|---|---|---|
| Cisco VG 202, 202 XM, 204, 204 XM, 310, 320, 350 Analog Voice Gateway | 11.5(1) and later | 12.5(1) and later | 14 and later |
| Cisco VG400 Analog Voice Gateway | 11.5(1)SU7 and later | 12.5(1) and later | 14 and later |
| Cisco VG410 Analog Voice Gateway | Not supported | Not supported | 14SU3 and later |
| Cisco VG420 Analog Voice Gateway | Not supported | 12.5(1)SU4 and later | 14SU1 and later |
| Cisco VG450 Analog Voice Gateway | 11.5(1)SU6 and later | 12.5(1) and later | 14 and later |
| Cisco 4321, 4331 4351, 4431, 4451 Integrated Services Router | 11.5(1) and later | 12.5(1) and later | 14 and later |
| Cisco 4461 Integrated Services Router | 11.5(1)SU6 and later | 12.5(1) and later | 14 and later |
| Cisco Catalyst 8300 Series Edge Platforms | — | 12.5(1)SU4 and later | 14 and later |

| ATA Adapter | 11.5(x) Releases | 12.5(x) Releases | 14(x) Releases |
|---|---|---|---|
| Cisco ATA 190 Analog Telephone Adapter | 11.5(1) and later | 12.5(1) and later | 14 and later |
| Cisco ATA 191 Analog Telephone Adapter | 11.5(1)SU4 and later | 12.5(1) and later | 14 and later |