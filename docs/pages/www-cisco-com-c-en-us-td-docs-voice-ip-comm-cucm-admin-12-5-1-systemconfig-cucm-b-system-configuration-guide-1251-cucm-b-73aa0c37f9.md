---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-73aa0c37f9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_010001.html
retrieved_at: 2026-08-16T17:30:33.412791+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Dial Plan Overview

## Chapter: Dial Plan Overview

# Dial Plan Overview

## About the Dial Plan

The dial plan is responsible for instructing the Cisco Unified Communications Manager system about how to route calls. When you configure a dial plan, you define such rules as:

the type of calls that are allowed

the preferred path that the system uses to place a call, as well as alternate paths

how extensions are dialed

how called and calling numbers are presented

## Dial Plan Prerequisites

Before you configure the dial plan, complete these tasks:

Initial Configuration Task Flow

Inbound and Outbound Calling Configuration

## Dial Plan
                        	 Configuration

Complete the following task flows to configure the dial plan for your system.

Step 1

Partition Configuration Task Flow

Configure partitions to create a logical grouping of directory numbers (DNs) and route patterns with similar reachability
                                          characteristics. Partitions facilitate call routing by dividing the route plan into logical subsets that are based on organization,
                                          location, and call type.

Step 2

National Numbering Plan Installation Task Flow

Optional. Cisco Unified Communications Manager provides a default North American Numbering Plan (NANP). For countries with
                                          different dial plan requirements, you can install a Cisco International Dial Plan and use it to create a unique numbering
                                          plan that is specific to your requirements. When you use a national numbering plan, you can configure route patterns that
                                          use the @ symbol, along with route filters, to create patterns for local, national, long distance, and emergency calling.

Using a national numbering dial plan is optional. If you do not use a national numbering plan, you can configure one manually.

Step 3

Call Routing Configuration Task Flow

Step 4

Hunt Pilot Configuration Task Flow

Configure a hunt pilot when you want to extend a call to one or more lists of numbers, where each list specifies a hunting
                                          order. When a call extends to a hunt party from these lists and the party fails to answer or is busy, hunting resumes with
                                          the next hunt party.

Step 5

Translation Pattern Configuration Task Flow

Configure translation patterns to manipulate inbound numbers from your voice gateway to the Cisco Unified Communications Manager.
                                          You can use translation patterns to change the calling and called number before the system forwards the call to the receiving
                                          endpoint. This translation is transparent and allows you to map extensions from the public to the private network.

Step 6

Transformation Pattern Configuration Task Flow

Configure transformation patterns for phones when you want to modify the calling number display on an inbound call. Configure
                                          transformation patterns for gateways or trunks when you want to modify the outgoing calling or called number display sent
                                          out for outbound calls. You can also use transformation patterns to modify the outbound redirecting number (known as a diversion
                                          header in SIP devices).

Step 7

Dial Rules Configuration Task Flow

You can configure different types of dial rules: application dial rules, directory lookup dial rules, and SIP dial rules.

Configure application dial rules to add and sort the priority of dialing rules for applications such as Cisco Web Dialer and
                                                Cisco Unified Communications Manager Assistant.

Configure directory lookup dial rules to transform caller identification numbers into numbers that can be looked up in the
                                                directory.

Configure the SIP Dial Rules to create dial patterns for phones that are running SIP. This procedure is typically for legacy
                                                SIP phones.

Step 8

ILS Configuration Task Flow

Configure Intercluster Lookup Service (ILS) to create networks of remote Cisco Unified Communications Manager clusters. You can configure ILS on a pair of clusters and then join those clusters to form an ILS network.

Step 9

Global Dial Plan Replication Task Flow

If you have configured an Intercluster Lookup Service (ILS) network, you can configure global dial plan replication to create
                                          a global dial plan that spans across the ILS network and includes intercluster dialing of directory URIs and alternate numbers.

Step 10

URI Dialing Configuration Task Flow

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Partition Configuration Task Flow | Configure partitions to create a logical grouping of directory numbers (DNs) and route patterns with similar reachability
                                          characteristics. Partitions facilitate call routing by dividing the route plan into logical subsets that are based on organization,
                                          location, and call type. |
| Step 2 | National Numbering Plan Installation Task Flow | Optional. Cisco Unified Communications Manager provides a default North American Numbering Plan (NANP). For countries with
                                          different dial plan requirements, you can install a Cisco International Dial Plan and use it to create a unique numbering
                                          plan that is specific to your requirements. When you use a national numbering plan, you can configure route patterns that
                                          use the @ symbol, along with route filters, to create patterns for local, national, long distance, and emergency calling. Using a national numbering dial plan is optional. If you do not use a national numbering plan, you can configure one manually. |
| Step 3 | Call Routing Configuration Task Flow | Configure a route plan to route internal calls and external calls to a private network or the public switched telephone network
                                       (PSTN). |
| Step 4 | Hunt Pilot Configuration Task Flow | Configure a hunt pilot when you want to extend a call to one or more lists of numbers, where each list specifies a hunting
                                          order. When a call extends to a hunt party from these lists and the party fails to answer or is busy, hunting resumes with
                                          the next hunt party. |
| Step 5 | Translation Pattern Configuration Task Flow | Configure translation patterns to manipulate inbound numbers from your voice gateway to the Cisco Unified Communications Manager.
                                          You can use translation patterns to change the calling and called number before the system forwards the call to the receiving
                                          endpoint. This translation is transparent and allows you to map extensions from the public to the private network. |
| Step 6 | Transformation Pattern Configuration Task Flow | Configure transformation patterns for phones when you want to modify the calling number display on an inbound call. Configure
                                          transformation patterns for gateways or trunks when you want to modify the outgoing calling or called number display sent
                                          out for outbound calls. You can also use transformation patterns to modify the outbound redirecting number (known as a diversion
                                          header in SIP devices). |
| Step 7 | Dial Rules Configuration Task Flow | You can configure different types of dial rules: application dial rules, directory lookup dial rules, and SIP dial rules. Configure application dial rules to add and sort the priority of dialing rules for applications such as Cisco Web Dialer and
                                                Cisco Unified Communications Manager Assistant. Configure directory lookup dial rules to transform caller identification numbers into numbers that can be looked up in the
                                                directory. Configure the SIP Dial Rules to create dial patterns for phones that are running SIP. This procedure is typically for legacy
                                                SIP phones. |
| Step 8 | ILS Configuration Task Flow | Configure Intercluster Lookup Service (ILS) to create networks of remote Cisco Unified Communications Manager clusters. You can configure ILS on a pair of clusters and then join those clusters to form an ILS network. |
| Step 9 | Global Dial Plan Replication Task Flow | If you have configured an Intercluster Lookup Service (ILS) network, you can configure global dial plan replication to create
                                          a global dial plan that spans across the ILS network and includes intercluster dialing of directory URIs and alternate numbers. |
| Step 10 | URI Dialing Configuration Task Flow | Configure URI dialing when you want to route calls to an endpoint using the directory URI as the call address. The directory
                                       URI follows the username@host format, where the host portion is an IPv4 address or a fully qualified domain name. |