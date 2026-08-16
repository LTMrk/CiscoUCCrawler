---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x14-0-ce1200-exwy-b-cisco-expressway-ce1200-applian-84545c16bc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X14-0/CE1200/exwy_b_cisco-expressway-ce1200-appliance-installation-guide-x14-0/exwy_m_introduction.html
retrieved_at: 2026-08-16T22:16:30.209749+00:00
---

Cisco Expressway CE1200 Appliance Installation Guide (X14.0)

# Cisco Expressway CE1200 Appliance Installation Guide (X14.0)

Updated: April 14, 2021

Chapter: Introduction

## Chapter: Introduction

# Introduction

## Introduction

This guide describes how to install a CE1200 appliance into a video network, including
                           			how to prepare and install the hardware, and how to do the basic initial configuration.
                           			It also provides some troubleshooting suggestions.

The guide is for Cisco Expressway Series deployments only, as the appliance does not
                                       				support the Cisco VCS product.

### Required Software Version

The CE1200 ships with pre-installed Expressway software. If you need to in future, you
                              			can upgrade the pre-installed software to a later supported version. (If you want to
                              			check whether the Cisco Expressway has the latest software installed, go to http://software.cisco.com/download/navigator.html and navigate to the Cisco
                              			Expressway.)

The minimum required Expressway software version depends on which revision of the
                              			appliance you are using. You can identify this from the serial number, as follows:

Platform

Serial numbers

Required software

2nd revision CE1200 (Expressway pre-installed on UCS C220 M5L)

52E1####

X12.5.5 or later

1st revision CE1200 (Expressway pre-installed on UCS C220 M5L)

52E0####

X8.11.1 or later

Although the system does not prevent downgrades to an earlier software version, Cisco
                                          				does not support appliances running earlier versions than those specified in the
                                          				table. This requirement applies to any UCS C220 M5L-based appliance.

### Required Firmware Version

If you upgrade the pre-installed UCS firmware, you must only upgrade to a Cisco UCS
                                 				Host Upgrade Utility package at Release 4.1(1c) or later . This is due to a known
                              			issue with the dual NIC/X710 firmware in some earlier 4.0x Host Upgrade Utility
                              			packages, that causes the 1Gb SFP transceiver modules to stop working.

### System Sizes Supported

The appliance can support either a Large or a Medium Expressway system.

For appliances which are deployed as Cisco Expressway-Es (but not for Cisco
                              			Expressway-Cs) you can optionally change the default system size setting in the
                              			Expressway software from a Large system to a Medium system, or the other way round.

### What's Different?

If you deploy existing CE500, CE1000, or CE1100 appliances, this section highlights some
                              			of the differences in the CE1200:

The CE1200 is designed for use with the Cisco Expressway Series product range,
                                    					and does not support the Cisco VCS product. It ships with the release key
                                    					pre-installed.

Unlike earlier appliances, the CE1200 is a single, multi-purpose server that can
                                    					operate as a Cisco Expressway-C or a Cisco Expressway-E. By default it always
                                    					ships with Expressway-C preinstalled. To deploy the server as an Expressway-E,
                                    					you configure the Type option as Expressway-E , in
                                    					the Service Setup Wizard (the wizard runs when you first launch the Expressway
                                    					web user interface, or you can run it anytime from the Status > Overview page). The Traversal Server option key is no longer used to
                                    					change to an Cisco Expressway-E.

The appliance now ships with most option keys installed by default. The only
                                    					functions which still need option keys to be installed manually are:

Desktop System licenses

Room System licenses

RMS licenses

Advanced Security

Microsoft interoperability

The CE1200 can support up to 5000 registrations for Mobile and Remote Access, an
                                    					increase on the 2500 MRA registrations supported by other physical appliances or
                                    					VM-based systems.

From May 2019, the CE1200 no longer ships with power cables and KVM cables
                                    					supplied as default.

To add a CE1200 appliance to an existing cluster that has CE1100 models in it, configure
                              			the Type option to match the other peers (Expressway-E or Expressway-C) through the
                              			service setup wizard on the Status > Overview page, before you add the CE1200 to the cluster.

### More Information and Training

#### Training

Training is available online and at our training locations. Information about the
                                 				courses we provide and the location of our training offices is at www.cisco.com/go/telepresencetraining

#### Glossary

A glossary of TelePresence terms is at https://tp-tools-web01.cisco.com/start/glossary/

#### Related documents

Detailed information about installing this appliance is provided in the Cisco UCS C220 Server Installation and
                                          							Service Guide

Managing and operating Cisco Expressway software is described in the Cisco
                                          							Expressway Administrator  Guide on the Expressway Maintain and Operate
                                          							Guides page

Creating and maintaining a cluster of Cisco Expressways is described in the Cisco Expressway Cluster Creation and Maintenance Deployment
                                          							Guide on the Expressway Configuration Guides page

| Note | The guide is for Cisco Expressway Series deployments only, as the appliance does not
                                       				support the Cisco VCS product. |
|---|---|

| Platform | Serial numbers | Required software |
|---|---|---|
| 2nd revision CE1200 (Expressway pre-installed on UCS C220 M5L) | 52E1#### | X12.5.5 or later |
| 1st revision CE1200 (Expressway pre-installed on UCS C220 M5L) | 52E0#### | X8.11.1 or later |

| Caution | Although the system does not prevent downgrades to an earlier software version, Cisco
                                          				does not support appliances running earlier versions than those specified in the
                                          				table. This requirement applies to any UCS C220 M5L-based appliance. |
|---|---|