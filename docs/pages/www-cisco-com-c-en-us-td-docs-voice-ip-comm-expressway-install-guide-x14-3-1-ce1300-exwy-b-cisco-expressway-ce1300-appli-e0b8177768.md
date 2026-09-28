---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x14-3-1-ce1300-exwy-b-cisco-expressway-ce1300-appli-e0b8177768
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X14-3-1/CE1300/exwy_b_cisco-expressway-ce1300-appliance-installation-guide-x1431/exwy_m_introduction.html
retrieved_at: 2026-08-16T22:09:50.051750+00:00
---

Cisco Expressway CE1300 Appliance Installation Guide (X14.3.1)

# Cisco Expressway CE1300 Appliance Installation Guide (X14.3.1)

Updated: October 15, 2024

Chapter: Introduction

## Chapter: Introduction

# Introduction

This guide describes how to install a CE1300 appliance into a video network, including how to prepare and install the hardware,
                        and how to do the basic initial configuration. It also provides some troubleshooting suggestions.

The guide is for Cisco Expressway Series deployments only, as the appliance does not support the Cisco VCS product.

This chapter explains the following:

## Change History

Date

Change

Reason

October 2024

Republished X14.3.1.

Addressed a few updates to the guide.

X14.3.1 release

September 2023

First Release

Updated content for Cisco Expressway CE1300 Appliance Installation Guide for X14.3.1 release

Published with Expressway X14.3.1 version

## Required Software Version

The CE1300 ships with pre-installed Expressway software. If you need to in future, you can upgrade the pre-installed software
                              to a later supported version. (If you want to check whether the Cisco Expressway has the latest software installed, go to Software Download and navigate to the Cisco Expressway.)

The minimum required Expressway software version depends on which revision of the appliance you are using. You can identify
                              this from the serial number, as follows:

Platform

Serial Numbers

Required Software

CE1300 (Expressway pre-installed on UCS C220 M6S)

52E5####

X14.3.1 or later

Caution

Although the system does not prevent downgrades to an earlier software version, Cisco does not support appliances running
                                          earlier versions than those specified in the table. This requirement applies to any UCS C220 M6S-based appliance.

## System Sizes Supported

The appliance can support either a Large or a Medium Expressway system.

For appliances which are deployed as Cisco Expressway-Es (but not for Cisco Expressway-Cs) you can optionally change the default
                              system size setting in the Expressway software from a Large system to a Medium system, or the other way round.

## What's Different?

If you deploy existing CE500, CE1000, or CE1100 appliances, this section highlights some of the differences in the CE1300
                              (and the previous CE1200 version):

The CE1300 is designed for use with the Cisco Expressway Series product range and does not support the Cisco VCS product.
                                    It ships with the release key pre-installed.

Unlike the Expressway appliances prior to the CE1200, or Virtualized appliances, the CE1300 is a single, multi-purpose server
                                    that can operate as a Cisco Expressway-C or a Cisco Expressway-E. By default, it always ships with Expressway-C preinstalled.
                                    To deploy the server as an Expressway-E, you configure the Type option as Expressway-E in the Service Setup Wizard (the wizard runs when you first launch the Expressway web user interface, or you can run it anytime
                                    from the Status > Overview page). The Traversal Server Option key is no longer used to change to a Cisco Expressway-E.

The appliance now ships with most option keys installed by default. The only functions which still need option keys to be
                                    installed manually are:

Desktop System licenses

Room System licenses

RMS licenses

Advanced Security

Microsoft interoperability

The CE1300 can support up to 8500 Mobile and Remote Access registrations but ships with a limited-capacity factory-loaded
                                    export-unrestricted Expressway image (maximum 2500 secured/crypto sessions). If you are eligible for a full-capacity export
                                    restricted image, you must order Expressway Select. For more information, see Cisco Expressway and Cisco Expressway Select Release Note for X14.3.x (Includes X14.3 and X14.3.1 releases .

The CE1300 is not shipped with power cables by default. However, they can be selected during the order configuration. KVM
                                    cables are also not included, but Cisco part N20-BKVM= can be ordered separately if needed.

To add a CE1300 appliance to an existing cluster that has CE1300 models in it, configure the Type option to match the other
                              peers (Expressway-E or Expressway-C) through the service setup wizard on the Status > Overview page, before you add the CE1300 to the cluster.

CE1300 physical hardware uses Self-Encrypting-Disks (SED's) and ships with encryption disabled. To enable encryption, see Appendix A: Enable Encryption on Self Encrypting Disks .

## More Information and Training

### Training

Training is available online and at our training locations. Information about the courses we provide and the location of our
                              training offices is at the following link .

### Glossary

A glossary of  TelePresence terms is at link .

### Related Documentation

Detailed information about installing this appliance is provided in the Cisco UCS C220 M6S Server Installation and Service Guide .

Managing and operating Cisco Expressway software is described in the Cisco Expressway Administrator Guide on the Expressway Maintain and Operate Guides page.

Creating and maintaining a cluster of Cisco Expressways is described in the Cisco Expressway Cluster Creation and Maintenance Deployment Guide on the Expressway Configuration Guides page.

| Note | The guide is for Cisco Expressway Series deployments only, as the appliance does not support the Cisco VCS product. |
|---|---|

| Date | Change | Reason |
|---|---|---|
| October 2024 | Republished X14.3.1. Addressed a few updates to the guide. | X14.3.1 release |
| September 2023 | First Release Updated content for Cisco Expressway CE1300 Appliance Installation Guide for X14.3.1 release | Published with Expressway X14.3.1 version |

| Platform | Serial Numbers | Required Software |
|---|---|---|
| CE1300 (Expressway pre-installed on UCS C220 M6S) | 52E5#### | X14.3.1 or later |

| Caution | Although the system does not prevent downgrades to an earlier software version, Cisco does not support appliances running
                                          earlier versions than those specified in the table. This requirement applies to any UCS C220 M6S-based appliance. |
|---|---|

| Note | CE1300 physical hardware uses Self-Encrypting-Disks (SED's) and ships with encryption disabled. To enable encryption, see Appendix A: Enable Encryption on Self Encrypting Disks . |
|---|---|