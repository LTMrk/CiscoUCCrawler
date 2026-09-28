---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-cpsintro-html-bb7a184f6e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/cpsintro.html
retrieved_at: 2026-08-21T16:10:42.737723+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Introduction

## Chapter: Introduction

## Introduction

This chapter provides an introduction to the Cisco Unified Presence Server system.

## Supported Cisco IP Phones

Table 1-1 shows the Cisco phones that are supported in Cisco Unified Presence Server 1.0(2) for both SIP and SCCP protocols.

Table 1-1 Supported Cisco IP Phones

12 SP

NA

No

30 VIP

NA

No

7902

NA

Yes

7910

NA

Yes

7905

No

Yes

7912

No

Yes

7940

No

Yes

7960

No

Yes

7935

NA

Yes

7936

NA

Yes

7920

NA

Yes

7911

Yes

Yes

7941

Yes

Yes

7961

Yes

Yes

7970

Yes

Yes

7971

Yes

Yes

7985 (Ocius)

NA

Yes

VT Advantage

Yes

Note This option is Yes only if SIP is available at the CTI gateway.

Yes

IP Communicator

NA

Yes

Cisco Unified Personal Communicator

No

NA

## Browsing to Cisco Unified Presence Server Administration

You access the Cisco Unified Presence Server Administration program from a PC that is not the web server and that does not have Cisco Unified Presence Server installed. No browser software exists on the server. See the "Web Browsers" section for more information on browsing to the server.

Additional Information

See the "Related Topics" section .

### Web Browsers

Cisco Unified Presence Server Administration supports the following Microsoft Windows operating system browsers:

• Microsoft Internet Explorer (IE) 6.0 or higher

• Netscape 7.2 or higher

From any user PC in your network, browse into a server that is running Cisco Unified Presence Server Administration and log in with administrative privileges.

Note Simultaneous logon to Cisco Unified Presence Server Administration by a large number of users can cause performance to suffer. Try to limit the number of users and administrators that are logged on simultaneously.

### Cisco Unified Presence Server Administration Logon

Use the following procedure to log on to Cisco Unified Presence Server Administration.

Use the following procedure to browse into the server and log on to Cisco Unified Presence Server Administration.

Step 1 Start your preferred operating system browser.

Step 2 In the address bar of the web browser, enter the following case-sensitive URL:

https://< server-name >

where: < server-name > equals the name or IP address of the server

Step 3 To log on to Cisco Unified Presence Server Administration, click the Cisco Unified Presence Server Administration link.

Step 4 A Security Alert dialog box displays. Click the appropriate button.

Step 5 At the Logon window, enter the application user password that you specified during Cisco Unified Presence Server installation and click Submit .

The Cisco Unified Presence Server Administration window displays.

Note For security purposes, Cisco Unified Presence Server Administration logs you out after 30 minutes, and you must log back in to continue using it.

Additional Information

See the "Related Topics" section .

### Cisco Unified Presence Server Administration Logoff

Use the following procedure to log off Cisco Unified Presence Server Administration.

Step 1 From the main Cisco Unified Presence Server Administration window, click the Log Off button that is in the upper, right corner (see Figure 1-1 ).

Step 2 The Logon window displays.

Additional Information

See the "Related Topics" section .

### Hypertext Transfer Protocol Over Secure Sockets Layer (HTTPS)

Hypertext Transfer Protocol over Secure Sockets Layer (SSL), which secures communication between the browser client and the web server (for Microsoft Windows users), uses a certificate and a public key to encrypt the data that is transferred over the internet. HTTPS also ensures that the user login password transports securely via the web. The following Cisco Unified CallManager applications support HTTPS, which ensures the identity of the server: Cisco Unified CallManager Administration, Cisco Unified CallManager Serviceability, the Cisco Unified CallManager User Options, Trace Collection Tool, the Real-Time Monitoring Tool (RTMT), and the XML (AXL) application programming interface.

A self-signed certificate gets generated on the web server at installation (the certificate also gets migrated during upgrades).

Note If you access the web application by using the hostname and install the certificate in the trusted folder and then try to access the application by using the localhost or IP address, the Security Alert dialog box displays to indicate that the name of the security certificate does not match the name of the site. If you use the localhost, the IP address, or the hostname in the URL to access the application that supports HTTPS, you must save the certificate in the trusted folder for each of type of URL (with the local host, IP address, and so on); otherwise, the Security Alert dialog box displays for each type.

### Using Internet Explorer and HTTPS with Cisco Unified Presence Server Administration

The following section describes how to save the CA Root certificate in the trusted folder, so the Security Alert dialog box does not display each time that you access the web application. The first time that you (or a user) access Cisco Unified Presence Server Administration or other Cisco Unified CallManager SSL-enabled virtual directories after the Cisco Unified CallManager 5.0 installation/upgrade from a browser client, a Security Alert dialog box asks whether you trust the server. When the dialog box displays, you must perform one of the following tasks:

• By clicking Yes, you choose to trust the certificate for the current web session only. If you trust the certificate for the current session only, the Security Alert dialog box displays each time that you access the application; that is, until you install the certificate in the trusted folder.

• By clicking View Certificate > Install Certificate, you indicate that you intend to perform certificate installation tasks, so you always trust the certificate. If you install the certificate in the trusted folder, the Security Alert dialog box does not display each time that you access the web application.

• By clicking No, you cancel the action. No authentication occurs, and you cannot access the web application. To access the web application, you must click Yes or install the certificate via the View Certificate > Install Certificate option.

For other tasks that you can perform in the Security Alert dialog box, refer to the Cisco Unified CallManager Security Guide .

Step 1 Browse to the application on the web server.

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

Note If you use the localhost, the IP address, or the hostname in the URL to access the application that supports HTTPS, you must save the certificate in the trusted folder for each of type of URL (with the local host, IP address, and so on); otherwise, the Security Alert dialog box displays for each type.

Additional Information

See the "Related Topics" section .

### Using Netscape and HTTPS with Cisco Unified Presence Server Administration

When you use HTTPS with Netscape, you can view the certificate credentials, trust the certificate for one session, trust the certificate until it expires, or not trust the certificate at all.

Tip If you trust the certificate for one session only, you must repeat the following procedure each time that you access the HTTPS-supported application. If you do not trust the certificate, you cannot access the application.

Perform the following procedure to save the certificate to the trusted folder:

Step 1 Browse to the application, for example, Cisco Unified Presence Server Administration, by using Netscape.

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

See the "Related Topics" section .

## Navigating the Cisco Unified Presence Server Administration Application

After you log on, the main Cisco Unified Presence Server Administration window displays. The window includes the drop-down list box called Navigation in the upper, right corner (see Figure 1-1 ). To access the applications in the drop-down list box, choose the program that you want and click Go . The choices in the drop-down list box include the following Cisco Unified Presence Server applications:

• Cisco Unified Presence Server Administration—Shows the default when you access Cisco Unified Presence Server. Use Cisco Unified Presence Server Administration to configure system parameters, applications, and much more.

• Cisco Unified Presence Server Serviceability—Takes you to the main Cisco Unified Presence Server Serviceability window that is used to configure trace files and alarms and to activate and deactivate services.

• Disaster Recovery System—Takes you to the Cisco Disaster Recovery System, a program that provides full data backup and restore capabilities for all servers in a Cisco Unified Presence Server cluster.

• Platform Administration—Takes you to a logon window, so you can configure and administer the Cisco Unified Presence Server platform.

Figure 1-1 Cisco Unified Presence Server Administration Navigation

These applications include additional security, so you must enter a userid and password before you can access these programs.

Additional Information

See the "Related Topics" section .

## Accessibility

Cisco Unified Presence Server Administration and Cisco Unified Presence Server User Options provide functionality for users that allows them to access buttons on the window without using a mouse. You can perform the following procedures from any point on the window, so the user does not have to scroll or tab through various fields.

Accessing the Icons in the Window

Many of the windows in Cisco Unified Presence Server and Cisco PCA have icons that display at the top of the window; for example, an icon of a disk for Save, an icon that is a plus sign (+) for Add, and so on. To access these icons, perform the following procedure.

1. Press Alt , press 1 , then press Tab . The cursor will highlight the first icon from the left. To move to the next icon, press Tab again.

2. Press Enter . The system performs the function of the icon; for example, Add.

Accessing the Buttons in the Window

Many of the windows in Cisco Unified Presence Server and Cisco PCA have buttons that display at the bottom of the window; for example, a button for Save, a button for Add, and so on. To access these buttons, perform the following procedure.

1. Press Alt , press 2 , and then press Tab . The cursor will highlight the first button from the left. To move to the next button, press Tab again.

2. Press Enter . The function of the button gets performed; for example, Save.

## Where to Find More Information

• Cisco Unified CallManager System Guide

• Cisco Unified CallManager Features and Services Guide

• Cisco Unified CallManager Serviceability System Guide

• Cisco Unified CallManager Serviceability Administration Guide

• Cisco CDR Analysis and Reporting Administration Guide

• Cisco IP Telephony Solution Reference Network Design Guide

• Installing Cisco Unified Presence Server Release 5.0(1)

• Cisco Unified CallManager Security Guide 5.0

• Cisco IP Telephony Platform Administration Guide

• Cisco IP Telephony Disaster Recovery System Administration Guide

## Related Topics

• Browsing to Cisco Unified Presence Server Administration

• Using Internet Explorer and HTTPS with Cisco Unified Presence Server Administration

• Hypertext Transfer Protocol Over Secure Sockets Layer (HTTPS)

• Navigating the Cisco Unified Presence Server Administration Application

• Accessibility

• Where to Find More Information

| Phone Type | SIP | SCCP |
|---|---|---|
| 12 SP | NA | No |
| 30 VIP | NA | No |
|  |  |  |
| 7902 | NA | Yes |
| 7910 | NA | Yes |
| 7905 | No | Yes |
| 7912 | No | Yes |
| 7940 | No | Yes |
| 7960 | No | Yes |
|  |  |  |
| 7935 | NA | Yes |
| 7936 | NA | Yes |
|  |  |  |
| 7920 | NA | Yes |
|  |  |  |
| 7911 | Yes | Yes |
| 7941 | Yes | Yes |
| 7961 | Yes | Yes |
| 7970 | Yes | Yes |
| 7971 | Yes | Yes |
|  |  |  |
| 7985 (Ocius) | NA | Yes |
| VT Advantage | Yes Note This option is Yes only if SIP is available at the CTI gateway. | Yes |
|  |  |  |
| IP Communicator | NA | Yes |
| Cisco Unified Personal Communicator | No | NA |