---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b04plug-html-45d046de19
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b04plug.html
retrieved_at: 2026-08-21T16:11:57.801279+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Plug-in Configuration

## Chapter: Plug-in Configuration

- Installing Plug-ins

- Updating the Plug-in URL

- Update Plug-in URL Configuration Settings

## Plug-in Configuration

Application plug-ins extend the functionality of Cisco Unified Presence Server. For example, the JTAPI plug-in allo ws a computer to host applications that access the Cisco Unified Presence Server via the Java Telephony Application Programming Interface (JTAPI).

This section contains the following topics:

• Installing Plug-ins

• Updating the Plug-in URL

• Update Plug-in URL Configuration Settings

## Installing Plug-ins

Tip After Cisco Unified Presence Server upgrades, you must reinstall all plug-ins except the Cisco CDR Analysis and Reporting plug-in. Before you install any plug-ins, disable all intrusion detection or antivirus services that run on the server where you plan to install the plug-in.

Perform the following procedure to install any plug-in.

Step 1 Choose Application > Plugins .

The Find and List Plugins window displays. Use the drop-down list boxes to search for available plug-in applications.

Step 2 From the first Find Plugins window drop-down list box, choose one of the following criteria:

• Name

• Description

From the second Find Plugins window drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

From the Plugin Type drop-down list box, choose one of the following criteria:

• Application Menu

• Installation

• User Menu

• Telecaster Menu

Step 3 Specify the appropriate search text, if applicable, and click Find .

Tip To find all available plug-ins, click Find without entering any search text.

Step 4 Click the plug-in name that you want to install.

Cisco Unified Presence Server does not support the following plugins:

• Cisco Unified CallManager AXL SQL Toolkit

• Cisco IP Phone Address Book Synchronizer

• Cisco JTAPI for Linux

• Cisco JTAPI for Solaris Sparc

• Cisco JTAPI for Solaris X86

• Cisco JTAPI for Windows

• Cisco TAPS for Windows

• Cisco Telephony Service Provider

• Cisco Unified CallManager Attendant Console

Step 5 To download the plug-in, click the Download link.

Step 6 Follow the instructions in the installation wizard to complete the installation.

Related Topics

• Plug-in Configuration

• Updating the Plug-in URL

## Updating the Plug-in URL

During the Cisco Unified Presence Server install process, records that are added to the Plugins table specify the URLs that the Administration applications use to build the Application drop-down menu. The domain name server (DNS) provides the basis for the URL that is constructed at installation time. If the DNS changes, the URL does not get updated.

Perform the following procedure to update the URL of the Plug-in URL.

Step 1 Choose Application > Plugins .

The Find and List Plugins window displays.

Step 2 From the drop-down list boxes, choose the Plugin name and the Plugin type.

Step 3 Click the Plugin name that you want to update.

The Update Plugin URL window displays.

Step 4 Enter the URL in the Custom URL field.

Step 5 To update and save the URL, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Related Topics

• Plug-in Configuration

• Installing Plug-ins

## Update Plug-in URL Configuration Settings

Table 19-1 describes the update plug-in URL configuration settings.

Table 19-1 Update Plug-in URL Configuration Settings

Plugin Name

From the drop-down list box, choose the Plugin Name for which you are changing the URL.

Plugin Type

From the drop-down list box, choose the Plugin Type for which you are changing the URL; for example, application or installation.

URL

The URL automatically displays.

Custom URL

Use only alphanumeric characters for the custom URL.

Show Plugin on User Option Pages

Check this check box to show the plug-in on the user option window.

| Field | Description |
|---|---|
| Plugin Name | From the drop-down list box, choose the Plugin Name for which you are changing the URL. |
| Plugin Type | From the drop-down list box, choose the Plugin Type for which you are changing the URL; for example, application or installation. |
| URL | The URL automatically displays. |
| Custom URL | Use only alphanumeric characters for the custom URL. |
| Show Plugin on User Option Pages | Check this check box to show the plug-in on the user option window. |