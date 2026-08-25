---
doc_id: developer-cisco-com-site-tapi-technical-overview-709a266c83
source_url: https://developer.cisco.com/site/tapi/technical-overview/
retrieved_at: 2026-08-25T21:10:51.203018+00:00
---

## Introduction

Cisco Unified Communication Manager (Unified CM) exposes sophisticated call control of IP telephony devices and soft-clients via the Computer Telephony TAPI interface. Cisco's Telephone Service Provider (TSP) and Wave Driver interface enables custom applications to monitor telephony-enabled devices and call events, establish first- and third-party call control, and interact with the media layer to terminate media, play announcements, record calls.

- Provides 1st Party Call Control - Perfect fit for desktop softphones and server-based IVR applications

- Provides 3rd Party Call Control - Perfect fit for server or desktop applications that perform screen pops for incoming calls and click-to-connect from Windows applications

- Provides all the hooks necessary to integrate with standard or custom RTP libraries, including methods to interact with the media layer.

## Usage

- Applications may monitor or control Cisco IP Phones, create and register CTI ports to provide media streaming capabilities (e.g. play announcements, offer self-service applications, etc), and manage CTI Route Points to queue and distribute incoming calls.

- Presence-based routing - combine user availability, location, and preferences to render a uniquely tailored UC experience. E.G. Single Number Reach - Find me, follow me, hide me

- Financial Specialist Softphone - Combine market data, business logic, and call control in a browser-based application to enable brokers and analysts to respond to rapid changes in today's global financial markets

- Healthcare Consoles - Combine call control, doctor/patient lookup, and emergency response team paging into a browser-based console

- Hospitality - Link caller data with POS systems to automate room or restaurant reservations, dispatch taxis, schedule wake-up calls, and more

- Self-Service - Collect caller information to provide automated services across a variety of devices

- Intelligent Contact Routing - Application monitors the status of devices and issues routing instructions to send calls to the right place at the right time, including Call Intercept & Virtual Hold

- Call Recording & Analytics - Application monitors the status of devices and issues Start/Stop recording instructions while retrieving call statistics for analysis

## Tech Details

- Cisco TAPI conforms to Microsoft's TAPI 2.1 specification. Our Telephone Service Provider (TSP) implementation uses client-side libraries to facilitate the connection(s) required by distributed application servers to connect to the Unified CM CTI Manager service running on one (or more) Unified CM Subscriber servers. Cisco CTI is secure, redundant , and scalable.

- Cisco TAPI applications can be written in C and C++

## TAPI/TSP Architecture