---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be6000-installationguide-15-cucm-b-installation-guide-6k-7k-m7-15-cucm--662c5d586e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE6000/InstallationGuide/15/cucm_b_installation-guide-6k_7k_m7_15/cucm_m_introduction-to-the-cisco-business.html
retrieved_at: 2026-08-21T22:40:17.694365+00:00
---

Installation Guide for Cisco Business Edition 6000 and 7000, Release 15 (M7 Appliances, zero factory preload 14X15X-K9-17 / 14X15X-XU-17)

# Installation Guide for Cisco Business Edition 6000 and 7000, Release 15 (M7 Appliances, zero factory preload 14X15X-K9-17 / 14X15X-XU-17)

Updated: June 23, 2025

Chapter: Introduction to the Cisco Business Edition 6000 and 7000 appliances

## Chapter: Introduction to the Cisco Business Edition 6000 and 7000 appliances

# Introduction to the Cisco Business Edition 6000 and 7000 appliances

## Who Should Use This Guide?

This guide is for deployments using the BE6000M (M6) BE7000M (M6) or BE7000H (M6) appliance models, factory-preloaded with
                              the  14X15X-K9-16 / 14X15X-XU-16 applications suite for Collaboration System Releases  14 and 15.

This guide helps you set up your Business Edition appliance if you can answer yes to the following questions.

Are you doing a manual installation of applications on a Cisco Business Edition appliance? This guide covers everything that
                                    you have to do to customize it for your business needs.

Are you installing application versions from Collaboration System Release 14 and 15? If yes, this installation guide applies.
                                    If no, then your applications may not support ESXi 7.0 and you cannot leverage the factory-loaded software.

Applications from Collaboration System Releases  12.5 and older are not factory-installed on M6 appliances.

Does your deployment fit within the Supported Solution Capacities described in Appendix A?

Cisco partners can find more information on the http://www.cisco.com/go/bepartner .

Caution

Do not reinstall or downgrade the factory-loaded virtualization software. Do not reformat the disks or rebuild the storage
                                          hardware array. Either action wipes out the factory preloaded software and causes post installation  problems.

## New and Changed Information

The following table provides an overview of the significant changes to the features in this guide up to this current release.
                              The table does not provide an exhaustive list of all changes made to the guide or of the new features up to this release.

Feature or Change

Description

See

Date

Initial Release of Document for Preloads Version 14X15X-K9/XU-16 on M6 Appliances

Preload application files for CSR 14 and 15 versions (drop all files for version12.x)

Revised preload file list (drop all skip-install-OVAs [now in UC media kits], drop all locales)

Preloaded ESXi version to 7.0 U3i (ships unlicensed, license required but is sold separately or customer-provided)

BE6000M, BE7000M, BE7000H (M6) appliance hardware

—

April 15, 2024

## Essential Documents for Installation of the Business Edition 6000 or 7000 Appliance

You can proceed with the installation by using the instructions in this document, refer the following documents that are listed
                              for Deployment Options, Equipment, and Applications. All of these documents are available at the http://www.cisco.com/c/en/us/support/unified-communications/business-edition-6000/tsd-products-support-series-home.html

Choose the product version, and then refer to the following documents:

Deployment Options—To gain insights to help you plan your deployment, see the Preferred Architecture guides and the Cisco Validated Designs that are relevant to your business needs.

Applications—To find out more about applications, see the following documents:

Business Edition 6000/7000 Software Load Summary / Release Notes —This document contains information on ISO and OVA files that are pre-loaded in the appliance's datastore.

Other documents for UC applications are listed on the Component Documentation tab.

| Note | Cisco partners can find more information on the http://www.cisco.com/go/bepartner . |
|---|---|

| Caution | Do not reinstall or downgrade the factory-loaded virtualization software. Do not reformat the disks or rebuild the storage
                                          hardware array. Either action wipes out the factory preloaded software and causes post installation  problems. |
|---|---|

| Feature or Change | Description | See | Date |
|---|---|---|---|
| Initial Release of Document for Preloads Version 14X15X-K9/XU-16 on M6 Appliances | Preload application files for CSR 14 and 15 versions (drop all files for version12.x) Revised preload file list (drop all skip-install-OVAs [now in UC media kits], drop all locales) Preloaded ESXi version to 7.0 U3i (ships unlicensed, license required but is sold separately or customer-provided) BE6000M, BE7000M, BE7000H (M6) appliance hardware | — | April 15, 2024 |