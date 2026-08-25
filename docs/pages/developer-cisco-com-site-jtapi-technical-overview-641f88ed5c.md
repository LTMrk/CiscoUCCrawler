---
doc_id: developer-cisco-com-site-jtapi-technical-overview-641f88ed5c
source_url: https://developer.cisco.com/site/jtapi/technical-overview/
retrieved_at: 2026-08-25T21:06:15.969815+00:00
---

## Introduction

Cisco Unified Communication Manager (Unified CM) exposes sophisticated call control of IP telephony devices and soft-clients via the Computer Telephony JTAPI interface. Cisco's JTAPI enables custom applications to monitor telephony-enabled devices and call events, as well as establish first- and third-party call control.

- Provides 1st Party Call Control - Perfect fit for desktop softphones and server-based IVR applications.

- Provides 3rd Party Call Control - Perfect fit for server or desktop applications that perform screen pops for incoming calls and click-to-connect from Windows applications.

- Provides all the hooks necessary to integrate with standard or custom RTP libraries (for example: Java Media Framework), but does not provide a specific audio implementation.

## Usage

- Presence-based routing - combine user availability, location, and preferences to render a uniquely tailored UC experience. E.G. Single Number Reach - Find me, follow me, hide me.

- Financial Specialist Soft-phone - Combine market data, business logic, and call control in a browser-based application to enable brokers and analysts to respond to rapid changes in today's global financial markets.

- Healthcare Consoles - Combine call control, doctor/patient lookup, and emergency response team paging into a browser-based console to improve response times and patient care.

- Hospitality - Link caller data with POS systems to automate room or restaurant reservations, dispatch taxis, schedule wake-up calls, and more.

- Self-Service - Collect caller information to provide automated services across a variety of devices.

- Intelligent Contact Routing - Application monitors the status of devices and issues routing instructions to send calls to the right place at the right time, including Call Intercept & Virtual Hold.

- Call Recording & Analytics - Application monitors the status of devices and issues Start/Stop recording instructions while retrieving call statistics for analys.

## Tech Details

- Cisco JTAPI conforms to Sun's JTAPI 1.2 specification. Our Java Telephony implementation uses client-side libraries to facilitate the connection(s) required by distributed application servers to connect to the Unified CM CTI Manager service running on one (or more) Unified CM Subscriber servers. Cisco CTI is secure, redundant , and scalable.

- Cisco JTAPI is a set of Java packages, supplying a robust object-oriented CTI development environment for multiple platforms.

## JTAPI Architecture

Below is a diagram that illustrates the architecture of JTAPI