---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su6-admingd-cucm-b-administration-guide-1251su6-cucm-b-test-858e255ab9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU6/adminGd/cucm_b_administration-guide-1251su6/cucm_b_test-adminguide_chapter_011001.html
retrieved_at: 2026-08-21T08:39:13.254654+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6 and 12.5(1)SU7

# Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6 and 12.5(1)SU7

Updated: April 8, 2025

Chapter: Troubleshooting Overview

## Chapter: Troubleshooting Overview

# Troubleshooting Overview

This section provides the necessary background information and available resources to troubleshoot the Unified Communications Manager .

## Cisco Unified Serviceability

Cisco Unified Serviceability , a web-based troubleshooting tool for Unified Communications Manager , provides the following functionality to assist administrators troubleshoot system problems:

Saves Unified Communications Manager services alarms and events for troubleshooting and provides alarm message definitions.

Saves Unified Communications Manager services trace information to various log files for troubleshooting. Administrators can configure, collect, and view trace
                                 information.

Monitors real-time behavior of the components in a Unified Communications Manager cluster through the real-time monitoring tool (RTMT).

Generates reports for Quality of Service, traffic, and billing information through Unified Communications Manager CDR Analysis and Reporting (CAR).

Provides feature services that you can activate, deactivate, and view through the Service Activation window.

Provides an interface for starting and stopping feature and network services.

Archives reports that are associated with Cisco Unified Serviceability tools.

Allows Unified Communications Manager to work as a managed device for SNMP remote management and troubleshooting.

Monitors the disk usage of the log partition on a server (or all servers in the cluster).

Access Cisco Unified Serviceability from the Cisco Unified Communications Manager Administration window by choosing Cisco Unified Serviceability from the Navigation drop-down list box. Installing the Unified Communications Manager software automatically installs Cisco Unified Serviceability and makes it available.

See Cisco Unified Serviceability Administration Guide for detailed information and configuration procedures on the serviceability tools.

## Cisco Unified
                        	 Communications Operating System Administration

Cisco Unified Communications Operating System Administration allows you to perform the following tasks to configure and manage the Cisco Unified Communications Operating System :

Check software and
                                 			 hardware status.

Check and update
                                 			 IP addresses.

Ping other network
                                 			 devices.

Manage Network
                                 			 Time Protocol servers.

Upgrade system
                                 			 software and options.

Restart the
                                 			 system.

Refer to the Administration Guide for Cisco Unified Communications Manager for detailed information and configuration procedures on the serviceability tools.

## General Model of Problem Solving

When troubleshooting a telephony or IP network environment, define the specific symptoms, identify all potential problems
                           that could be causing the symptoms, and then systematically eliminate each potential problem (from most likely to least likely)
                           until the symptoms disappear.

The following steps provide guidelines to use in the problem-solving process.

Analyze the network problem and create a clear problem statement. Define symptoms and potential causes.

Gather the facts that you need to help isolate possible causes.

Consider possible causes based on the facts that you gathered.

Create an action plan based on those causes. Begin with the most likely problem and devise a plan in which you manipulate
                                    only one variable.

Implement the action plan; perform each step carefully while testing to see whether the symptom disappears.

Analyze the results to determine whether the problem has been resolved. If the problem was resolved, consider the process
                                    complete.

If the problem has not been resolved, create an action plan based on the next most probable cause on your list. Return to 4 and repeat the process until the problem is solved.

Make sure that you undo anything that you changed while implementing your action plan. Remember that you want to change only
                              one variable at a time.

If you exhaust all the common causes and actions (either those outlined in this document or others that you have identified
                                          in your environment), contact Cisco TAC.

## Network Failure Preparation

You can always recover more easily from a network failure if you are prepared ahead of time. To determine if you are prepared
                           for a network failure, answer the following questions:

Do you have an accurate physical and logical map of your internetwork that outlines the physical location of all of the devices
                                 on the network and how they are connected as well as a logical map of network addresses, network numbers, and subnetworks?

Do you have a list of all network protocols that are implemented in your network for each of the protocols implemented and
                                 a list of the network numbers, subnetworks, zones, and areas that are associated with them?

Do you know which protocols are being routed and the correct, up-to-date configuration information for each protocol?

Do you know which protocols are being bridged? Are any filters configured in any of these bridges, and do you have a copy
                                 of these configurations? Is this applicable to Unified Communications Manager ?

Do you know all the points of contact to external networks, including any connections to the Internet? For each external network
                                 connection, do you know what routing protocol is being used?

Has your organization documented normal network behavior and performance, so you can compare current problems with a baseline?

If you can answer yes to these questions, faster recovery from a failure results.

## Where to Find More Information

Use the following links for information on various IP telephony topics:

For further information about related Cisco IP telephony applications and products, see the Cisco Unified Communications Manager Documentation Guide . The following URL shows an example of the path to the documentation guide:

https://www.cisco.com/en/US/products/sw/voicesw/ps556/products_documentation_roadmaps_list.html

For documentation related to Cisco Unity, see the following URL: https://www.cisco.com/en/US/products/sw/voicesw/ps2237/tsd_products_support_series_home.html

For documentation related to Cisco Emergency Responder , see the following URL: https://www.cisco.com/en/US/products/sw/voicesw/ps842/tsd_products_support_series_home.html

For documentation related to Cisco Unified IP Phone , see the following URL: https://www.cisco.com/en/US/products/hw/phones/ps379/tsd_products_support_series_home.html

For information on designing and troubleshooting IP telephony networks, see the Cisco IP Telephony Solution Reference Network
                                 Design Guides that are available at: https://www.cisco.com/go/srnd

| Note | If you exhaust all the common causes and actions (either those outlined in this document or others that you have identified
                                          in your environment), contact Cisco TAC. |
|---|---|