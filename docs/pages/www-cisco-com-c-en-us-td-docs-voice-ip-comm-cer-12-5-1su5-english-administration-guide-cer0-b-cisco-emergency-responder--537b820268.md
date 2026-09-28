---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-12-5-1su5-english-administration-guide-cer0-b-cisco-emergency-responder--537b820268
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/12_5_1su5/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-1251su5/cer0_b_cisco-emergency-responder-administration-guide-1251su3_preface_00.html
retrieved_at: 2026-08-21T15:34:20.995871+00:00
---

Cisco Emergency Responder Administration Guide for Release 12.5(1)SU5

# Cisco Emergency Responder Administration Guide for Release 12.5(1)SU5

Updated: August 23, 2023

Chapter: Preface

## Chapter: Preface

# Preface

## Overview

This document provides you with the required information to install, configure, manage, and use Cisco Emergency Responder
                           (Emergency Responder).

## Audience

Network engineers, system administrators, and telecom engineers
                           		should review this guide to learn the steps required to properly set up
                           		Emergency Responder  in the network. Because of the close interaction of
                           		Emergency Responder with CiscoUnifiedCommunicationsManager, you should
                           		be familiar with CiscoUnifiedCommunicationsManager before deploying
                           		Emergency Responder.

Security personnel should also read this document.

## Organization

The following table details how this guide is organized:

Topic

Description

Plan for Cisco Emergency Responder

Provides information to help you understand emergency call ordinances, how Emergency Responder helps you meet the ordinances,
                                          and what you must do to deploy Emergency Responder successfully.

Cisco Emergency Responder Installation

Provides detailed information about installing or upgrading to Emergency Responder.

Configure Cisco Unified Communications Manager

Describes the configuration procedures for Unified CM for Emergency Responder.

Configure Cisco Emergency Responder

Describes the configuration procedure for Emergency Responder.

Configure Emergency Responder and Intrado V9-1-1 Enterprise Services

Describes how to configure Emergency Responder to interoperate with Intrado V-9-1-1 Enterprise.

Configure Cisco Emergency Responder Serviceability

Describes how to configure and use Emergency Responder Serviceability features.

Configure Cisco Unified Operating System

Describes how to configure and use the Cisco Unified Communications Operating System, which is bundled with Emergency Responder.

Configure Cisco Emergency Responder Disaster Recovery System

Describes how to configure the Cisco Emergency Responder Disaster Recovery System.

Cisco Emergency Responder Admin Utility

Describes how to use the Cisco Emergency Responder Admin Utility.

Cisco Emergency Responder User Preparation

Describes the various roles for Emergency Responder users.

Troubleshoot Cisco Emergency Responder

Addresses problems you might encounter with Emergency Responder and provides ways to resolve them; also includes other tasks
                                          associated with problem identification and resolution.

ALI Formatting Tool

Describes the ALI Formatting Tool (AFT) and provides information about how to use and troubleshoot the AFT.

Cisco Emergency Responder Administration Web Interface

Describes the fields on the pages of the Emergency Responder administrator web interface.

Cisco Emergency Responder Serviceability Web Interface

Describes the Emergency Responder serviceability web interface.

Cisco Unified Operating System Administration Web Interface

Describes the Cisco Unified Operating System (OS) Administration web interface.

Disaster Recovery System Web Interface

Describes the Cisco Emergency Responder Disaster Recovery System Administration web interface.

Admin Utility Web Interface for Cisco Emergency Responder

Describes the Cisco Emergency Responder Admin Utility web interface.

Using AFT for Specific Service Providers

Provides service-provider specific information for use in conjunction with the AFT.

Event Log Messages

Provides Emergency Responder based Event Log messages and administrative alerts.

Cisco Emergency Responder Port Usage

Provides information about the ports used by Emergency Responder.

## Related
                        	 Documentation

For additional information about Cisco Emergency Responder (Emergency Responder) and Cisco Unified Communications Manager
                           (Unified Communications Manager), see the following publications:

All Cisco Emergency Responder documents are available at:

https://www.cisco.com/c/en/us/support/unified-communications/emergency-responder/series.html

Cisco Unified Communications Manager installation documents are available at:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html

Cisco Unified Communications Manager operating system installation documents and backup and restore documents are available
                                 at:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html

## Cisco Product
                        	 Security Overview

This product
                           		contains cryptographic features and is subject to United States and local
                           		country laws governing import, export, transfer and use. Delivery of Cisco
                           		cryptographic products does not imply third-party authority to import, export,
                           		distribute or use encryption. Importers, exporters, distributors and users are
                           		responsible for compliance with U.S. and local country laws. By using this
                           		product you agree to comply with applicable laws and regulations. If you are
                           		unable to comply with U.S. and local laws, return this product immediately.

## Acknowledgments

This product includes software developed by Justin Wells and
                           		Semiotek Inc. for use in the WebMacro Servlet Framework
                           		(http://www.webmacro.org).

You may use WebMacro for use under the BSD License. You may also use WebMacro under the terms of the Semiotek Public License.
                           The terms of the Semiotek Public License are as follows:

Copyright © 2010 WebMacro, Semiotek Inc.

All rights reserved.

Redistribution and use in source and binary forms, with or
                           		without modification, are permitted provided that the following conditions are
                           		met:

Redistributions of source code must retain the above copyright
                                 			 notice, this list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright
                                 			 notice, this list of conditions and the following disclaimer in the
                                 			 documentation and/or other materials provided with the distribution.

All advertising materials mentioning features or use of this
                                 			 software must display the following acknowledgment: "This product includes software developed by Justin Wells and
                                    				Semiotek Inc. for use in the WebMacro Servlet Framework
                                    				(http://www.webmacro.org)."

The names "Semiotek Inc." and "WebMacro" must not be used to endorse or promote products
                                 			 derived from this software without prior written permission. For written
                                 			 permission, please contact justin@webmacro.org

Products derived from this software may not be called "WebMacro" nor may "WebMacro" appear in their names without prior written
                                 			 permission of Justin Wells.

Redistributions of any form whatsoever must retain the following
                                 			 acknowledgment: "This product includes software developed by Justin Wells and
                                    				Semiotek Inc. for use in the WebMacro Servlet Framework
                                    				(http://www.webmacro.org)."

THIS SOFTWARE IS PROVIDED BY SEMIOTEK INC. "AS IS" AND ANY EXPRESSED OR IMPLIED WARRANTIES OR CONDITIONS,
                           		INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OR CONDITIONS OF
                           		MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
                           		EVENT SHALL SEMIOTEK INC. OR ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
                           		INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
                           		BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
                           		DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
                           		LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
                           		OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
                           		ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

| Topic | Description |
|---|---|
| Plan for Cisco Emergency Responder | Provides information to help you understand emergency call ordinances, how Emergency Responder helps you meet the ordinances,
                                          and what you must do to deploy Emergency Responder successfully. |
| Cisco Emergency Responder Installation | Provides detailed information about installing or upgrading to Emergency Responder. |
| Configure Cisco Unified Communications Manager | Describes the configuration procedures for Unified CM for Emergency Responder. |
| Configure Cisco Emergency Responder | Describes the configuration procedure for Emergency Responder. |
| Configure Emergency Responder and Intrado V9-1-1 Enterprise Services | Describes how to configure Emergency Responder to interoperate with Intrado V-9-1-1 Enterprise. |
| Configure Cisco Emergency Responder Serviceability | Describes how to configure and use Emergency Responder Serviceability features. |
| Configure Cisco Unified Operating System | Describes how to configure and use the Cisco Unified Communications Operating System, which is bundled with Emergency Responder. |
| Configure Cisco Emergency Responder Disaster Recovery System | Describes how to configure the Cisco Emergency Responder Disaster Recovery System. |
| Cisco Emergency Responder Admin Utility | Describes how to use the Cisco Emergency Responder Admin Utility. |
| Cisco Emergency Responder User Preparation | Describes the various roles for Emergency Responder users. |
| Troubleshoot Cisco Emergency Responder | Addresses problems you might encounter with Emergency Responder and provides ways to resolve them; also includes other tasks
                                          associated with problem identification and resolution. |
| ALI Formatting Tool | Describes the ALI Formatting Tool (AFT) and provides information about how to use and troubleshoot the AFT. |
| Cisco Emergency Responder Administration Web Interface | Describes the fields on the pages of the Emergency Responder administrator web interface. |
| Cisco Emergency Responder Serviceability Web Interface | Describes the Emergency Responder serviceability web interface. |
| Cisco Unified Operating System Administration Web Interface | Describes the Cisco Unified Operating System (OS) Administration web interface. |
| Disaster Recovery System Web Interface | Describes the Cisco Emergency Responder Disaster Recovery System Administration web interface. |
| Admin Utility Web Interface for Cisco Emergency Responder | Describes the Cisco Emergency Responder Admin Utility web interface. |
| Using AFT for Specific Service Providers | Provides service-provider specific information for use in conjunction with the AFT. |
| Event Log Messages | Provides Emergency Responder based Event Log messages and administrative alerts. |
| Cisco Emergency Responder Port Usage | Provides information about the ports used by Emergency Responder. |