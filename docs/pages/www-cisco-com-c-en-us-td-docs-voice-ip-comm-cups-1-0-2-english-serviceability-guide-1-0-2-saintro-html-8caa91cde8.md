---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-serviceability-guide-1-0-2-saintro-html-8caa91cde8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/serviceability/guide/1_0_2/saintro.html
retrieved_at: 2026-08-21T16:05:49.335565+00:00
---

Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Introduction

## Chapter: Introduction

## Introduction

This chapter comprises the following topics:

• Cisco Unified Presence Server Serviceability Overview

• Accessing Cisco Unified Presence Server Serviceability

• Using Hypertext Transfer Protocol over Secure Sockets Layer (HTTPS)

• Using the Cisco Unified Presence Server Serviceability Interface

• Accessibility Features

• Where to Find More Information

## Cisco Unified Presence Server Serviceability Overview

Cisco Unified Presence Server Serviceability, a web-based troubleshooting tool for Cisco Unified Presence Server, provides the following functionality:

• Saves Cisco Unified Presence Server services alarms and events for troubleshooting and provides alarm message definitions.

• Saves Cisco Unified Presence Server services trace information to various log files for troubleshooting. Administrators can configure, collect, and view trace information.

• Monitors real-time behavior of the components in a Cisco Unified Presence Server cluster through the real-time monitoring tool (RTMT).

• Provides feature services that you can activate, deactivate, and view through the Service Activation window.

• Provides an interface for starting and stopping feature and network services.

• Archives reports that are associated with Cisco Unified Presence Server Serviceability tools.

• Allows Cisco Unified Presence Server to work as a managed device for SNMP remote management and troubleshooting.

• Monitors the disk usage of the log partition on a server (or all servers in the cluster).

## Accessing Cisco Unified Presence Server Serviceability

To access Cisco Unified Presence Server Serviceability, perform the following procedure:

Step 1 By using Netscape 7.1 (or later) or Internet Explorer 6.0 (or later), browse into the Cisco Unified Presence Server 1.0 server where Cisco Unified Presence Server Serviceability service runs.

Tip In the supported browser, enter https://<server name or IP address>:8443 , where server name or IP address equals the server where the Cisco Unified Presence Server Serviceability service runs and 8443 equals the port number for HTTPS. If you enter http://<server name or IP address>:8080 in the browser, the system redirects you to use HTTPS. HTTP uses the port number, 8080.

Step 2 Click the Cisco Unified Presence Server Administration link.

Step 3 If the system prompts you about certificates, see the "Using Hypertext Transfer Protocol over Secure Sockets Layer (HTTPS)" section .

Step 4 The first time that the system prompts you for a user name and password, enter CCMAdministrator for the username and the application user password that you specified during installation for the password.

Tip Any user who has the Standard CCMUsers role assigned can access Cisco Unified Presence Server Serviceability. For information on how to assign this role to a user, refer to the Cisco Unified Presence Server Administration Guide .

Step 5 After Cisco Unified Presence Server Administration displays, choose Serviceability from the Navigation drop-down list box in the upper, right corner of the window.

Cisco Unified Presence Server Serviceability displays.

Tip To return to the Cisco Unified Presence Server Serviceability main window at any time during the configuration, click Home in the upper, right corner of the application window.

Additional Information

See the Related Topics .

## Using Hypertext Transfer Protocol over Secure Sockets Layer (HTTPS)

This section contains information on the following topics:

• HTTPS Overview for Internet Explorer

• Saving the Certificate to the Trusted Folder in Internet Explorer

Hypertext Transfer Protocol over Secure Sockets Layer (SSL), which secures communication between the browser client and the Tomcat web server, uses a certificate and a public key to encrypt the data that is transferred over the internet. HTTPS, which ensures the identity of the server, supports applications, such Cisco Unified Presence Server Serviceability. HTTPS also ensures that the user login password transports securely via the web.

### HTTPS Overview for Internet Explorer

The first time that you (or a user) accesses Cisco Unified Presence Server Administration or other Cisco Unified Presence Server SSL-enabled virtual directories after the Cisco Unified Presence Server 1.0 installation/upgrade, a Security Alert dialog box asks whether you trust the server. When the dialog box displays, you must perform one of the following tasks:

• By clicking Yes, you choose to trust the certificate for the current web session only. If you trust the certificate for the current session only, the Security Alert dialog box displays each time that you access the application: that is, until you install the certificate in the trusted folder.

• By clicking View Certificate > Install Certificate, you indicate that you intend to perform certificate installation tasks, so you always trust the certificate. If you install the certificate in the trusted folder, the Security Alert dialog box does not display each time that you access the web application.

• By clicking No, you cancel the action. No authentication occurs, and you cannot access the web application. To access the web application, you must click Yes or install the certificate via the View Certificate > Install Certificate options.

Note The system issues the certificate by using the hostname. If you attempt to access a web application by using the IP address, the Security Alert dialog box displays, even though you installed the certificate on the client.

Additional Information

See the Related Topics .

### Saving the Certificate to the Trusted Folder in Internet Explorer

To save the CA Root certificate in the trusted folder, so the Security Alert dialog box does not display each time that you access the web application, perform the following procedure:

Step 1 Browse to the application on the Tomcat web server.

Step 2 When the Security Alert dialog box displays, click View Certificate .

Step 3 In the Certificate pane, click Install Certificate .

Step 4 Click Next .

Step 5 Click the Place all certificates in the following store radio button; click Browse .

Step 6 Browse to Trusted Root Certification Authorities .

Step 7 Click Next .

Step 8 Click Finish .

Step 9 To install the certificate, click Yes .

A message states that the import was successful. Click OK .

Step 10 In the lower, right corner of the dialog box, click OK .

Step 11 To trust the certificate, so you do not receive the dialog box again, click Yes .

Additional Information

See the Related Topics .

## Using Netscape to Save the Certificate to the Trusted Folder

When you use HTTPS with Netscape, you can view the certificate credentials, trust the certificate for one session, trust the certificate until it expires, or not trust the certificate at all.

Tip If you trust the certificate for one session only, you must repeat this procedure each time that you access the HTTPS-supported application. If you do not trust the certificate, you cannot access the application.

Perform the following procedure to save the certificate to the trusted folder:

Step 1 Browse to the application, for example, Cisco Unified Presence Server Serviceability, by using Netscape.

The certificate authority dialog box displays.

Step 2 Click one of the following radio buttons:

• Accept this certificate for this session

• Do not accept this certificate and do not connect

• Accept this certificate forever (until it expires)

Note If you choose Do not accept, the application does not display.

Note To view the certificate credentials before you continue, click Examine Certificate . Review the credentials, and click Close .

Step 3 Click OK .

The Security Warning dialog box displays.

Step 4 Click OK .

Additional Information

See the Related Topics .

## Using the Cisco Unified Presence Server Serviceability Interface

In addition to performing troubleshooting and service-related tasks in Cisco Unified Presence Server Serviceability, you can perform the following tasks:

• To display documentation for a single window, choose Help > This page in Cisco Unified Presence Server Serviceability.

• To display a list of documents that are available with this release of Cisco Unified Presence Server (or to access the online help index), choose Help > Contents > Contents and Index in Cisco Unified Presence Server Serviceability.

• To go directly to the home page in Cisco Unified Presence Server Serviceability from a configuration window, click the Home link in the upper, right corner of the window.

• To access Cisco Unified Presence Server Administration or other applications, choose the appropriate application from the Navigation drop-down list box in the upper, right corner of the window.

• To use the icons in Cisco Unified Presence Server Serviceability, see Table 1-1 .

Table 1-1 Icons in Cisco Unified Presence Server Serviceability

Adds a new configuration

Cancels the operation

Clears the configuration that you specify

Deletes the configuration that you choose

Shows the online help for the configuration

Refreshes the window to display the latest configuration

Restarts the service that you choose

Saves the information that you entered

Sets the default for the configuration

Starts the service that you choose

Stops the service that you choose

## Accessibility Features

Cisco Unified Presence Server Serviceability Administration provides functionality for users that allows them to access buttons on the window without using a mouse. These navigation shortcuts assist visually impaired or blind attendants to use the application.

Use Table 1-2 as a guide for navigating the interface by using keyboard shortcuts.

Table 1-2 Navigation Shortcuts for Cisco Unified Presence Server Serviceability

Alt

Moves focus to the browser menu bar.

Enter

Chooses the item with focus (menu option, button, and so on.)

Alt, arrow keys

Moves between browser menus.

Spacebar

Toggles control; for example, checks and unchecks a check box.

Tab

Moves focus to the next item in the tab order or to next control group

Shift+Tab

Moves focus to the previous item or group in the tab order

Arrow keys

Moves among controls within a group

Home

Moves to the top of the window if more than one screenful of information exists. Also, moves to the beginning of a line of user-entered text.

End

Moves to the end of a line of user-entered text.

Moves to the bottom of the window if more than one screenful of information exists.

Page Up

Scrolls up one screen.

Page Down

Scrolls down one screen.

## Where to Find More Information

• Cisco Unified Presence Server Administration Guide

Additional Information

See the Related Topics .

## Related Topics

• Using Hypertext Transfer Protocol over Secure Sockets Layer (HTTPS)

• HTTPS Overview for Internet Explorer

• Saving the Certificate to the Trusted Folder in Internet Explorer

| Icon | Purpose |
|---|---|
|  | Adds a new configuration |
|  | Cancels the operation |
|  | Clears the configuration that you specify |
|  | Deletes the configuration that you choose |
|  | Shows the online help for the configuration |
|  | Refreshes the window to display the latest configuration |
|  | Restarts the service that you choose |
|  | Saves the information that you entered |
|  | Sets the default for the configuration |
|  | Starts the service that you choose |
|  | Stops the service that you choose |

| Keystroke | Action |
|---|---|
| Alt | Moves focus to the browser menu bar. |
| Enter | Chooses the item with focus (menu option, button, and so on.) |
| Alt, arrow keys | Moves between browser menus. |
| Spacebar | Toggles control; for example, checks and unchecks a check box. |
| Tab | Moves focus to the next item in the tab order or to next control group |
| Shift+Tab | Moves focus to the previous item or group in the tab order |
| Arrow keys | Moves among controls within a group |
| Home | Moves to the top of the window if more than one screenful of information exists. Also, moves to the beginning of a line of user-entered text. |
| End | Moves to the end of a line of user-entered text. Moves to the bottom of the window if more than one screenful of information exists. |
| Page Up | Scrolls up one screen. |
| Page Down | Scrolls down one screen. |