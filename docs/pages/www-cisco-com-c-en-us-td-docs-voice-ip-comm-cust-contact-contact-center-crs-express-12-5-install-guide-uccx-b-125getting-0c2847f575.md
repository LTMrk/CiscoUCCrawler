---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-install-guide-uccx-b-125getting-0c2847f575
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/install/guide/uccx_b_125getting-started-ip-ivr/uccx_b_125getting-started-ip-ivr_chapter_01000.html
retrieved_at: 2026-08-16T21:15:34.093347+00:00
---

Getting Started with IP IVR Guide, Release 12.5(1)

# Getting Started with IP IVR Guide, Release 12.5(1)

Updated: February 10, 2020

Chapter: Unified ICME for Unified CCE Installation and Configuration

## Chapter: Unified ICME for Unified CCE Installation and Configuration

# Unified ICME for Unified CCE Installation and Configuration

## About Unified ICME Software

As part of Unified CCE, Unified ICME software provides ACD
                              		  functionality including monitoring and control of agent states, routing and
                              		  queuing of contacts, CTI capabilities, real-time data for agents and
                              		  supervisors, and gathering real-time and historical data for reporting in the
                              		  Unified CCE system.

The basic Unified ICME software for a Unified CCE system
                              		  includes the following components: CallRouter, Logger, Peripheral Gateway with
                              		  a Unified CM PIM and an Unified IP IVR PIM, CTI Server, and an Admin
                              		  Workstation.

## Unified ICME Dependencies in a Unified CCE System

Before installing and configuring Unified ICME for use with
                              		  Unified IP IVR in a Unified CCE system, you must do the following.

On the Cisco Unified Communications Manager, you must have:

- Created a Unified CM
                                       				  PG user and associated the user with CTI Route Point(s) and CTI Port(s).

- Enabled CTI for the
                                       				  Unified CM PG user.

On the Unified IP IVR system, you must have:

- Configured one CTI
                                       				  Route Point for each post route number and/or one for each translation route
                                       				  DNIS.

- Configured the VRU
                                       				  Port Group.

- Configured the ICM
                                       				  subsystem.

- Predefined in the
                                       				  Unified CCX Editor any enterprise ECC variables and uploaded VRU scripts.

- Specified the VRU
                                       				  Connection Port.

- Configured translation
                                       				  routing on the Unified IP IVR system.

## Configure the Unified ICME System for the Unified IP IVR System

To enable the Unified ICME to communicate with the Unified IP
                              		  IVR system, you must:

- Add an ICM VRU PIM to an
                                 			 ICM VRU Peripheral Gateway.

- Add a Type 2 Network VRU
                                 			 in the ICM Configuration Manager and select this Network VRU in the Advanced
                                 			 tab of the VRU PIM configuration.

- Define the necessary ICM
                                 			 Labels.

- Create separate ICM call
                                 			 types for Unified IP IVR applications and queuing applications (not essential,
                                 			 but a good practice).

- Define ICM Expanded Call
                                 			 Variables.

- Configure Announcements.

- Define ICM VRU Scripts.

- Configure an ICM Service
                                 			 for Translation Routing.

- Configure an ICM Service
                                 			 for Post Routing.

For complete instructions on configuring Unified ICME for use
                              		  in a Unified CCE Environment, see the appropriate installation and
                              		  configuration guide for the software version you have at Cisco Unified Contact Center Enterprise Install and Upgrade
                                 			 Guides .

### Ensure Unified IP IVR PG is Configured Correctly

There may be cases when a call is not queued, but instead
                                 		  sent to the agent directly (via the LAA Select node) from Unified IP IVR. You
                                 		  must ensure the Unified IP IVR PG is configured correctly to ensure that such a
                                 		  call is considered answered at the Unified IP IVR service rather than
                                 		  abandoned.

In the ICM Configuration Manager, select Tools > Explorer
                                                				  Tools > PG Explorer .

Click Retrieve.

Select the IP IVR peripheral.

In Configuration Parameter, insert /ASSUME_ANSWERED .

Click Save.

## Unified ICME Documentation

Planning and step-by-step installation instructions for Unified
                           		ICME are included in the documentation located at Cisco Unified Contact Center Enterprise Install and Upgrade
                              		  Guides .

| Step 1 | In the ICM Configuration Manager, select Tools > Explorer
                                                				  Tools > PG Explorer . |
|---|---|
| Step 2 | Click Retrieve. |
| Step 3 | Select the IP IVR peripheral. |
| Step 4 | In Configuration Parameter, insert /ASSUME_ANSWERED . |
| Step 5 | Click Save. |