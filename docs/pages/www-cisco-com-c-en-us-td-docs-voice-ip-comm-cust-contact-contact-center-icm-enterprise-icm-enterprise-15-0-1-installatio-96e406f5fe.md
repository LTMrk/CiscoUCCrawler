---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-installatio-96e406f5fe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/installation/guide/rcct-b-cce-es-installation-guide--release-15_01_es/rcct-m-engineering-specials-installation.html
retrieved_at: 2026-08-16T19:57:39.762900+00:00
---

Cisco Unified Contact Center Enterprise Engineering Specials Installation Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Engineering Specials Installation Guide, Release 15.0(1)

Book Contents

- Book Title Page

- Introduction

- Manual ES Installation

Find Matches in This Book

## Results

Updated: August 15, 2025

Chapter: Introduction

## Chapter: Introduction

# Introduction

## Key Considerations Before Installation

The Engineering Special (ES) is a cumulative update for the Contact Center Enterprise (CCE) components. It contains all new
                           features, updated features, trials features, security fixes, and resolved defects from the base release, customized for VOS,
                           CCE, and CVP components.

The CCE ES is applicable to all CCE nodes including PGs, Administation Clients, and all Central Controller Components (Logger,
                           Router, and Administration and Data Server).

For procedures on how install (and uninstall) the ES patches on VOS, CCE, and CVP components, see the Cisco Unified Contact Center Enterprise Engineering Specials Installation Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

### Imporant Notes

To install the ES patch on VVB, use the CLI command utils system upgrade initiate .

If the command-line interface (CLI) method fails, use the Install/Upgrade option in the Cisco Unified CCE Administration Page
                                          to perform the installation or upgrade. For detailed instructions and additional information, refer to the Cisco Unified Contact
                                          Center Express Installation and Upgrade Guides available at the following link: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-guides-list.html .

## ES Installation Methods

You can install the ES in one of the following ways:

### Installation via Orchestration

The Orchestration feature provides partners and administrators an option to automatically download software updates and simplify
                              the installation and rollback processes. Orchestration currently supports installation and rollback of Cisco Engineering Specials
                              (ES), Service Updates (SU), and Microsoft Patches.

For more details, see the CCE Orchestration chapter in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

### Manual ES Installation

Install the ES's manually by following the procedures provided in the next chapter.

Before proceeding, make sure to thoroughly review the Considerations section in the Release Notes for CCE ES202508 at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html . In the same Release Notes, you will find the components that have made an ES available, along with their download links,
                                          listed under the Quarterly Patch Downloads – 15.0_ES202508 section.

| Note | If the command-line interface (CLI) method fails, use the Install/Upgrade option in the Cisco Unified CCE Administration Page
                                          to perform the installation or upgrade. For detailed instructions and additional information, refer to the Cisco Unified Contact
                                          Center Express Installation and Upgrade Guides available at the following link: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-guides-list.html . |
|---|---|

| Note | Before proceeding, make sure to thoroughly review the Considerations section in the Release Notes for CCE ES202508 at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-release-notes-list.html . In the same Release Notes, you will find the components that have made an ES available, along with their download links,
                                          listed under the Quarterly Patch Downloads – 15.0_ES202508 section. |
|---|---|