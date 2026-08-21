---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-reporting-guide-ccv-84e07c2f98
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/reporting/guide/ccvp_b_150_reporting-guide-for-cisco-unified-customer-voice-portal/cvp_m_150_reporting-server.html
retrieved_at: 2026-08-21T03:01:53.530573+00:00
---

Reporting Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

# Reporting Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

Updated: March 1, 2025

Chapter: Reporting Server

## Chapter: Reporting Server

# Reporting Server

## Reporting Service

Reporting is an optional component for Cisco  Unified Customer Voice Portal (CVP) installation.

Select Reporting during the installation process
                              to install the Reporting Server,
                              which is comprised of the reporting service and the
                              reporting database.

The             reporting
                              service receives reporting data from the Interactive Voice Response (IVR) service, the Session Initiation Protocol (SIP)
                              service (if used), and the VoiceXML (VXML) server and transforms and writes this data to
                              the Informix reporting database to provide historical reporting in a call center
                              environment.

Reporting data includes summary information about call
                              activity, which assists call center managers in reviewing
                              and managing daily operations. It can also include operational detail data for
                              various IVR applications.

## Reporting
                        	 Architecture

The following
                              		  diagram shows the Unified CVP architecture. For clarity, the diagram separates
                              		  the reporting service and the database.

The call server
                              		  uses a central messaging bus to allow each service to communicate.

The reporting
                              		  service connects to the message bus through either an in-process plug-in or an
                              		  out-of-process plug-in, depending on whether the reporting service resides in
                              		  the same Java Virtual Machine (JVM) with the message bus system.

The service
                              		  listens to all messages passing through the message bus and captures both
                              		  call-state change messages sent from Call Server or reporting messages sent
                              		  from the Reporting Server.

The reporting service then parses those messages, converts them into batches of applicable Structured Query language (SQL)
                              statements, and runs them into an SQL database using the Java Database Connectivity (JDBC) Application provisioning interface
                              (API).

The reporting
                              		  service can also receive and process Unified CVP messages related to Unified
                              		  CVP system administrative tasks, such as turning on or off debugging and
                              		  querying statistics. As the Figure 1 shows, the reporting service can be shared
                              		  by multiple Call Servers that belong to the same Unified CVP deployment.

If your
                              		  environment uses more than one reporting server, be aware that:

Each Call
                                    				Server and each VXML Server can be associated with only one reporting server.

Reports
                                    				cannot span multiple Informix databases.

Although Unified CVP does not have a built-in reporting engine, its installation includes reporting templates designed for
                              use with the Unified Intelligence Center (Unified IC) reporting application. You can import these templates into Unified IC
                              and run them from the Unified IC interface.

## Cisco Unified
                        	 Customer Voice Portal Reporting Server Deployment Options and Sizing

## Cisco Unified Customer Voice Portal Reporting Server Installation and Upgrade

Explanations and procedures
                              regarding the installation and upgrade of the Unified CVP reporting server are
                              documented in the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal .

Topics in the Installation and Upgrade guide
                              include:

Installing the reporting
                                    component

Specifying the reporting password

Excluding the reporting server from anti-virus software port
                                    blocking

Upgrading the reporting server

Adding reporting capability to the VXML Server

Backing up and purging of the reporting
                                    database

## Cisco Unified
                        	 Customer Voice Portal Reporting Server Setup

You can find
                              		  explanations and procedures regarding the configuration and maintenance of the
                              		  Unified CVP Reporting server in the Administration Guide for
                                       				  Cisco Unified Customer Voice Portal and in the Configuration Guide for
                                       				  Cisco Unified Customer Voice Portal .

Topics in the
                              		  operations console help and in the Configuration guide include:

Reporting server
                                    				statistics

Adding a
                                    				reporting server

Editing a
                                    				reporting server

Deleting a
                                    				reporting server

Finding a
                                    				reporting server

Configuring a
                                    				VoiceXML server for reporting (adding and editing)

Applying
                                    				inclusive and exclusive VoiceXML filters for reporting

Transferring a
                                    				file to multiple devices

## Database
                        	 Maintenance

Through the
                              		  Operations Console, Unified CVP provides access to database maintenance and
                              		  enables you to perform administrative tasks such as backups and purges.

See Configuration Guide for
                                       				  Cisco Unified Customer Voice Portal for details on database operations.

| Note | The connection
                                       		  of the Operations Console to the call server through an OAMP Resource Manager
                                       		  (ORM) is simply indicative, because the ORM is invisible to the end user. An
                                       		  ORM is co-located with each managed Unified CVP component, and the Operations
                                       		  Console is connected to each component. |
|---|---|

| Note | A deployment needs only one reporting server. During temporary database outages, messages are buffered to file and are inserted
                                       into the database after the database comes back on line. The amount of time that messages can be buffered depends on the system
                                       throughput. See Failure and Restoration . |
|---|---|