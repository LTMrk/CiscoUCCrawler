---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-survivable-remote-site-telephony-119026-configure-cusm-9cd8b0b870
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-survivable-remote-site-telephony/119026-configure-cusm-00.html
retrieved_at: 2026-08-21T13:54:18.682188+00:00
---

Configure the CUSM for Integration with the CUCM

# Configure the CUSM for Integration with the CUCM

### Download Options

Updated: May 29, 2015

Document ID: 119026

Contents

## Contents

## Introduction

This document describes how to configure the Cisco Unified Survivable Remote Site Telephony (SRST) Manager (CUSM) for integration with the Cisco Unified Communications Manager (CUCM).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Call Manager Express (CME)

- CUCM

- CUSM

- SRST

### Components Used

The information in this document is based on these software and hardware versions:

- CUSM installed from an Open Virtualization Application (OVA) template

- CUCM Version 8.6 or later

- CME Version 8.6 or later

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

The CUSM operates as a part of the Cisco Enhanced Survivable Remote Site Telephony (E-SRST) solution.

The SRST and E-SRST solutions provide telephone functionality in remote branch sites during temporary WAN outages that prevent communication between the central site and the branch site.

## Configure

This section describes how to configure the CUSM and the associated components for integration with the CUCM.

Note : Use the Command Lookup Tool ( registered customers only) in order to obtain more information on the commands used in this section.

### Configure the CUCM

Complete these steps in order to configure the CUCM for integration with the CUSM:

- Log into the CUCM.

- Create an application user, and assign the Standard AXL API Access role:

- Enter the show network eth0 command in order to verify whether the CUCM is defined via a Fully Qualified Domain Name (FQDN) (such as CCMpub.cisco.com ). The CUCM server must be defined via an FQDN.

- Ensure that the Domain Name System (DNS) server to which the CUCM points has both forward and reverse lookup configured for the CUCM hostname or IP address. If not, the integration with the CUSM will fail.

- Configure the device pools on the CUCM so that the CUSM can retrieve the SRST references that are associated to the device pools and provision the sites appropriately.

### Configure the CUSM

Complete these steps in order to configure the CUSM:

- Define your voicemail Pilot setting preference, and then click Next .

- Select whether you want to integrate the SRST Manager and the branch site routers via Transport Layer Security (TLS), and then click Finish .

- Navigate to System > Domain Name System Settings .

Note : Ensure that the DNS server has forward and reverse entries for the CUCM hostname or IP address.

- Add the hostname and domain of the SRST Manager.

- Click Apply .

Note : This step is optional at this point, as it can be changed post-integration.

- Click trusted TLS ( Transport Layer Security) certificates.

Note : If you copy/paste the certificate, use the tomcat.pem certificate. If you choose to manually upload the certificate, use the tomcat.der certificate.

- Ensure that the certificate has the correct Common Name (CN); it should include the hostname and domain name: If the CN does not reflect the hostname and domain name, you will most likely encounter this error:

### Integrate the CUCM with the CUSM

Complete these steps in order to integrate the CUCM with the CUSM:

- From the CUSM, click Configure and select Central Call Agents .

- Enter the hostname/IP address of the CUCM server.

- Enter the username and password of the application user that you created on the CUCM.

Note : There is an option to add the Publisher and Subscriber server at this point as well.

- Configure the schedule in accordance with the CUSM that will poll the CUCM via AXL for any configuration changes or updates.

- Enable the CUCM.

Note : Though you can add a Publisher and Subscriber server, the CUSM does not exchange keep-alives with the two servers. It only attempts to contact the servers when you forcefully try to retrieve the SRST references or when the time schedule that is configured on the CUSM requires it to contact the CUCM.

### Configure the SRST Gateways/CME

The CUSM has the ability to provision the sites as:

- E-SRST

- SRST-only (call-manager-fallback)

- Customized templates that you configure

Complete these steps in order to configure the SRST gateways/CME:

- Enable the gateway for HTTP in order to act as a server (IP HTTP server).

- Configure Telnet or Secure Shell (SSH).

Note : You must configure SSH if you use TLS between the gateway and the CUSM.

The CUSM completes the rest of the configuration for you based on your provision choice for the site (SRST-only, E-SRST, or based on a customized template).

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

29-May-2015

Initial Release

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

- Unified Survivable Remote Site Telephony

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 29-May-2015 | Initial Release |