---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-ce1400v-exwy-b-cisco-expressway-ce1400v-appliance-i-afd75d734a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/CE1400V/exwy_b_cisco-expressway-ce1400v-appliance-installation-guide/exwy_m_introduction.html
retrieved_at: 2026-08-16T22:09:11.996415+00:00
---

Cisco Expressway CE1400V Appliance Installation Guide (M7 Appliances, zero factory preload)

# Cisco Expressway CE1400V Appliance Installation Guide (M7 Appliances, zero factory preload)

Updated: September 1, 2025

Chapter: Introduction

## Chapter: Introduction

# Introduction

This guide describes how to install a CE1400V appliance into the Cisco on-premises collaboration products, including how to
                        prepare and install the hardware, and how to do the basic initial configuration. It also provides some troubleshooting suggestions.

The guide is for Cisco Expressway Series deployments only, as the appliance does not support hosting any other applications.

This chapter explains the following:

## Change History

Date

Change

Reason

September 2025

First Release

Updated content for Cisco Expressway CE1400V Appliance

Published with Expressway X15.3 release

## Required Software Version

The CE1400V appliance requires virtualization software and a license (which must be customer-provided) and is a virtualized
                              hardware replacement for the CE1300 appliance. For software downloads, go to Software Download and navigate to the Cisco Expressway.

The minimum required Expressway software version depends on which revision of the appliance you are using. You can identify
                              this from the serial number, as follows:

Platform

Required Software

CE1400V

The following is required:

Hypervisor, also known as a virtual machine monitor (VMM) or virtualizer

VMware vSphere ESXi

Minimum version 7.0

For detailed information, see Virtualization for Cisco Expressway Series .

For information, see the Cisco Expressway and Cisco Expressway Select Release Note .

Caution

Although the system does not prevent downgrades to an earlier software version. You can contact the Technical Assistance Center
                                          or BEMS to downgrade to earlier versions of the Cisco Expressway.

## System Sizes Supported

The CE1400V can support either a Large or a Medium Expressway system.

For appliances which are deployed as Cisco Expressway-Es (but not for Cisco Expressway-Cs) you can optionally change the default
                              system size setting in the Expressway software from a Large system to a Medium system, or the other way round.

You can optionally change the default system size settings in the Expressway software for up to either,

3 Large virtual machines

6 Medium virtual machines

## What's Different?

Key differences between the Cisco Expressway CE1400V and the previous appliances CE1300 and CE1200

The CE1400V is virtualized/non-virtualized, requiring a hypervisor and license, while CE1300 and CE1200 are bare-metal appliances.

CE1400V offers more flexible deployment with multiple VMs, whereas CE1300 and CE1200 are single workload servers.

CE1400V requires customer-provided virtualization infrastructure, marking a shift from physical to virtual appliance deployment.

This reflects the evolution from physical appliances (CE1200, CE1300) to a virtualized appliance (CE1400V) with enhanced scalability
                              and deployment flexibility.

## More Information and Training

### Training

Training is available online and at our training locations. Information about the courses we provide and the location of our
                              training offices is at the following link .

### Glossary

A glossary of terms is at link .

### Related Documentation

Detailed information about installing this appliance is provided in the Cisco UCS C220 M7 Server Installation and Service Guide .

Managing and operating Cisco Expressway software is described in the Cisco Expressway Administrator Guide on the Expressway Maintain and Operate Guides page.

Creating and maintaining a cluster of Cisco Expressways is described in the Cisco Expressway Cluster Creation and Maintenance Deployment Guide on the Expressway Configuration Guides page.

| Note | The guide is for Cisco Expressway Series deployments only, as the appliance does not support hosting any other applications. |
|---|---|

| Date | Change | Reason |
|---|---|---|
| September 2025 | First Release Updated content for Cisco Expressway CE1400V Appliance | Published with Expressway X15.3 release |

| Platform | Required Software |
|---|---|
| CE1400V | The following is required: Hypervisor, also known as a virtual machine monitor (VMM) or virtualizer VMware vSphere ESXi Minimum version 7.0 For detailed information, see Virtualization for Cisco Expressway Series . For information, see the Cisco Expressway and Cisco Expressway Select Release Note . |

| Caution | Although the system does not prevent downgrades to an earlier software version. You can contact the Technical Assistance Center
                                          or BEMS to downgrade to earlier versions of the Cisco Expressway. |
|---|---|

| Note | You can optionally change the default system size settings in the Expressway software for up to either, 3 Large virtual machines 6 Medium virtual machines |
|---|---|