---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-windows-221644-download-jabber-problem-report-prt-log-h-9e65ef723e
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-windows/221644-download-jabber-problem-report-prt-log.html
retrieved_at: 2026-08-21T06:57:14.950055+00:00
---

Download Jabber Problem Report (PRT) Logs Using Web-Server.

# Download Jabber Problem Report (PRT) Logs Using Web-Server.

### Download Options

Updated: February 7, 2024

Document ID: 221644

Contents

## Contents

## Introduction

This document describes how to setup a Web Server on a Windows machine and also has steps to transfer the Jabber PRT to a web server.

## Prerequisites

Cisco recommends that you have knowledge of these topics.

- Cisco Unified Communication Manager (CUCM)

- Cisco Jabber

### Requirements

### Components Used

The information in this document is based on these software versions:

CUCM version - 12.5.1.13900-152 Cisco Jabber version - 12.9.2.54247 XAMPP (Web Server) version - 7.4.10

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

### Network Diagram

Cisco Jabber > Windows_PC (with web-server XAMPP software)

### Configurations

These configuration steps help you to transfer the Jabber PRT to a web server using 'Hypertext Transfer' (HTTP - port 80) and also using 'Hypertext Transfer Protocol Secure' (HTTPS - port 443) Protocols.

1. XAMPP software installation on the Windows PC. 2. Initial configuration on XAMPP. 3. Setting up a 'Folder' to store the Jabber PRTs on the Windows server. 4. Create a "UC Service" and assign it to the "Service Profile" on the CUCM. 5. Assign the "Service Profile" to the Jabber End User. 6. Collecting the Jabber - PRT.

If you want to configure HTTPS (secured) based Web-Server, please configure these additional steps.

7. Generate "Server Key" and "Certificate Signing Request" (CSR) on the XAMPP. 8. Sign the CSR using Certificate Authoriy (CA) and get the CA signed certificate. 9. Upload the certificate and restart the Apache service. 10. Modify the URL on the "UC Service" 11. Collecting the Jabber - PRT.

#### 1. XAMPP software installation on the Windows PC.

Download XAMPP software (for windows) by clicking here .

The steps mentioned in these screenshots help you in installing the XAMPP on the Windows machine.

Click the Next button in the setup wizard.

Select the mentioned components and click the Next button.

Choose the installation folder and click the Next button.

Choose the language and click the Next button.

Click the Next button.

Click the Next button to proceed with installation.

Installation is in progress.

Click the Finish button.

#### 2. Initial configuration on XAMPP.

Open "XAMPP Control Panel" as an Administrator.

Run the 'XAMPP Control Panel' as an administrator.

Click on the Config button.

Click on the Config button.

Select the marked options and click the Save button.

Select the mentioned components  and click the Save button.

Start the Apache service by clicking the highlighted " X " button.

Start the Apache service.

Press the Config button and click on PHP .

Open the php file.

Ensure the " upload_max_filesize " value is set as 40M .

Set the value of  upload_max_filesize  to 40M.

Start the Apache service by clicking the Start button.

Click the Start button to bring up the Apache service.

Status messages display that the Apache service is running.

#### 3. Setting up a 'Folder' to store the Jabber PRTs on the Windows server.

Create a new folder " JabberPRT " inside the location " C:\xampp\htdocs ". This folder is used to store the Jabber PRTs. Also create a PHP script as shown in this screenshot.

Specify the folder location to store the Jabber's PRT logs.

Create a file " uploadprt.php " inside the location >> " C:\xampp\htdocs " and write these lines inside the .php file

<?php
$uploaddir = 'C:\xampp\htdocs\JabberPRT\\';
$uploadfile = $uploaddir . date('Y_m_d_H_i_s') . basename($_FILES['zipFileName']['name']);
move_uploaded_file($_FILES['zipFileName']['tmp_name'], $uploadfile);
?>

#### 4. Create a "UC Service" and assign it to the "Service Profile" on the CUCM.

Log in to the CUCM Administration web page and navigate : User Management > User Settings > UC Service .

Create a new UC Service .

Open 'UC Service' on the CUCM Administration web page.

Choose "Jabber Client Configuration (jabber-config.xml)" and choose appropriate values. Give the webserver and PHP file details in the URL as shown in this screenshot.

Section : Client

Parameter : PrtLogServerURL

Value : http://<WebServer_IP/FQDN>:80/uploadprt.php

Configuring the Web Server's details in  Jabber Client Configuration (jabber-config.xml) .

Navigate : User Management > User Settings > UC Service .

Assign the created UC services to the Service Profile .

Open 'Service Profile' on the CUCM Administration web page.

Assign the created  Jabber Client Configuration  to the 'Service Profile' and click the Save button.

#### 5. Assign the "Service profile" to the Jabber End User.

Ensure this Service Profile is associate to the Jabber End User .

Assign the  Service profile  to the Jabber End User.

#### 6. Collecting the Jabber - PRT.

For collecting the Jabber PRT, You can choose Jabber and click on the button " Generate PRT for selected ".

Collect the Jabber PRT.

You can find the Jabber PRT in the Web server (the location is configured in the PHP script).

The Web server contains the downloaded Jabber PRT file.

If you run a Wireshark capture on the Web Server during PRT transfer event, you see this information.

Wireshark capture on the Web server shows the PRT file transactions.

If you want to configure HTTPS (secured) based Web-Server, please configure these additional steps.

These steps help in installing Certificate Authority (CA) signed certificate on the WebServer and also, has Cisco CallManager (CCM) configurations for transferring the Jabber PRT via TLS1.2.

#### 7. Generate "Server Key" and "Certificate Signing Request" (CSR) on the XAMPP.

Open Shell in the XAMPP Control panel (webserver) and type openssl command and hit enter .

Run the command  openssl  via the Shell of the XAMPP Control panel.

Generate server key by running the command " genrsa -out server.key 2048 ".

Run the command  genrsa -out server.key 2048

Generate a Certificate Signing Request (CSR) by running these commands.

genrsa -out server.key 2048

req -new -sha1 -nodes -key server.key -out server.csr -days 0000

Provide the relevant info under these fields:

- Country Name.

- State or Province Name.

- Locality Name.

- Organization Name.

- Organizational Unit.

- Common Name.

- Email Address.

- Extra attributes.

Generate a Certificate Signing Request (CSR) for the Web Server.

You can find the CSR in this location.

C:\xampp\

Generated  Certificate Signing Request  (CSR) location.

Copy the server.csr to this folder location.

C:\xampp\apache\conf\ssl.csr

Copy the CSR file to a new folder location.

Copy the server.key file to the mentioned location:-

From C:\xampp\apache

To C:\xampp\apache\conf\ssl.key

Copy the server.key to a new folder location.

#### 8. Sign the CSR using Certificate Authority (CA) and get the CA signed certificate.

Get the CSR ( server.csr ) signed by the CA (LAB CA server - ADFSCAIMP) and get the CA-signed Webserver certificate " server.crt ".

Note : Ensure you save the cert in .crt format (and not as .cer or .der). This screenshot shows how to save the cert in .crt format using the Windows CA server (when downloading the signed cert)

Sign the CSR by Certificiate Authority (CA) server and get the signed certificate.

Signed Certificate.

#### 9. Upload the certificate and restart the Apache service.

Upload the server.crt in this location.

C:\xampp\apache\conf\ssl.crt

Upload the signed certificate.

After uploading the KEY/CSR/CERT, restart the Apache service.

Restart the Apache service by pressing the Stop & Start button.

On the CUCM, ensure the Tomcat certificate is signed by the same CA (Here the CA server is ADFSCAIMP).

Tomcat certificate signed by the same CA server.

#### 10. Modify the URL on the "UC Service"

Log in to the CUCM Administration web page and navigate : User Management > User Settings > UC Service .

Modify the Web Server URL accordingly as shown in this UC Service section.

Section : Client

Parameter : PrtLogServerURL

Value : https://<WebServer_FQDN>:443/uploadprt.php

Configuring the Web Server's details in  Jabber Client Configuration (jabber-config.xml) .

#### 11. Collecting the Jabber - PRT.

After that, generate PRT via CCM page.

Collect the Jabber PRT.

From the packet capture you can confirm that the traffic between Jabber and Web Server are encrypted via TLS1.2 (HTTPS-443):

Web server IP : 10.88.11.218 Jabber PC IP : 10.201.251.189

Wireshark capture on the Web server shows the PRT file transactions happened securely.

## Verify

You can find the Jabber PRT in the Web server (the location is configured in the PHP script).

The Web server contains the downloaded Jabber PRT file.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

## Related Information

- Collect PRT Logs Remotely

I hope this article is helpful !

### Revision History

1.0

07-Feb-2024

Initial Release

### Contributed by Cisco Engineers

Ramesh Balakrishnan

### This Document Applies to These Products

- Jabber for Windows

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 07-Feb-2024 | Initial Release |