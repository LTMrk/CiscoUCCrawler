---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1su1-rtmt-cucm-b-cisco-unified-rtmt-administration-1251su1-173f961e38
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1SU1/rtmt/cucm_b_cisco-unified-rtmt-administration-1251su1/cucm_b_cisco-unified-rtmt-administration-1251su1_chapter_01.html
retrieved_at: 2026-08-21T01:39:36.091656+00:00
---

Cisco Unified Real-Time Monitoring Tool Administration Guide, Release 12.5(1)SU1

# Cisco Unified Real-Time Monitoring Tool Administration Guide, Release 12.5(1)SU1

Updated: October 12, 2021

Chapter: Administration Overview

## Chapter: Administration Overview

- Administration Overview

- Cisco Unified Real-Time Monitoring Tool

- Operating System Support

# Administration Overview

## Cisco Unified Real-Time Monitoring Tool

The Cisco Unified Real-Time Monitoring Tool, which runs as a
                              		  client-side application, monitors the real-time behavior of 
                              		  your system components. Unified RTMT uses Hypertext
                              		  Transfer Protocol Secure (HTTPS) and Transmission Control Protocol (TCP) to
                              		  monitor the following:

System performance

Device status

Device discovery

Computer Telephony Integration (CTI) applications

Unified RTMT can connect directly to devices through HTTPS to
                              		  troubleshoot system problems.

Unified RTMT allows you to perform the following tasks:

Monitor a set of predefined management objects that monitor the health of the system.

Generate various alerts, in the form of email messages, for objects when values go above or below user-configured thresholds.

Collect and view traces in various default viewers that exist in Unified RTMT.

View syslog messages in SysLog Viewer.

Work with performance-monitoring counters.

Unified Communications Manager only: Translate Q931 messages.

A single copy of Unified RTMT that is installed on your computer lets you monitor more than one server or more than one cluster
                              at a time. For example, you can monitor all of the following entities:

A Unified Communications Manager product on one server.

An IM and Presence Service product on one server.

A Unity Connection product on one server.

A server on a cluster (to monitor the health of the cluster).

## Operating System Support

You can install Unified RTMT on a computer that is running one of the following operating systems:

Windows 8

Linux with KDE or GNOME client

Consider the following information when you install Unified RTMT:

Unified RTMT requires at least 128 MB memory to run on a Windows OS platform.

Unified RTMT requires at least 300 MB of disk space to run on a Windows and Linux OS platform.

When you install Unified RTMT on a Windows 10 platform, you will see this User Account Control popup message: "An unidentified program wants to access your computer." Click Allow to continue working with Unified RTMT.

Unified RTMT runs on 32 bit and 64 bit Windows platforms.

| Note | Even when Unified RTMT is not running as an application on your desktop, tasks such as alarm and performance monitoring updates
                                       continue to take place on the server in the background. |
|---|---|

| Note | For Windows 10 and later, ensure that you launch Unified RTMT in 'Run as administrator' mode. Otherwise, User Access Control
                                       (UAC) rights are disabled. |
|---|---|