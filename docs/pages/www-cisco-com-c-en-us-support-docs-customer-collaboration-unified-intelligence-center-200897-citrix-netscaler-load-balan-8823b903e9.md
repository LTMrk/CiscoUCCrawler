---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-intelligence-center-200897-citrix-netscaler-load-balan-8823b903e9
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-intelligence-center/200897-Citrix-NetScaler-Load-Balancer-Configura.html
retrieved_at: 2026-08-16T19:24:43.903521+00:00
---

Citrix NetScaler Load Balancer Configuration for Cisco Unified Intelligence Center (CUIC)

# Citrix NetScaler Load Balancer Configuration for Cisco Unified Intelligence Center (CUIC)

Updated: December 17, 2016

Document ID: 200897

Contents

## Contents

## Introduction

This document describes the configuration steps to use Citrix NetScalaer load bablander for CUIC.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CUIC

- Citrix Netscaler

### Components Used

The information in this document is based on these software and hardware versions:

- CUIC 11.0(1)

- Citrix NS: appliance Edition: Citrix NetScaler 1000v (10.1 Build 125.8)

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

CUIC is a flexible and intuitive web-based reporting platform that provides you with reports on relevant business data. With CUIC, you can create a comprehensive information portal where contact center reports and dashboards are developed and shared throughout your organization. In large CUIC deployments, the Citrix NetScaler 1000v (Load Balancer) is used to load balance CUIC Hypertext Transfer Protocol (HTTP) and Hypertext Transfer Protocol Secure (HTTPS) traffic.

## Network Diagram

## Access Unified Intelligence Center Report with HTTP/HTTPS

When HTTP is disabled in CUIC server, this is the HTTP flow to different ports.

## Configuration

### System Settings

Configuration > Settings > Configure Basic Features

### Upload License

Without License SSL might not work. Navigate to System > Licenses > Manage Licenses > Update License

### Network Configuration

Clients talk to Load balancer through Virtual IP (VIP) and Load balancer talks to CUIC through its Subnet IP (SNIP).

Click System > Network > IPs > IPv4s

### Create Subnet IP

Step 1. Click on Add to add IP Address , select Type as Subnet IP . Step 2. Click Create to create desired IP address.

### Create VIP

Step 1. Click Add to add IP Address , select Type as Virtual IP . Step 2. Click Create to create desired IP address.

### Create Routes

If needed, create routes to the network from where HTTP/HTTPS requests come to Load Balancer.

Click Create to create desired route.

### HTTPS Load Balancing Configuration

To create Virtual Server entries, one for each port in CUIC, three ports need to be monitored (HTTP ports 80. 8081 and HTTPS port 8444). Each virtual server entry is the IP and port combination which receives the HTTP traffic from client (accessing CUIC report).

Virtual servers are required to be linked with servers, to send the load traffic them. To check the health status of the server’s monitors, they need to be assigned to each server. Using the monitors, load detects the server (CUIC) failure and re-distributes the incoming traffic to servers which are in good health to serve the requests.

So the association is Virtual Server->Service and Server->Monitor.

Summary of Configurations:

- Create monitors

- Create Servers

- Create Services with Server association

- Link each service to corresponding monitors

- Create Virtual servers

- Link corresponding Services with Virtual Servers

- Create Persistency Group and add Virtual Servers

ThIs image depicts three Virtual server entries and its association.

### Create Monitors

Navigate to Traffic Management > Load Balancing > Monitors

To Create monitor, navigate to Traffic Management > Load Balancing > Monitors , click on Add button. Three types of monitors are created, for port 80, 8081and 8444.

### Create monitor for http port 80

Select Type as TCP and specify Interval , Response Time-out , Down Time , Retries etc. accordingly. Click Create to create the monitor. For HTTPS, two monitors needs to be created (one per server).

For HTTPS type monitor, configure special parameter section. This monitor reports success if the response to the HTTP request is either 200 or 302.

When HTTP is disabled in CUIC, 302 is expected otherwise 200. To deal with both the situations 200 and 302 are included.

For HTTPS type monitor, configure special parameter section. This monitor reports success only if the response contains a string In Service .

### Create Servers

Server represents a CUIC node. For each CUIC node served by the load balancer a server entry is required.

To create server, navigate to Traffic Management > Load Balancing > Servers , Click on Add button.

### Create Services

To create monitor, navigate to Traffic Management > Load Balancing > Services , Click on Add .

When there are no monitors associated, a default monitor might be displayed in configured box. Without removing that, select the correct monitor from available monitors from the available list (in this image it is cust_tcp ) and click Add to move it to Configured list. Click OK . Next time when this page is opened, it shows only the selected monitor. Default monitor disappears. This happens because; always a service needs to be associated with a monitored. If nothing is configured, load balancer provides a default one, but when user selects a monitored then load balancer takes out the default monitor.

### Create Virtual Server

To create a virtual server, navigate to Traffic Management > Load Balancing > Virtual Servers , and click Add . Check the services that needs to be associated with this virtual service.

In the Method and Persistence tab, select Method as Least Connection , Persistence as SOURCEIP and Time-out as 40 minutes. This is because the default historical reporting refresh rate is set to 30 minutes; you need to configure some value greater than the refresh rate. If you are configuring different refresh rate for historical report, then change this value as well.

### Create Persistency Groups

To create Persistency group, navigate to Traffic Management > Load Balancing > Persistency Groups , click Add .

Select Method as Least Connection , Persistence as SOURCEIP and Time-out as 40 minutes. This is because the default historical reporting refresh rate is set to 30 minutes; you need to configure some value greater than the refresh rate. If you are configuring different refresh rate for historical report, then change this value as well.

Since each CUIC server listens on three ports, you need to include all three virtual servers here. If a client requests to HTTP 80 port which is already sent to a particular CUIC server, all requests from that client targeting to port 8081, 8444 is routed to the same CUIC.

### Reference

1. http://support.citrix.com/proddocs/topic/netscaler/ns-gen-netscaler-wrapper-con.html

### Revision History

1.0

06-Apr-2017

Initial Release

### Contributed by Cisco Engineers

Kevin Lamenzo

### This Document Applies to These Products

- Unified Intelligence Center

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 06-Apr-2017 | Initial Release |