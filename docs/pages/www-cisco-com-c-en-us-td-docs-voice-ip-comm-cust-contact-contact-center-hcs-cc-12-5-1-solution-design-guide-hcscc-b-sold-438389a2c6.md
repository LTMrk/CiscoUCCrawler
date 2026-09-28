---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-hcs-cc-12-5-1-solution-design-guide-hcscc-b-sold-438389a2c6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/hcs-cc/12_5_1/Solution_Design_Guide/hcscc_b_soldg-for-hcs-cc-12_5/hcscc_b_soldg-for-hcs-cc-12_5_chapter_01.html
retrieved_at: 2026-08-21T23:54:09.507390+00:00
---

Solution Design Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5

# Solution Design Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5

Updated: February 16, 2020

Chapter: Cisco Unified Contact Center Solutions

## Chapter: Cisco Unified Contact Center Solutions

# Cisco Unified Contact Center Solutions

## Contact Center Enterprise
                        		Solutions

The first four chapters of this book are for anyone who wants to get familiar with the contact center enterprise solutions:

Packaged Contact Center Enterprise

Cisco Hosted Collaboration Solution for Contact Center

Unified Contact Center Enterprise

For information about design considerations and guidelines specific to HCS for CC , see the remaining chapters.

Cisco contact center enterprise
                           			solutions support several deployment models to meet various business needs. Choose the
                           			deployment model that fits your needs.

Cisco offers these contact center enterprise
                           			solutions:

Cisco Packaged Contact Center Enterprise Solution—A predesigned solution for up to 12000 multichannel agents

Cisco Hosted Collaboration Solution for Contact Center—For Service Providers who offer cloud contact center solutions for up to 36000 multichannel agents

Cisco Unified Contact Center Enterprise Solution—For enterprise customers who need scale and flexibility for up to 36000 multichannel agents

All of the contact center enterprise
                           			solutions use a redundant architecture for high availability and solution
                           			serviceability. They provide a comprehensive feature set, including:

Call processing and call control

Web chat, email, and callback

Social media monitoring

Rich VRU and routing scripting

Interactive voice and video response
                                 					unit

Voice and video recording and streaming

Agent selection and queuing

Web-based agent and supervisor desktops

Comprehensive reporting

### Packaged Contact
                           	 Center Enterprise

Cisco Packaged Contact Center Enterprise (Packaged CCE) is a predefined deployment.

If your requirements fit the boundaries of the solution, Packaged CCE simplifies some major features of your deployment. Enjoy
                                 the advantages of a simplified management interface and reduced time to install. The solution supports up to 12,000 concurrent active agents.

### Hosted
                           	 Collaboration Solution for Contact Center

Cisco Hosted
                                    						Collaboration Solution for Contact Center ( Cisco HCS for Contact
                                    						Center ) is designed for service providers who offer hosted contact center services to their end customers. Cisco HCS for Contact
                                    						Center deployments can support small to large end customers. As a service provider, you operate the solution for your end customers.
                              This contact center enterprise solution enables your end customers to tap into the applications and services of the Cisco
                              Hosted Collaboration Solution. Cisco HCS for Contact
                                    						Center enables you to deliver the capabilities of a contact center enterprise solution as a cloud service to the market with shared
                              aggregation and administration layers  across tenants, such as CUBE, ASA, Unified CCDM, UCDM, and Prime Collaboration Assurance..

### Unified Contact
                           	 Center Enterprise

Cisco Unified Contact Center Enterprise
                              			(Unified CCE) offers industry-leading routing capabilities and CTI capabilities. Unified
                              			CCE provides the options to support a single-site or a multisite environment.

Unified CCE supports multiple Unified CM clusters. You can also network multiple Unified CCE instances together for greater
                              system capacity.

## Contact Center
                        	 Enterprise Solution Comparison

This table
                           		highlights the differences between the contact center enterprise solutions:

Feature

Packaged
                                       					 CCE

Cisco HCS for Contact
                                             						Center (for a single instance)

Unified
                                       					 CCE (for a single instance)

Deployments and Scalability

Preconfigured Reference Designs (2000, 4000, and 12000 agents)

Avaya PG and ICM-to-ICM Gateway as a Non-Reference Design (4000 and 12000 agents)

Preconfigured Reference Designs (2000, 4000, 12000, and 24000 agents) 1

Reference Designs (2000, 4000, 12000, 24000 agents, and Contact Director [24000 agents across 3 instances])

Non-Reference Design deployments

Hardware

Tested Reference Configuration ( B-Series and C-Series)

Tested Reference Configuration ( B-Series and C-Series)

Spec-based
                                       					 UCS support (B-Series and C-Series)

Tested Reference Configuration ( B-Series and C-Series)

Spec-based UCS support (B-Series and C-Series)

Spec-based
                                       					 (Non-UCS), third-party hardware support

Architecture

Configuration and Administration tools

Gadget-based CCE Administration and other tools

Partial
                                       					 gadget-based CCE Administration, Unified Contact Center Domain Manager, ICM
                                       					 Configuration Manager, and other tools

Partial
                                       					 gadget-based CCE Administration, Unified Contact Center Management Portal, ICM
                                       					 Configuration Manager, and other tools

| Note | The first four chapters of this book are for anyone who wants to get familiar with the contact center enterprise solutions: Packaged Contact Center Enterprise Cisco Hosted Collaboration Solution for Contact Center Unified Contact Center Enterprise For information about design considerations and guidelines specific to HCS for CC , see the remaining chapters. |
|---|---|

| Feature | Packaged
                                       					 CCE | Cisco HCS for Contact
                                             						Center (for a single instance) | Unified
                                       					 CCE (for a single instance) |
|---|---|---|---|
| Deployments and Scalability | Preconfigured Reference Designs (2000, 4000, and 12000 agents) Avaya PG and ICM-to-ICM Gateway as a Non-Reference Design (4000 and 12000 agents) | Preconfigured Reference Designs (2000, 4000, 12000, and 24000 agents) 1 | Reference Designs (2000, 4000, 12000, 24000 agents, and Contact Director [24000 agents across 3 instances]) Non-Reference Design deployments |
| Hardware | Tested Reference Configuration ( B-Series and C-Series) | Tested Reference Configuration ( B-Series and C-Series) Spec-based
                                       					 UCS support (B-Series and C-Series) | Tested Reference Configuration ( B-Series and C-Series) Spec-based UCS support (B-Series and C-Series) Spec-based
                                       					 (Non-UCS), third-party hardware support |
| Architecture |
| Configuration and Administration tools | Gadget-based CCE Administration and other tools | Partial
                                       					 gadget-based CCE Administration, Unified Contact Center Domain Manager, ICM
                                       					 Configuration Manager, and other tools | Partial
                                       					 gadget-based CCE Administration, Unified Contact Center Management Portal, ICM
                                       					 Configuration Manager, and other tools |