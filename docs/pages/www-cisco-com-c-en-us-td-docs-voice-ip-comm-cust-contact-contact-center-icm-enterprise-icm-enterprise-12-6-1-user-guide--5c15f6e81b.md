---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-user-guide--5c15f6e81b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/User/guide/reporting-concepts-for-cisco-unified-icm-contact-center-enterprise-release-12-6-1/importance-of-configuration-and-scripting.html
retrieved_at: 2026-08-16T20:41:27.970413+00:00
---

Reporting Concepts for Cisco Unified ICM-Contact Center Enterprise, Release 12.6(1)

# Reporting Concepts for Cisco Unified ICM-Contact Center Enterprise, Release 12.6(1)

Updated: June 27, 2023

Chapter: Importance of Configuration and Scripting

## Chapter: Importance of Configuration and Scripting

# Importance of Configuration and Scripting

## Configuration

Open the Configuration Manager from the Unified CCE Tools folder on your desktop to enter and update information about the entities that are part of your enterprise.

Configured entities are stored as records
                              in the Central Controller database tables. These entities include agents, call types,
                              devices, PGs, services and service members, skill groups, and translation
                              routes.

For error-free routing and accurate reporting, it is
                              crucial to configure all peripheral targets—that is, any and all destinations
                              to which a call can be sent. Reports show no data for devices that are not
                              configured and monitored.

Changes and additions that you make in
                              Configuration Manager are immediately applied to the Central Database on the
                              Logger and are copied to all local databases.

### Naming Conventions in Configuration

Before configuring the system, consider how
                                 you want to name the reporting entities that you will be configuring—such as
                                 peripherals, skill groups, and agents.

The configured names for
                                 these entities appear in the Unified IC user interface as
                                 selection criteria for filtering reports. They are selected from Value Lists
                                 and Collections.

Use
                                 meaningful naming conventions to help reporting users interpret and locate the
                                 appropriate report selection items. For example, append the same prefix for all
                                 items associated with a particular site and use descriptive text to identify
                                 call types.

## Scripting

After your configuration is defined, create routing scripts using the Script Editor. Unified CCE software uses these routing scripts to determine the best destination for a call by assessing the current call center activity
                              that is extracted and forwarded by the PGs . The call flow defined in the script determines the data that is gathered for
                              reporting.

Routing scripts
                              		  contain instructions that:

Examine the call
                                    				information provided by the routing client and use that information to classify
                                    				the call as a particular call type.

Determine the
                                    				best destination for the call.

Direct the call
                                    				to an appropriate routing target; for example, to an individual agent, to a
                                    				skill group, or to an appropriate announcement.

Post-route
                                    				transfers and conferences.

Routing scripts are a representation of your business rules. You can create a specific set of scripts to be run for each call type, such as Sales or Support. For more granular reports,
                              you might want to create multiple scripts; for example, you might create a script for initial call classification and create
                              scripts that route calls that are sent to particular services or skill groups on different ACDs.

You can also
                              		  schedule different scripts to be used at different times of the day or
                              		  different days of the week and year for each call type, and you can use dialed
                              		  numbers to direct calls to scripts that handle transfers.

Routing script data
                              		  are stored in the Central Controller database. Scripting changes that you make
                              		  are applied to the local database, immediately update the Central Database on
                              		  the Logger, and are copied to all local databases. You cannot alter scripts
                              		  directly. Instead, you create and maintain routing scripts with the Script
                              		  Editor, one of the tools on the Administration & Data Server.

See the Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html for more information.

### ACD Script Considerations

Refer to your ACD Supplement Guide for any modifications you need to make in your ACD scripts. For example, you might need to modify your ACD scripts to include SEND INFO commands that notify Unified CCE when a call state transition occurs.

Also, ensure that the script the ACD follows to route the call to the appropriate agent takes into account the Services and
                                 the Service Members (skill groups) that are configured in Unified CCE .

### Unexpected Scripting Conditions

Decide whether you
                                 want calls that encounter unexpected scripting conditions to be counted as
                                 default-routed or as errors.

If you want the calls to
                                 count as default-routed:

Plan to configure default
                                       labels for each dialed number. When a call is routed to a default label, the
                                       call is added to the count of default-routed calls for the call type. If the
                                       call cannot be routed and a default label is not assigned, the call is counted
                                       as an error.

Also, plan to include a Termination Node
                                       with Termination type of default label for all scripts in which there is some
                                       unexpected input (else condition).

In all scripts,
                                 account for failure by creating a path for calls that encounter unexpected
                                 conditions. You might want to route these calls to voicemail, an announcement,
                                 or a busy signal.