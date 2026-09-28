---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-administrat-92d10a2bc1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/administration/guide/ucce_b_150_administration-guide-for-cisco-unified-contact-center-enterprise/ucce_m_150_voice-call-routing.html
retrieved_at: 2026-08-16T20:44:03.210534+00:00
---

Administration Guide for Cisco Unified Contact Center Enterprise Release, 15.0(1)

# Administration Guide for Cisco Unified Contact Center Enterprise Release, 15.0(1)

Updated: July 31, 2026

Chapter: Voice Call Routing

## Chapter: Voice Call Routing

# Voice Call Routing

## Routing a Target Device in Unified CCE

The following procedures outline the steps to follow each time you want
                           		to route to a new device target in Unified CCE.

### Target Device Routing on Unified CM

Step 1

Create a CTI Route Point on the Unified CM.

This step configures the Unified CM to make a route request to the
                                             				system software when the Route Point is dialed.

Step 2

Associate the CTI Route Point with the PG User.

This step makes the Route Point visible to the system software.

### Route Target Device
                           	 Using Configuration Manager

Step 1

Create a new
                                          			 Dialed Number using the Configuration Manager.

Defines a new
                                             				entry point for call routing.

Step 2

Add a new Call
                                          			 Type using the Configuration Manager.

Allows you to
                                             				categorize calls and route them appropriately.

Step 3

Associate the
                                          			 Dialed Number with the Unified ICM Call Type.

Allows you to
                                             				map the Dialed Number to a routing script.

Step 4

Create a new
                                          			 routing script using the Script Editor.

Routes the call
                                             				to the entry point.

Step 5

Associate the
                                          			 Call Type with the routing script.

Associates the
                                             				Call Type with the routing script.

In a Unified
                                                   				  Communications Manager cluster, be aware that two routing clients must not
                                                   				  share the same CTI Route Point. Each routing client must use distinct CTI Route
                                                   				  Points in a Unified Communications Manager cluster.

Only one unique Dialed Number can be assigned to a CTI Route Point across all partitions. When setting up a new CTI Route
                                                   Point, avoid using a Dialed Number that is already assigned to a different CTI Route Point in another partition. Using different
                                                   Dialed Numbers for different partitions for a CTI Route Point is not a supported configuration.

When you
                                                   				  configure a calling party transformation mask for the translation pattern in
                                                   				  Unified Communications Manager, the application will have additional
                                                   				  connections and disconnections. Therefore, for the components to function
                                                   				  properly, do not configure a translation pattern mask for the calling party.

### Peripherals and Skill Groups

Only base skill groups are supported for Unified CCE configurations. A
                              		default is set at the peripheral level, ensuring that any new skill group
                              		created is base-only.

Agents must be associated with skill groups or precision queues. You can create precision queues using the Unified CCE Web
                              Administration.

For more information about creating routing scripts, see Scripting and Media Routing Guide for Cisco Unified Contact Center Enterprise and the Script Editor online help.

For more information about configuring Unified CCE, see Cisco Unified Contact Center Enterprise Installation and Upgrade Guide

| Step 1 | Create a CTI Route Point on the Unified CM. This step configures the Unified CM to make a route request to the
                                             				system software when the Route Point is dialed. |
|---|---|
| Step 2 | Associate the CTI Route Point with the PG User. This step makes the Route Point visible to the system software. |

| Step 1 | Create a new
                                          			 Dialed Number using the Configuration Manager. Defines a new
                                             				entry point for call routing. |
|---|---|
| Step 2 | Add a new Call
                                          			 Type using the Configuration Manager. Allows you to
                                             				categorize calls and route them appropriately. |
| Step 3 | Associate the
                                          			 Dialed Number with the Unified ICM Call Type. Allows you to
                                             				map the Dialed Number to a routing script. |
| Step 4 | Create a new
                                          			 routing script using the Script Editor. Routes the call
                                             				to the entry point. |
| Step 5 | Associate the
                                          			 Call Type with the routing script. Associates the
                                             				Call Type with the routing script. |

| Note | In a Unified
                                                   				  Communications Manager cluster, be aware that two routing clients must not
                                                   				  share the same CTI Route Point. Each routing client must use distinct CTI Route
                                                   				  Points in a Unified Communications Manager cluster. Only one unique Dialed Number can be assigned to a CTI Route Point across all partitions. When setting up a new CTI Route
                                                   Point, avoid using a Dialed Number that is already assigned to a different CTI Route Point in another partition. Using different
                                                   Dialed Numbers for different partitions for a CTI Route Point is not a supported configuration. When you
                                                   				  configure a calling party transformation mask for the translation pattern in
                                                   				  Unified Communications Manager, the application will have additional
                                                   				  connections and disconnections. Therefore, for the components to function
                                                   				  properly, do not configure a translation pattern mask for the calling party. |
|---|---|